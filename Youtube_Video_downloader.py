import os
video_url=input("Enter the video Url:")
os.system(f"yt-dlp -F {video_url}")
itag= input("Enter the format from the list: ")
os.system(f"yt-dlp -f {itag} {video_url}")