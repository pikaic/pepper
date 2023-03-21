#! /home/logan_18/anaconda3/envs/peppercudaenv/bin/python3
# -*- encoding: UTF-8 -*-

# import openai
# import os

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



from pynput import keyboard
import time
import pyaudio
import wave
import sched
import sys

CHUNK = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.mp3"

p = pyaudio.PyAudio()
frames = []

def callback(in_data, frame_count, time_info, status):
    frames.append(in_data)
    return (in_data, pyaudio.paContinue)

class MyListener(keyboard.Listener):
    def __init__(self):
        super(MyListener, self).__init__(self.on_press, self.on_release)
        self.key_pressed = None
        self.wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        self.wf.setnchannels(CHANNELS)
        self.wf.setsampwidth(p.get_sample_size(FORMAT))
        self.wf.setframerate(RATE)
    def on_press(self, key):
        if key.char == 'r':
            self.key_pressed = True
        return True

    def on_release(self, key):
        if key.char == 'r':
            self.key_pressed = False
        return True


listener = MyListener()
listener.start()
started = False
stream = None

def recorder():
    global started, p, stream, frames

    if listener.key_pressed and not started:
        # Start the recording
        try:
            stream = p.open(format=FORMAT,
                             channels=CHANNELS,
                             rate=RATE,
                             input=True,
                             frames_per_buffer=CHUNK,
                             stream_callback = callback)
            print("Stream active:", stream.is_active())
            started = True
            print("start Stream")
        except:
            raise

    elif not listener.key_pressed and started:
        print("Stop recording")
        stream.stop_stream()
        stream.close()
        p.terminate()
        listener.wf.writeframes(b''.join(frames))
        listener.wf.close()
        print("You should have a wav file in the current directory")
        sys.exit()
    # Reschedule the recorder function in 100 ms.
    task.enter(0.1, 1, recorder, ())


print("Press and hold the 'r' key to begin recording")
print("Release the 'r' key to end recording")
task = sched.scheduler(time.time, time.sleep)
task.enter(0.1, 1, recorder, ())
task.run()