from pytube import YouTube
from time import sleep
import os
# test link = https://www.youtube.com/watch?v=kyM_wPi99Ms

######################
print("---------------------------------------------------------------------")
print(f"author = Kamesh(Hack-505)")
print("GitHub link = https://github.com/hack505")
print("test link of youtube = https://www.youtube.com/watch?v=kyM_wPi99Ms ")
print("---------------------------------------------------------------------")
######################

print(" ")

link = input("Enter th Link:")
loc = f""

path = input("Do you want to change the download path (y/n):")

if path  == "y":
    location = input("Paste the path to download:")
    sleep(1)
    print(f"{loc}----------{location}----------")

else:
    location = f"downloads_file"
    print(f"{loc}---------{location}-----------")

yt = YouTube(link)

print("-----------------------------------------------------------------------------------------------------")
print('Title:', yt.title)
print("-----------------------------------------------------------------------------------------------------")
print('Number of View:', yt.views)
print("-----------------------------------------------------------------------------------------------------")
print('Length of Video:', yt.length)
print("-----------------------------------------------------------------------------------------------------")
print('Description:', yt.description)
print("-----------------------------------------------------------------------------------------------------")
print('Rating:', yt.rating)
print("-----------------------------------------------------------------------------------------------------")
print(yt.streams)
print("-----------------------------------------------------------------------------------------------------")
print(yt.streams.filter(only_audio=True))
print("-----------------------------------------------------------------------------------------------------")
print(yt.streams.filter(only_video=True))
print("-----------------------------------------------------------------------------------------------------")
print(yt.streams.filter(progressive=True))
ys = yt.streams.get_highest_resolution()
ys = yt.streams.get_by_itag('22')
ys.download(f"{location}")

print("..............Download Completed..............")
print(f"file = {location}\{yt.title}.mp4")
print("Thank you.............")

os.system("pause")
