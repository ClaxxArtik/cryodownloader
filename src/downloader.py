import yt_dlp
import os


def download_audio(url):

    audio_dir = os.path.join(
        "downloads", "audio"
    )  # Set the directory for audio downloads
    os.makedirs(audio_dir, exist_ok=True)  # Create the directory if it doesn't exist

    ydl_audio = {
        "format": "mp3/bestaudio/best",
        "outtmpl": os.path.join(
            audio_dir, "%(title)s.%(ext)s"
        ),  # Save to downloads/audio folder with title as filename
        "postprocessors": [
            {  # Extract audio using ffmpeg
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            },
            {"key": "EmbedThumbnail"},
        ],
        "writethumbnail": True,
    }

    with yt_dlp.YoutubeDL(ydl_audio) as ydl:
        error_code = ydl.download(url)


def download_video(url):

    video_dir = os.path.join(
        "downloads", "video"
    )  # Set the directory for video downloads
    os.makedirs(video_dir, exist_ok=True)  # Create the directory if it doesn't exist

    ydl_video = {
        "format": "bestvideo[height<=1080]+bestaudio/best",
        "outtmpl": os.path.join(
            video_dir, "%(title)s.%(ext)s"
        ),  # Save to downloads/video folder with title as filename
        "postprocessors": [
            {  # Extract audio using ffmpeg
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_video) as ydl:
        error_code = ydl.download(url)


def open_audio_dir():
    audio_dir = os.path.join("downloads", "audio")
    os.makedirs(audio_dir, exist_ok=True)
    os.startfile(audio_dir)


def open_video_dir():
    video_dir = os.path.join("downloads", "video")
    os.makedirs(video_dir, exist_ok=True)
    os.startfile(video_dir)
