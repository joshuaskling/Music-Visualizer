import librosa
import numpy as np
import os, sys
import time

# script setup and housekeeping
#
htmlBrk = '<br>'
os.chdir('.\\pyBlender\\Media\\')
print(os.getcwd())
print(htmlBrk)
audioPath = sys.argv[1]
print(audioPath)
print(htmlBrk)
samples = 0
frames = 0
samplesPerFrame = 2
melBins = int(sys.argv[2])
print(melBins)
print(htmlBrk)
frameRate = 24
sampleRate = 1000 * frameRate
sampleHop = (sampleRate/frameRate)/samplesPerFrame
scaleFactor = 100/80
print(htmlBrk)
print("Mel Spectrogram Processing Engine")
print(htmlBrk)
print("--------------")
print(htmlBrk)
time.sleep(1)
# setup librosa functions/processing
#
y, sr = librosa.load(audioPath + ".mp3", sr=sampleRate)
S = librosa.feature.melspectrogram(y=y, sr=sampleRate, n_mels=melBins,fmax=8000,hop_length = sampleHop)
librosaMel = librosa.logamplitude(S,ref_power=np.max)

# print out some information about what we're working with
#
samples = len(librosaMel[0])
print("Samples: " + str(samples))
print(htmlBrk)
frames = samples/samplesPerFrame
print("Anim. Frames: " + str(frames))
print(htmlBrk)
print("Samples/Frame: " + str(samplesPerFrame))
print(htmlBrk)
print("Seconds: " + str(frames/frameRate))
print(htmlBrk)
print("Mel Bins: " + str(melBins))
print(htmlBrk)
# convert the bin based Mel spectrogram array to a time based array
#
timeArray = []
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

os.chdir('..\\Output\\')
np.savetxt("n_bin_mel.lfa", frameArray)
# confirm script execution
#
print(htmlBrk)
print("**Frame Array Construction Finished**")
print(htmlBrk)
time.sleep(2)
