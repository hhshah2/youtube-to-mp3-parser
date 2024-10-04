# YouTube Audio Downloader

A Python script that downloads audio from YouTube videos or playlists, converts them to MP3 format, and adds metadata such as title, author, year, and thumbnail. It uses `yt_dlp` for downloading, `pydub` for audio processing, and `mutagen` for adding metadata.

## Features

- Downloads audio from YouTube videos or playlists.
- Converts audio to MP3 format.
- Adds metadata to the MP3 file (e.g., title, author, year, and thumbnail).
- User-friendly prompts to choose download options.

## Prerequisites

- Python 3.7 or later
- Required Python modules:
  - `yt_dlp`
  - `requests`
  - `pydub`
  - `mutagen`
- FFmpeg installed and accessible via the command line.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your_username/youtube-audio-downloader.git
   cd youtube-audio-downloader

    Install dependencies:

    sh

pip install yt_dlp requests mutagen pydub

Install FFmpeg:

    Windows: Download from FFmpeg website and add it to your PATH.
    macOS (using Homebrew):

    sh

brew install ffmpeg

Linux:

sh

        sudo apt-get install ffmpeg

Usage

    Run the script:

    sh

    python youtube_downloader.py

    Enter the required inputs:
        Is playlist (y or n)?: Specify whether the provided link is a playlist.
        Enter a YouTube URL or playlist to download: Provide the YouTube video or playlist URL.
        What directory would you like to download to?: Specify the directory to save the downloaded MP3 files (default is the current directory).

Example

sh

Is playlist(y or n)?: n
Enter a YouTube URL or playlist to download: https://www.youtube.com/watch?v=example_video_id
What directory would you like to download to?: ./downloads

This example will download the audio from the specified YouTube video and save it as an MP3 file in the ./downloads directory.
Notes

    Metadata: The script adds metadata, including the title, uploader, album title, year of upload, and thumbnail to the downloaded MP3 file.
    FFmpeg is required for extracting audio and converting it to MP3.
    Ensure that the output path exists before running the script to avoid errors.

Dependencies

    yt_dlp - for downloading YouTube videos and playlists.
    pydub - for working with audio files.
    mutagen - for adding metadata to MP3 files.
    requests - for downloading the thumbnail image.
