from pytube import YouTube

link = input("Enter the link: ")

a = YouTube(link)
b = a.streams.all()

m=1
for i in b:
    print(str(m)+" "+str(i))
    m += 1

c = int(input("Enter the option: "))

video = b[c-1]
video.download()
print("Downloaded...")
