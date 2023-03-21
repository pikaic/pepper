# CHUNK = 1024  # Number of frames per buffer
# FORMAT = pyaudio.paInt16  # Format of audio data
# CHANNELS = 1  # Number of channels
# RATE = 44100  # Sampling rate in Hz
# WAVE_OUTPUT_FILENAME = "output.wav"  # Name of output file

# # Set up PyAudio object and stream object
# p = pyaudio.PyAudio()
# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)

# # Initialize variables for recording state and frames list
# recording = False  # True if space key is pressed, False otherwise
# frames = []  # List of audio frames

# # Define functions for key press and release events
# def on_press(key):
#     global recording
#     if key == keyboard.Key.ctrl:  # If space key is pressed
#         recording = True
#         print("Recording started...")

# def on_release(key):
#     global recording, frames
#     if key == keyboard.Key.ctrl:  # If space key is released
#         recording = False
#         print("Recording stopped.")
#         write_to_file(frames)
#         frames = []

# def write_to_file(frames):
#     print("Writing to file...")
#     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))
#     wf.close()
#     print("File written.")

# # Start the keyboard listener
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()

# # Stop the stream and terminate PyAudio object
# stream.stop_stream()
# stream.close()
# p.terminate()


from pynput import keyboard
import sounddevice as sd