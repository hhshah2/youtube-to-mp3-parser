import yt_dlp
import requests
from pydub import AudioSegment
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TYER, APIC
import os
import re

def handle_playlist(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def convert_to_mp3(info_dict, output_path='.'):
    video_title = re.sub(r'[^a-zA-Z0-9 \n\.]', '', info_dict['title'])
    mp3_file = f"{video_title}.mp3"

    # Adding metadata
    audio = ID3(mp3_file)
    audio.add(TIT2(encoding=3, text=info_dict['title']))  # Title
    audio.add(TPE1(encoding=3, text=info_dict['uploader']))  # Author
    audio.add(TALB(encoding=3, text=info_dict['title']))  # Album Title
    audio.add(TYER(encoding=3, text=str(info_dict['upload_date'][:4])))  # Year of Upload

    # Download and add thumbnail
    thumbnail_url = info_dict['thumbnail']
    thumbnail_data = requests.get(thumbnail_url).content
    audio.add(APIC(
        encoding=3,
        mime='image/jpeg',
        type=3,
        desc='Cover',
        data=thumbnail_data
    ))
    audio.save(v2_version=3)

    # Optionally remove the thumbnail image if downloaded separately
    thumbnail_path = f"{video_title}.jpg"
    if os.path.exists(thumbnail_path):
        os.remove(thumbnail_path)

def main():
    try:
        is_playlist = input("Is playlist(y or n)?: ")
        link = input("Enter a YouTube URL or playlist to download: ")
        output_path = input("What directory would you like to download to?: ") or "."
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            if is_playlist == "y":
                ydl.download([link])
            else:
                info_dict = ydl.extract_info(link, download=True)
                convert_to_mp3(info_dict, output_path)

    except Exception as e:
        print("An error occurred: ", str(e))

if __name__ == "__main__":
    main()
