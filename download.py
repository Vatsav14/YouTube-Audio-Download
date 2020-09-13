import os

# If importing moviepy throws an error, uncomment the following line
# and point the environment variable to where your ffmpeg.exe file is located

# os.environ["IMAGEIO_FFMPEG_EXE"] = "C:\\FFmpeg\\bin\\ffmpeg.exe"

import sys
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *


# To get the url of the video to download
url = sys.argv[1]

# To get the name with which you want to store the file
name = sys.argv[2]

# Now download the YouTube video as an mp4 file
ytd = YouTube(url).streams.first().download(filename="test")

# If you want the video and not the mp3 format, remove everything below this line
mp4 = "test.mp4"

# In the next line, change where you want to store the file
# If you want to change the name of the file, change the value of the name variable
mp3 = "<file location>" + name + ".mp3"
videoclip = VideoFileClip(mp4)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3)
audioclip.close()
videoclip.close()

# Delete the mp4 file from memory since we don't need it
os.remove(ytd)
