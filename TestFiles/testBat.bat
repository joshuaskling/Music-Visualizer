cls
SET/P song=Enter song path:
cls
SET/P bins=Enter number of mel bins (must be even):
cls
::SET bins=8
::SET song=C:\classicalTest.mp3
python beat_frames.py %song%
python 1_bin_mel.py %song%
python n_bin_mel.py %song% %bins%