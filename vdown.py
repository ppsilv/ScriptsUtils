from pytube import YouTube

def Download(link):
   youtubeObject = YouTube(link)
   youtubeObject = youtubeObject.streams.get_highest_resolution()
   try:
     youtubeObject.download()
   except:
     print("Has an error downloading")
   print("Download completed succesfull!")

link = input("Please what url?: ")
Download(link)

