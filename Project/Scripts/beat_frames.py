import librosa
import numpy as np
<<<<<<< HEAD:Project/Scripts/beat_frames.py
import os, sys
=======
import os
import sys
>>>>>>> 31ceaf5cd5749419471ed7784204c1c05b9929be:TestFiles/beat_frames.py

# script setup and housekeeping
#
<<<<<<< HEAD:Project/Scripts/beat_frames.py
os.chdir('..\\Media\\')
audioPath = sys.argv[1]
=======

if len(sys.argv) < 2:
	sys.exit("Not enough parameters. Please provide song location.")

# declare constants
#
audio_path = "./" + sys.argv[1]
>>>>>>> 31ceaf5cd5749419471ed7784204c1c05b9929be:TestFiles/beat_frames.py
frameRate = 24
sampleRate = 1000 * frameRate

print("")
print("")
print("")
print("Tempo/Beats Processing Engine")
print("--------------")
print("")

# setup librosa functions/processing
#
y, sr = librosa.load(audioPath + ".mp3", sr=sampleRate)
tempo, beats = librosa.beat.beat_track(y=y, sr=sampleRate)
beatArray = librosa.frames_to_time(beats, sr=sr)

# print out some information about what we're working with
#
print("Beats: " + str(len(beats)))
print("Tempo: " + str(int(tempo)))

# setup, fill, and save time and frame values for beat info
#
frameArray = []
for i in beatArray:
	i = i * 100
	i = int(i)
	i = float(i)
	i = i / 100
	frameArray.append(int(i*24))
<<<<<<< HEAD:Project/Scripts/beat_frames.py

os.chdir('..\\Output\\')
np.savetxt("beat_frames.lfa", frameArray)
os.chdir('..\\')
=======
np.savetxt("./Output/beat_frames.lfa", frameArray)
>>>>>>> 31ceaf5cd5749419471ed7784204c1c05b9929be:TestFiles/beat_frames.py

# confirm script execution
#
print("")
<<<<<<< HEAD:Project/Scripts/beat_frames.py
print("**Frame Array Construction Finished**")
print("")
=======

#os.system("pause")
>>>>>>> 31ceaf5cd5749419471ed7784204c1c05b9929be:TestFiles/beat_frames.py

