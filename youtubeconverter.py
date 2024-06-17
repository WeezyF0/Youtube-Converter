import yt_dlp
import os

print("Insert the link")
link = input("Paste the YouTube Video link here: ")
dir = input("Enter the full path of the location where you want to save the file: ")
os.chdir(dir)
format = input("Download audio or video? (a/v): ")


if format == 'a':
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'ffmpeg_location': 'ffmpeg.exe'  
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(link)

else:
    ydl_opts = {
        'format': 'bv*+ba/b',
        'ffmpeg_location': 'ffmpeg.exe'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(link)