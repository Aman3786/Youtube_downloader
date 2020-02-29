# Note: you should have both module pytube and pytube3 installed in your pc.

from pytube import YouTube

link = input("Enter the link: ")

a = YouTube(link)
b = a.streams.all()  #It will show you all streams of video

m=1
for i in b:
    print(str(m)+" "+str(i))
    m += 1

c = int(input("Enter the option: "))

video = b[c-1]
print("Downloading...")
video.download()
print("Downloaded..")
