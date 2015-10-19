import numpy as np
import librosa
from tempfile import TemporaryFile

#outfile = TemporaryFile()

y, sr = librosa.load("C:\\Users\\Admin\\Desktop\\Project2\\TestFiles\\andre.mp3")
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

np.save('outfile.npy', beats)

print(beats)
print(tempo)