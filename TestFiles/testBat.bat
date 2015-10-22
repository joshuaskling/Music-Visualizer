SET bins=8
SET song=C:\classicalTest.mp3
python beat_frames.py %song%
python 1_bin_mel.py %song%
python n_bin_mel.py %song% %bins%