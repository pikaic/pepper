#! /home/logan_18/anaconda3/envs/peppercudaenv/bin/python3
# -*- encoding: UTF-8 -*-

import whisper
import openai
import json
import pyaudio
import wave
import os
import functools
import subprocess
import pyglet

openai_api_key=""
path_to_save_recording="/home/logan_18/pepper/chatgpt/recordings"
recorded_audio_path="/home/logan_18/pepper/chatgpt/recordings/recording.mp3"

# Function to load the whisper model
@functools.lru_cache(maxsize=None)
def load_whisper_model():
    whisper_model=whisper.load_model("medium.en")
    return whisper_model

# Function to transcribe text from audio
def transcribe(audio_file):
    whisper_model=load_whisper_model()
    transcription = whisper_model.transcribe(audio_file)
    return transcription['text']

# Function to record audio when spacebar is pressed
def record_audio(path, filename):
    # Set the parameters for the audio stream
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 44100
    
    # Initialize the PyAudio object
    p = pyaudio.PyAudio()
    
    # Open the audio stream
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    
    frames = []
    
    # Create a key event handler for starting and stopping recording
    def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            print("Recording started")
            pyglet.clock.schedule_interval(on_update, 1 / 60.0)
    
    def on_key_release(symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            print("Recording stopped")
            pyglet.clock.unschedule(on_update)
            # Stop and close the audio stream
            stream.stop_stream()
            stream.close()
            
            # Terminate the PyAudio object
            p.terminate()
            
            # Save the recorded audio as a WAV file
            file_path = os.path.join(path, filename)
            wf = wave.open(file_path, 'wb')
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(sample_format))
            wf.setframerate(fs)
            wf.writeframes(b''.join(frames))
            wf.close()

            window.close()
    
    # Create a clock event handler for recording audio
    def on_update(dt):
        data = stream.read(chunk)
        frames.append(data)
    
    # Create a window and attach the key event handlers
    window = pyglet.window.Window()
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    
    # Start the Pyglet event loop
    pyglet.app.run()



# Function to record audio with a fixed duration
def record_audio_with_fixed_duration(path, filename, duration):
    # Set the parameters for the audio stream
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 44100
    
    # Initialize the PyAudio object
    p = pyaudio.PyAudio()
    
    # Open the audio stream
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    
    frames = []
    
    # Record the audio for the specified duration
    for i in range(int(fs / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)
    
    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    
    # Terminate the PyAudio object
    p.terminate()
    
    # Save the recorded audio as a WAV file
    file_path = os.path.join(path, filename)
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    # Convert the WAV file to MP3
    # os.system(f"ffmpeg -i {filename} -acodec libmp3lame -aq 4 {filename[:-4]}.mp3")

# Writing the output to a json file
def writing_response_to_json_file(answer):
    sorted_output=json.dumps(answer)
    with open('/home/logan_18/pepper/chatgpt/json_file.json', "w") as outfile:
        outfile.write(sorted_output)
    
   
# Function to generate chatgpt response
def chatgpt_response(question):
    # Loading the whisper model
    load_whisper_model()
    # using the openai api key
    openai.api_key=openai_api_key
    conversation=[{"role":"system","content":"You are a helpful assistant"}]
    # completion=openai.Completion.create(engine="text-davinci-003",prompt=question,max_tokens=1000)
    # response=completion.choices[0]['text']

    while(True):
        conversation.append({"role":"user","content": question})
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            temperature=0.2,
            max_tokens=1000,
            top_p=0.9
        )
        conversation.append({"role":"assistant","content":response['choices'][0]['message']['content']})
        answer=response['choices'][0]['message']['content']
        writing_response_to_json_file(answer)
        subprocess.run(['python2','/home/logan_18/pepper/chatgpt/chatgpt_output_file.py'])
        # print("\n" + answer + "\n")
        while(1):
            confirmation=input("Do you wish to continue asking questions? Enter Y or y for yes || Enter N or n for no: ")
            if(confirmation=='y' or confirmation=='Y'):
                print("What do you want to know? ")
                record_audio(path_to_save_recording, "recording.mp3")
                print("Question recorded")
                print("Transcribing audio")
                question=transcribe(recorded_audio_path)
                print("Audio Transcribed and question generated")
                print(question)
                # chatgpt_response(transcribed_text)
                break
            elif(confirmation=='n' or confirmation=='N'):
                return
            else:
                print("Invalid Option entered")

    # Writing the output to a json file
    # sorted_output=json.dumps(answer)
    # with open('/home/logan_18/pepper/chatgpt/json_file.json', "w") as outfile:
    #     outfile.write(sorted_output)
    


def main():
    # load_whisper_model()
    # while(1):
    print("What do you want to know?")
    # Record 7 seconds of audio
    record_audio(path_to_save_recording, "recording.mp3")
    print("Question recorded!!")
    # Transcribing audio
    print("Transcribing audio")
    result=transcribe(recorded_audio_path)
    print("Audio Transcribed and Question Generated: " + result)
    chatgpt_response(result)
    # Running the code in python 2.7 to execute on pepper
    # subprocess.run(['python','/home/logan_18/pepper/chatgpt/chatgpt_output_file.py'])
    # execute=input("Do you want to continue asking questions? If Yes: Press Y or y, If No: Press N or n---> ")
    # if(execute=='Y' or execute=='y'):
    #     continue
    # elif(execute=='N' or execute=='n'):
    #     return
    # else:
    #     print("Please enter valid option")



if __name__ == "__main__":
    main()