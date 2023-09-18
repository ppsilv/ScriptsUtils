import sys
from pytube import YouTube

def Download(link):
   youtubeObject = YouTube(link)
   youtubeObject = youtubeObject.streams.get_highest_resolution()
   try:
     youtubeObject.download()
   except:
     print("Has an error downloading")
   print("Download completed succesfull!")

 
# total arguments
n = len(sys.argv)
if n < 2 :
	print("usage: vdown <video url>\n\n")
	exit(1)
	
print("Total arguments passed.:", n)
 
# Arguments passed
print("Name of Python script..:", sys.argv[0])
print("nUrl...................:", sys.argv[1])
print("Downloading....\n")    
    
#link = input("Please what url?: ")
Download(sys.argv[1])

