import librosa
import matplotlib.pyplot as plt
import numpy as np
import seaborn
import IPython.display
import os


audio_path = "C:\\andre.mp3"
y, sr = librosa.load(audio_path, sr=6000)
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
print("Tempo :")
print(tempo)
intArray = librosa.frames_to_time(beats, sr=sr)
doubArray = []
for i in intArray:
	i = i * 100
	i = int(i)
	i = float(i)
	i = i / 100
	doubArray.append(i)
np.savetxt("C:\\data.dat", doubArray)
print(doubArray)
os.system("pause")
