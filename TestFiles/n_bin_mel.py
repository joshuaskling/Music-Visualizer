import librosa
import numpy as np
import os
import sys

# function declarations
#

if len(sys.argv) < 3:
	sys.exit("Not enough parameters. Please provide song location and number of bins.")


# declare constants
#
audioPath = sys.argv[1]
samples = 0
frames = 0
samplesPerFrame = 2
melBins = sys.argv[2]
frameRate = 24
sampleRate = 1000 * frameRate
sampleHop = (sampleRate/frameRate)/samplesPerFrame
timeArray = []
scaleFactor = 100/80

# setup librosa functions/processing
#
y, sr = librosa.load(audioPath, sr=sampleRate)
S = librosa.feature.melspectrogram(y=y, sr=sampleRate, n_mels=melBins,fmax=8000,hop_length = sampleHop)
librosaMel = librosa.logamplitude(S,ref_power=np.max)



# print out some information about what we're working with
#
print("Array: ")
print(librosaMel)

print("Samples: ")
samples = len(librosaMel[1])
print(samples)

print("Anim. Frames: ")
frames = samples/samplesPerFrame
print(frames)

print("Samples/Frame: ")
print(samplesPerFrame)

print("Seconds: ")
print(frames/frameRate)

# convert the bin based Mel spectrogram array to a time based array
#	
for q in range(samples):
    tmpArry = []
    for r in range(melBins):
	tmpValue = ((librosaMel[r])[q])+80
        tmpArry.append(int(tmpValue*scaleFactor))
    timeArray.append(tmpArry)

# downconvert the time based array into an animation frame array
#
frameArray = []
for q in range(frames):
    tmpArry = []
    for r in range(melBins):
        tempValue = 0
        for s in range(samplesPerFrame):
	    tmpValue = tempValue + ((timeArray[(2*q)+s])[r])
        tmpValue = tmpValue / samplesPerFrame
        tmpArry.append(int(tmpValue))
    frameArray.append(tmpArry)
np.savetxt("C:/n_bin_mel.lfa", frameArray)

# confirm script execution
#
print("Frame Array Construction Finished")
print("")

#os.system("pause")