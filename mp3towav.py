import os
import random
from pydub import AudioSegment
import simpleaudio
from time import sleep

for file in os.listdir("../non-stop-pop-audio-files/spotify"):
    if file.endswith(".mp3"):
        sound = AudioSegment.from_mp3(f"../non-stop-pop-audio-files/spotify/{file}")
        sound.export(f"../non-stop-pop-audio-files/spotify/{file[:-4]}.wav", format="wav")