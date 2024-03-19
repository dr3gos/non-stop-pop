import os
import random
from pydub import AudioSegment

combinedSongs = AudioSegment.empty()

songfilenames = []
for file in os.listdir("../non-stop-pop-audio-files"):
    if file.endswith(".wav"):
        if file != "test.wav":
            songfilenames.append(file)

random.shuffle(songfilenames)

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
    randomfile = generalfilenames[random.randint(0, len(generalfilenames) - 1)]

    djfile = AudioSegment.from_wav(f"../non-stop-pop-audio-files/gta5/{randomfolder}/{randomfile}")
    song = AudioSegment.from_wav(f"../non-stop-pop-audio-files/{i}")
    partofsong = song[:len(djfile)] - 20
    overlayedpart = djfile.overlay(partofsong, position=0)

    restofsong = song[len(djfile):]

    combinedSongs += overlayedpart
    combinedSongs += restofsong

    # combinedSongs += AudioSegment.from_wav(f"../non-stop-pop-audio-files/gta5/{randomfolder}/{randomfile}").overlay(AudioSegment.from_wav(f"../non-stop-pop-audio-files/{i}")[:len( AudioSegment.from_wav(f"../non-stop-pop-audio-files/gta5/{randomfolder}/{randomfile}"))] - 30, position=0)
    # # combinedSongs += AudioSegment.from_wav(f"../non-stop-pop-audio-files/{i}")[:len(randomfile)] - 30
    # combinedSongs += AudioSegment.from_wav(f"../non-stop-pop-audio-files/{i}")[len(AudioSegment.from_wav(f"../non-stop-pop-audio-files/{i}")[len(AudioSegment.from_wav(f"../non-stop-pop-audio-files/gta5/{randomfolder}/{randomfile}"))]):]

combinedSongs.export("../non-stop-pop-audio-files/test.wav", format="wav")
