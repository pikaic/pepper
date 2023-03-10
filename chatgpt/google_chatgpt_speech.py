#! /home/logan_18/anaconda3/envs/pepperenv/bin/python3
# -*- encoding: UTF-8 -*-

from google.cloud import speech
client=speech.SpeechClient.from_service_account_file('chatgpt/google_speech_api.json')

file_name="chatgpt/recording.mp3"

with open(file_name,'rb') as f:
    wav_data=f.read()


audio_file=speech.RecognitionAudio(content=wav_data)

config=speech.RecognitionConfig(
    sample_rate_hertz=44100,
    enable_automatic_punctuation=True,
    language_code='en-US'
)

response=client.recognize(
    config=config,
    audio=audio_file
)

print(response)

for result in response.results:
    print("Output: {}".format(result.alternatives[0].transcript))