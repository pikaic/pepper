#! /home/logan_18/anaconda3/envs/pepperenv/bin/python3


import whisper
import subprocess
import ffmpeg

model = whisper.load_model("medium.en")
result = model.transcribe("chatgpt/recording.mp3")
print(result["text"])