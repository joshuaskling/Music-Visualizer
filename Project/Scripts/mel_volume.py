import librosa
import numpy as np
<<<<<<< HEAD:Project/Scripts/mel_volume.py
import os, sys
=======
import os
import sys
>>>>>>> 31ceaf5cd5749419471ed7784204c1c05b9929be:TestFiles/n_bin_mel.py

# script setup and housekeeping
#
<<<<<<< HEAD:Project/Scripts/mel_volume.py
os.chdir('..\\Media\\')
audioPath = sys.argv[1]
samplesPerFrame = 2
melBins = 1
=======

if len(sys.argv) < 3:
	sys.exit("Not enough parameters. Please provide song location and number of bins.")


# declare constants
#
audioPath = "./" + sys.argv[1]
samples = 0
frames = 0
samplesPerFrame = 2
melBins = int(sys.argv[2])
>>>>>>> 31ceaf5cd5749419471ed7784204c1c05b9929be:TestFiles/n_bin_mel.py
frameRate = 24
sampleRate = 1000 * frameRate
sampleHop = (sampleRate/frameRate)/samplesPerFrame
scaleFactor = 100/80

print("")
print("")
print("")
print("Volume Processing Engine")
print("--------------")
print("")

# setup librosa functions/processing
#
y, sr = librosa.load(audioPath + ".mp3", sr=sampleRate)
S = librosa.feature.melspectrogram(y=y, sr=sampleRate, n_mels=melBins,fmax=8000,hop_length = sampleHop)
librosaMel = librosa.logamplitude(S,ref_power=np.max)

# print out some information about what we're working with
samples = len(librosaMel[0])
print("Samples: " + str(samples))

frames = samples/samplesPerFrame
print("Anim. Frames: " + str(frames))

print("Samples/Frame: " + str(samplesPerFrame))

print("Seconds: " + str(frames/frameRate))

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
<<<<<<< HEAD:Project/Scripts/mel_volume.py

os.chdir('..\\Output\\')
np.savetxt("mel_volume.lfa", frameArray)
os.chdir('..\\')
=======
np.savetxt("./Output/n_bin_mel.lfa", frameArray)
>>>>>>> 31ceaf5cd5749419471ed7784204c1c05b9929be:TestFiles/n_bin_mel.py

# confirm script execution
#
print("")
<<<<<<< HEAD:Project/Scripts/mel_volume.py
print("**Frame Array Construction Finished**")
print("")
=======

#os.system("pause")
>>>>>>> 31ceaf5cd5749419471ed7784204c1c05b9929be:TestFiles/n_bin_mel.py
