from pytube import YouTube
import time

video_url = input("link: ")

try:
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()
    video.download()
    print("downloaded!")
except Exception as e:
    print(str(e))
    time.sleep(3)
    exit()
