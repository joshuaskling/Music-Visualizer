import librosa
import matplotlib.pyplot as plt
import numpy as np
import seaborn
import IPython.display
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
timeArray = []
frameArray = []
for i in beatArray:
	i = i * 100
	i = int(i)
	i = float(i)
	i = i / 100
	timeArray.append(i)
	frameArray.append(int(i*24))
np.savetxt("C:\\BeatTimes.dat", timeArray)
np.savetxt("C:\\BeatFrames.dat", frameArray)

# confirm script execution
#
print(timeArray)
print(frameArray)
print("")

os.system("pause")

