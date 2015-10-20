import matplotlib.pyplot as plt
import librosa
import numpy as np
import os

frameRate = 24

y, sr = librosa.load("C:\\andre.mp3", sr=(frameRate * 1000))
S = librosa.feature.melspectrogram(y=y, sr=(frameRate * 1000), n_mels=8,fmax=8000)
D = librosa.logamplitude(S,ref_power=np.max)
np.savetxt("C:\\newdata.dat", D)

value = []
samples = 0
for s in D:
    t=s
    value.append(t)

for s in value[1]:
    samples = samples + 1

print("Array: ")
print(value)
print("Samples: ")
print(samples)
print("Frames: ")
frames = (samples * 512) / 1000
print(frames)
print("Seconds: ")
print(frames/frameRate)
    		
arry = []
frameArry = []

for q in range(samples):
    tmpArry = []
    for r in range(8):
        arry = value[r]
        tmpArry.append(arry[q]+80)
    frameArry.append(tmpArry)

print("Frame Array: ")
print(frameArry)
np.savetxt("C:\\newdataArry.dat", frameArry)

print(stopscript)
os.system("pause")