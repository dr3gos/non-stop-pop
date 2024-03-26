import os
import random
from pydub import AudioSegment
import simpleaudio
from time import sleep

combinedSongs = AudioSegment.empty()

def getRandomPath():
    foldernames = []
    for file in os.listdir("../non-stop-pop-audio-files/gta5"):
        if file != ".DS_Store":
            foldernames.append(file)
    generalfilenames = []
    foldernames.remove("nspf_to")
    foldernames.remove("nspf_time")
    randomfolder = foldernames[random.randint(0, len(foldernames)-1)]
    for file in os.listdir(f"../non-stop-pop-audio-files/gta5/{randomfolder}"):
        if file.endswith(".wav"):
            generalfilenames.append(file)
    randomfile = generalfilenames[random.randint(0, len(generalfilenames) - 1)]
    randomfilepath = f"../non-stop-pop-audio-files/gta5/{randomfolder}/{randomfile}"
    return randomfilepath

def play_audio(audio_segment):
    # Convert pydub AudioSegment to raw audio data
    audio_data = audio_segment.raw_data
    num_channels = audio_segment.channels
    bytes_per_sample = audio_segment.sample_width
    sample_rate = audio_segment.frame_rate

    # Play audio
    return simpleaudio.play_buffer(audio_data, num_channels, bytes_per_sample, sample_rate)

songfilenames = []
for file in os.listdir("../non-stop-pop-audio-files/spotify"):
    if file.endswith(".wav"):
        if file != "test.wav":
            songfilenames.append(file)
random.shuffle(songfilenames)



for i in songfilenames:

    randomfile = getRandomPath()

    djfile = AudioSegment.from_wav(randomfile)
    song = AudioSegment.from_wav(f"../non-stop-pop-audio-files/spotify/{i}")

    

    partofsong = song[:len(djfile)+500] - 15
    djpartofsong = djfile[:len(djfile)]
    restofsong = song[len(djfile)+500:]

    song = partofsong.append(restofsong, crossfade=500)

    finalsong = djfile.overlay(song, position=0)
    finalsong += song[len(djfile):]

    # finalsong.detectsilence(min_silence_len=100, silence_thresh=-20, seek_step=1)

    # combinedSongs += finalsong

    play_object = play_audio(finalsong)

    song_done = False
    while not song_done:
        if play_object.is_playing():
            sleep(0.1)
        else:
            song_done = True



# print("Exporting...")

# combinedSongs.export("../non-stop-pop-audio-files/test.wav", format="wav")


