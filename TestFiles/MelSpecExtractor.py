import matplotlib.pyplot as plt
import librosa
import numpy as np
import os

# function declarations
#


# declare constants
#
frameRate = 24
sampleRate = 1000 * frameRate
melBins = 8
sampleHop = 500

# setup librosa functions/processing
#
y, sr = librosa.load("C:\\andre.mp3", sr=sampleRate)
S = librosa.feature.melspectrogram(y=y, sr=sampleRate, n_mels=melBins,fmax=8000,hop_length = sampleHop)
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
frames = (frameRate * (samples * sampleHop)) / sampleRate
print(frames)
print("Samples/Frame: ")
frameConversionRate = float(samples)/float(frames)
print(frameConversionRate)
print("Seconds: ")
print(frames/frameRate)

# convert the bin based Mel spectrogram array to a time based array
#	
timeArray = []
scaleFactor = 100/80

for q in range(samples):
    tmpArry = []
    for r in range(melBins):
	tmpValue = ((librosaMel[r])[q])+80
        tmpArry.append(int(tmpValue*scaleFactor))
    timeArray.append(tmpArry)
np.savetxt("C:\\MelTimeArray.dat", timeArray)

# downconvert the time array into an animation frame array
#
frameArray = []
for q in range(samples/frameConversionRate):
    tmpArry = []
    for r in range(melBins):
	tmpValue = (((timeArray[(2*q)])[r])+((timeArray[(2*q)+1])[r]))/2
        tmpArry.append(int(tmpValue))
    frameArray.append(tmpArry)
np.savetxt("C:\\MelFrameArray.dat", frameArray)

# confirm script execution
#
print("Frame Array Construction Finished")
print("")

print(stopscript)
os.system("pause")