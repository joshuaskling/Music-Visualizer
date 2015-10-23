ECHO OFF
CLS
ECHO.
SET/P song="What song would you like -->"
CLS
ECHO.
SET/P bins="How many bins would you like -->"
CLS
CD /D %~dp0
CD .\Scripts
CALL python beat_frames.py %song%
CALL python mel_volume.py %song%
CALL python n_bin_mel.py %song% %bins%
START blender empty.blend -P BlenderScript.txt %song%
ECHO.
ECHO.
ECHO.
PAUSE
