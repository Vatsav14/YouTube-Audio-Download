import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "C:\\FFmpeg\\bin\\ffmpeg.exe"
import sys
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *


# To get the url of the video to download
url = sys.argv[1]

# To get the name with which you want to store the file
name = sys.argv[2]

ytd = YouTube(url).streams.first().download(filename="test")
mp4 = "test.mp4"
mp3 = "C:\\Users\\Vatsav\\Music\\" + name + ".mp3"
videoclip = VideoFileClip(mp4)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3)
audioclip.close()
videoclip.close()
os.remove(ytd)
