from os import path
from pydub import AudioSegment

# files
src = "voice/*.mp3" # Name of the source mp3 file
dst = "test.wav" # result as a wav file

# convert mp3 to wav
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")