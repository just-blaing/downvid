from pytube import YouTube

print("Отправьте ссылку на видео.")
video_url = input()

try:
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()
    video.download()
    print("Ваше видео установлено! Оно находится в той же папке, где и код.")
except Exception as e:
    print("Произошла ошибка при установке видео:", str(e))
