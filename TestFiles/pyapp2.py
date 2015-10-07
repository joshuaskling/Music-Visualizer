import librosa
import matplotlib.pyplot as plt
import numpy as np
import seaborn
import IPython.display
import os

y, sr = librosa.load("C:\\andre.mp3")
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

hop_length = 512
plt.figure()
onset_env = librosa.onset.onset_strength(y, sr=sr,aggregate=np.median)
plt.plot(librosa.util.normalize(onset_env), label='Onset strength')
plt.vlines(beats, 0, 1, alpha=0.5, color='r',linestyle='--', label='Beats')
plt.legend(frameon=True, framealpha=0.75)
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

os.system("pause")
