#! /home/logan_18/anaconda3/envs/peppercudaenv/bin/python3
# -*- encoding: UTF-8 -*-

# import subprocess

# subprocess.run(['python','/home/logan_18/pepper/chatgpt/client.py'])

# import json
# import zmq

# # Create a ZeroMQ context
# context = zmq.Context()

# # Create a ZeroMQ socket of type REQ (request)
# socket = context.socket(zmq.REQ)

# # Connect the socket to the same port as the Python 2.7 process
# socket.connect("tcp://localhost:5555")

# # Prepare some data to send as a JSON object
# data = [1, 2, 3, 4, 5]

# # Serialize the data as a JSON object
# message = json.dumps(data)

# # Send the message to the Python 2.7 process
# socket.send(message.encode())

# # Wait for the response
# response = socket.recv()

# # Parse the response as a JSON object
# result = json.loads(response)

# print("Received result: %s" % result)







# import json
# import socket

# # Create a socket and connect it to the Python 2.7 process
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(('localhost', 8000))

# # Send JSON data to the Python 2.7 process
# json_data = {'message': 'Hello from Python 3.10'}
# json_str = json.dumps(json_data)
# sock.send(json_str.encode())

# # Receive JSON data from the Python 2.7 process
# data = sock.recv(1024)
# json_data = json.loads(data)
# print("Received data:", json_data['response'])

# # Close the connection
# sock.close()



# subprocess.run(['python2','/home/logan_18/pepper/chatgpt/client.py'])



import functools
# import whisper
# import openai
import pyaudio
import wave
import os
import keyboard

frames=[]

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
    
    # frames = []
    

    def callback(event):
        global frames
        if event.event_type=="down":
            print("Recording")
            frames=[]
            while not keyboard.is_pressed("space"):
                data=stream.read(chunk)
                frames.append(data)
            keyboard.unhook_all()
            print("recording stopped")


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
    
    # Set the keyboard callback
    keyboard.on_press(callback)
    
    # Start the keyboard listener
    keyboard.wait()


    # # Record the audio for the specified duration
    # for i in range(int(fs / chunk * duration)):
    #     data = stream.read(chunk)
    #     frames.append(data)
    
    # # Stop and close the audio stream
    # stream.stop_stream()
    # stream.close()
    
    # # Terminate the PyAudio object
    # p.terminate()
    
    # # Save the recorded audio as a WAV file
    # file_path = os.path.join(path, filename)
    # wf = wave.open(file_path, 'wb')
    # wf.setnchannels(channels)
    # wf.setsampwidth(p.get_sample_size(sample_format))
    # wf.setframerate(fs)
    # wf.writeframes(b''.join(frames))
    # wf.close()

    # Convert the WAV file to MP3
    # os.system(f"ffmpeg -i {filename} -acodec libmp3lame -aq 4 {filename[:-4]}.mp3")
    
# Example usage: Record 5 seconds of audio and save it as "recording.mp3"
print("What do you want to know?")
record_audio("/home/logan_18/pepper/chatgpt/recordings", "new_recording.mp3")