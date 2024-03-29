import os
import random
from pydub import AudioSegment

combinedSongs = AudioSegment.empty()

def getRandomPath():
    foldernames = []
    for file in os.listdir("../non-stop-pop-audio-files/gta5"):
        if file != ".DS_Store":
            foldernames.append(file)
    generalfilenames = []
    randomfolder = foldernames[random.randint(0, len(foldernames)-3)]
    for file in os.listdir(f"../non-stop-pop-audio-files/gta5/{randomfolder}"):
        if file.endswith(".wav"):
            generalfilenames.append(file)
    randomfile = generalfilenames[random.randint(0, len(generalfilenames) - 1)]
    randomfilepath = f"../non-stop-pop-audio-files/gta5/{randomfolder}/{randomfile}"
    return randomfilepath

songfilenames = []
for file in os.listdir("../non-stop-pop-audio-files"):
    if file.endswith(".wav"):
        if file != "test.wav":
            songfilenames.append(file)
random.shuffle(songfilenames)

for i in songfilenames:

    randomfile = getRandomPath()

    djfile = AudioSegment.from_wav(randomfile)
    song = AudioSegment.from_wav(f"../non-stop-pop-audio-files/{i}")

    

    partofsong = song[:len(djfile)+500] - 15
    djpartofsong = djfile[:len(djfile)]
    restofsong = song[len(djfile)+500:]

    song = partofsong.append(restofsong, crossfade=500)

    finalsong = djfile.overlay(song, position=0)
    finalsong += song[len(djfile):]

    combinedSongs += finalsong

combinedSongs.export("../non-stop-pop-audio-files/test.wav", format="wav")
