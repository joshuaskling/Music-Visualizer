import os
import librosa
import numpy as np
import os, sys
import time
import logging

def beat_frames(audioPath):
	# script setup and housekeeping
	#
	frameRate = 24
	sampleRate = 1000 * frameRate

	sout("")
	sout("")
	sout("Tempo/Beats Processing Engine")
	sout("--------------")
	sout("")

	# setup librosa functions/processing
	#
	y, sr = librosa.load(audioPath, sr=sampleRate)
	tempo, beats = librosa.beat.beat_track(y=y, sr=sampleRate)
	beatArray = librosa.frames_to_time(beats, sr=sr)

	# sout out some information about what we're working with
	#
	sout("Beats: " + str(len(beats)))
	sout("Tempo: " + str(int(tempo)))

	# setup, fill, and save time and frame values for beat info
	#
	frameArray = []
	for i in beatArray:
		i = i * 100
		i = int(i)
		i = float(i)
		i = i / 100
		frameArray.append(int(i*24))

	np.savetxt(".\\pyBlender\\Output\\beat_frames.lfa", frameArray)

	# confirm script execution
	#
	sout("")
	sout("**Frame Array Construction Finished**")
	sout("")
	time.sleep(2)

def mel_volume(audioPath):
	# script setup and housekeeping
	#
	samplesPerFrame = 2
	melBins = 1
	frameRate = 24
	sampleRate = 1000 * frameRate
	sampleHop = (sampleRate/frameRate)/samplesPerFrame
	scaleFactor = 100/80

	sout("")
	sout("")
	sout("Volume Processing Engine")
	sout("--------------")
	sout("")

	# setup librosa functions/processing
	#
	S = librosa.feature.melspectrogram(y=y, sr=sampleRate, n_mels=melBins,fmax=8000,hop_length = sampleHop)
	librosaMel = librosa.logamplitude(S,ref_power=np.max)

	# sout out some information about what we're working with
	samples = len(librosaMel[0])
	sout("Samples: " + str(samples))

	frames = samples/samplesPerFrame
	sout("Anim. Frames: " + str(frames))

	sout("Samples/Frame: " + str(samplesPerFrame))

	sout("Seconds: " + str(frames/frameRate))

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

	np.savetxt(".\\pyBlender\\Output\\mel_volume.lfa", frameArray)

	# confirm script execution
	#
	sout("")
	sout("**Frame Array Construction Finished**")
	sout("")
	time.sleep(2)
	
	
def n_bin_mel(audioPath, bins):
	bins = int(bins)
	# script setup and housekeeping
	#
	samples = 0
	frames = 0
	samplesPerFrame = 2
	frameRate = 24
	sampleRate = 1000 * frameRate
	sampleHop = (sampleRate/frameRate)/samplesPerFrame
	scaleFactor = 100/80
	sout("")
	sout("")
	sout("Mel Spectrogram Processing Engine")
	sout("--------------")
	# setup librosa functions/processing
	#
	M  = librosa.feature.melspectrogram(y=y, sr=sampleRate, n_mels=bins, fmax=8000,hop_length = sampleHop)
	librosaMel = librosa.logamplitude(M,ref_power=np.max)

	# sout out some information about what we're working with
	#
	samples = len(librosaMel[0])
	sout("Samples: " + str(samples))
	frames = samples/samplesPerFrame
	sout("Anim. Frames: " + str(frames))
	sout("Samples/Frame: " + str(samplesPerFrame))
	sout("Seconds: " + str(frames/frameRate))
	sout("Mel Bins: " + str(bins))
	# convert the bin based Mel spectrogram array to a time based array
	#	
	timeArray = []
	for q in range(samples):
		tmpArry = []
		for r in range(bins):
			tmpValue = ((librosaMel[r])[q])+80
			tmpArry.append(int(tmpValue*scaleFactor))
		timeArray.append(tmpArry)

	# downconvert the time based array into an animation frame array
	#
	frameArray = []
	for q in range(frames):
		tmpArry = []
		for r in range(bins):
			tempValue = 0
			for s in range(samplesPerFrame):
				tmpValue = tempValue + ((timeArray[(2*q)+s])[r])
			tmpValue = tmpValue / samplesPerFrame
			tmpArry.append(int(tmpValue))
		frameArray.append(tmpArry)
	np.savetxt(".\\pyBlender\\Output\\n_bin_mel.lfa", frameArray)
	# confirm script execution
	#
	sout("")
	sout("**Frame Array Construction Finished**")
	sout("")
	time.sleep(2)

def core_insert(core):
	sout("")
	sout("")
	sout("Scene\\Render Core Fusion Engine")
	sout("--------------")
	sout("")

	scenePath  =  ".\\pyBlender\\Scripts\\SceneSetup.txt"
	corePath   =  ".\\pyBlender\\Scripts\\RenderingCores\\" + core + ".txt"
	scriptPath =  ".\\pyBlender\\Output\\RenderScript.txt"

	sout("Scene will be rendered with core:")
	sout(corePath)

	filenames = [scenePath, corePath]
	with open(scriptPath, 'w') as outputFile:
		for file in filenames:
			with open(file) as inputFile:
				outputFile.write(inputFile.read())

	# confirm script execution
	#
	sout("")
	sout("**Render Script Construction Finished**")
	sout("")
	time.sleep(2)


def sout(input):
	logging.info(input)
	
def main(args):
	# script setup and housekeeping
	#
	logging.basicConfig(
		filename = "Out.txt",
		level = logging.DEBUG, 
		format = '[webPy]: %(message)s'
	)

	sout("autoBlender Python Web Service - *Started* @ %s" % time.ctime())
	sout("");
	sout("");
	sout("System:")
	sout("---------------------------")
	sout("Args: " + ', '.join(args))
	sout("CWD: " + os.getcwd())
	sout("")
	audioPath = (".\pyBlender\Output\userMusic.mp3")
	melBins = args[1]
	core = "VUmeter"
	beat_frames(audioPath)
	mel_volume(audioPath)
	n_bin_mel(audioPath, melBins)
	core_insert(core)
	sout("")
	sout("")
	sout("")
	sout("")
	
if __name__ == '__main__':
    main(sys.argv)