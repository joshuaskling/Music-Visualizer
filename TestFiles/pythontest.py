import matplotlib.pyplot as plt
import librosa
import numpy as np
import os

# function declarations
#
def scale(input):
    input = (input - minVol) * scaleFactor
    input = input * scaleFactor
    return input

# declare constants
#
frameRate = 24
sampleRate = 1000 * frameRate


# setup librosa functions/processing
#
y, sr = librosa.load("C:\\andre.mp3", sr=sampleRate)
S = librosa.feature.melspectrogram(y=y, sr=sampleRate, n_mels=8,fmax=8000)
librosaMel = librosa.logamplitude(S,ref_power=np.max)
np.savetxt("C:\\newdata.dat", librosaMel)
samples = len(librosaMel[1])

# print out some information about what we're working with
#
print("Array: ")
print(librosaMel)
print("Samples: ")
print(samples)
print("Anim. Frames: ")
frames = (frameRate * (samples * 512)) / sampleRate
print(frames)
print("Seconds: ")
print(frames/frameRate)

# convert the bin based Mel spectrogram array to a time based array
#	
frameArry = []
scaleFactor = 1.25

for q in range(samples):
    tmpArry = []
    for r in range(8):
	tmpValue = ((librosaMel[r])[q])+80
        tmpArry.append(int(tmpValue*scaleFactor))
    frameArry.append(tmpArry)

print("Frame Array Finished")
np.savetxt("C:\\newdataArry.dat", frameArry)










print(stopscript)
os.system("pause")