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

print(value)

for s in value[1]:
    samples = samples + 1

print(samples)

arry = []
for r in range(8):
    arry = value[r]
    for q in range(samples):
        print("Hi")
print("Samp: ")
print(samples)
print("Frames: ")
frames = (samples * 512) / 1000
print(frames)
print("Seconds: ")
print(frames/24)
    		




freqBuckets=value[1]

for i in freqBuckets:
    totSamp = totSamp + 1

for i in range (8):
    freqBuckets = value[i]

os.system("pause")