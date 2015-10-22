import librosa
import numpy as np
import os

# function declarations
#


# declare constants
#
audio_path = "C:\\andre.mp3"
frameRate = 24
sampleRate = 1000 * frameRate

# setup librosa functions/processing
#
y, sr = librosa.load(audio_path, sr=sampleRate)
tempo, beats = librosa.beat.beat_track(y=y, sr=sampleRate)
beatArray = librosa.frames_to_time(beats, sr=sr)

# print out some information about what we're working with
#
print("Tempo :")
print(tempo)

# setup, fill, and save time and frame values for beat info
#
frameArray = []
for i in beatArray:
	i = i * 100
	i = int(i)
	i = float(i)
	i = i / 100
	frameArray.append(int(i*24))
np.savetxt("C:\\beat_frames.lfa", frameArray)

# confirm script execution
#
print("Frame Array Construction Finished: ")
print(frameArray)
print("")

os.system("pause")

