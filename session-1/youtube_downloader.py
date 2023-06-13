import os

from pytube import YouTube

os.chdir("/Users/valentin/Documents/VHS Kurse/Automatisierung mit Python/Demo Ordner")

url = "https://www.youtube.com/watch?v=LzGBQerkvWs"

new_video = YouTube(url)

print(new_video.title)

audio = new_video.streams.filter(only_audio=True).first()

best_video = new_video.streams.get_highest_resolution()

#best_video.download()

out_file = audio.download()

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

os.mkdir("musik")
os.rename(new_file, os.getcwd() + "/musik/" + audio.title + ".mp3")