import os.path
import yt_dlp
import sys
import argparse
from datetime import datetime

# Create a datetime object
now = datetime.now()


# sys.path.append('/path/to/your/exe/file/location')


def download_youtube_video_yt_dlp(url, output_path='downloads'):
    ydl_opts = {
        # 'format': 'bestvideo+bestaudio/best',  # Download best quality video and audio
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output template for filename
        'merge_output_format': 'mp4',  # Merge video and audio into MP4
        'ignoreerrors': True,  # Continue downloading even if some videos fail
        'download_archive': 'downloaded_videos.txt',
        'verbose': True,
        'keepvideo': True,  # don't delete video after audio is extracted
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav'
        }],
        "output": "[%(id)02d]--%(title)s.%(ext)s",
        # 'no_check_certificate': True,
        # 'simulate': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Video downloaded successfully to {output_path}!")
    except Exception as e:
        print(f"An error occurred: {e}")


def clean(directory_path, extension="wav"):
    for filename in os.listdir(directory_path):
        if filename.endswith(extension):
            file_path = os.path.join(directory_path, filename)
            try:
                os.remove(file_path)
                print(f"Removed: {file_path}")
            except OSError as e:
                print(f"Error removing {file_path}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script description here")
    parser.add_argument("-u", "--url", help="rutube playlist url")
    parser.add_argument("-o", "--out", help="target local folder", default=f"~/downloads/{now.strftime("%Y%m%d-%H%M")}")
    args = parser.parse_args()

    # video_url = input("Enter YouTube video URL: ")
    print(f"URL : {args.url}")
    print(f"DIR : {args.out}")

    if not os.path.exists(args.out):
        os.makedirs(args.out, exist_ok=True)

    download_youtube_video_yt_dlp(args.url, args.out)

    clean(args.out)
