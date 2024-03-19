import os
import random
from pydub import AudioSegment

combinedSongs = AudioSegment.empty()

songfilenames = []
for file in os.listdir("../non-stop-pop-audio-files"):
    if file.endswith(".wav"):
        if file != "test.wav":
            songfilenames.append(file)

foldernames = []

# foldernames = os.listdir("../non-stop-pop-audio-files/gta5")

for file in os.listdir("../non-stop-pop-audio-files/gta5"):
    # if file.endswith(".wav"):
    if file != ".DS_Store":
        foldernames.append(file)

generalfilenames = []

randomfolder = foldernames[random.randint(0, len(foldernames)-3)]

for file in os.listdir(f"../non-stop-pop-audio-files/gta5/{randomfolder}"):
    if file.endswith(".wav"):
        generalfilenames.append(file)

# print(os.listdir())

# print(songfilenames)

random.randint(0, len(songfilenames) - 1)

for i in songfilenames:
    combinedSongs += AudioSegment.from_wav(f"../non-stop-pop-audio-files/gta5/{randomfolder}/{generalfilenames[random.randint(0, len(generalfilenames) - 1)]}")
    combinedSongs += AudioSegment.from_wav(f"../non-stop-pop-audio-files/{i}")

combinedSongs.export("../non-stop-pop-audio-files/test.wav", format="wav")
