# pip install yt_dlp
import os
import yt_dlp


def download_video():
    url = input("ссылка: ")
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'quiet': False,
        'verbose': True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', 'unknown')
            video_duration = info_dict.get('duration', 0)
            video_file = f"{video_title}.mp4"
            video_size = os.path.getsize(video_file)
            duration_str = f"{video_duration // 60} min {video_duration % 60} sec"
            size_str = f"{video_size / (1024 * 1024):.2f} МБ"
            print(f"скачано!\n"
                  f"имя: {video_title}\n"
                  f"длина: {duration_str}\n"
                  f"размер: {size_str}\n"
                  f"название файла: {video_file}")
    except Exception as e:
        print(f"{str(e)}")

if __name__ == "__main__":
    download_video()
