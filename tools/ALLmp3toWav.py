from pydub import AudioSegment
import glob, os


# Will convert all mp3 files to wav files
os.chdir("voice")
for file in glob.glob("*.mp3"):
    sound = AudioSegment.from_mp3(file)
    sound.export(file.replace(".mp3", ".wav"), format="wav")
    os.remove(file)
