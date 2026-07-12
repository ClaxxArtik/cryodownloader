import yt_dlp
import os
import threading
import sys
import stat


def get_ffmpeg_path():
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Look for ffmpeg.exe in the bin/ folder
    ffmpeg_path = os.path.join(base_path, "bin", "ffmpeg.exe")

    if os.path.exists(ffmpeg_path):
        try:
            # Add execute permissions on Windows
            os.chmod(ffmpeg_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
        except:
            pass
        return ffmpeg_path

    # Fallback: try system PATH
    return "ffmpeg"


class Download:
    def __init__(self):
        self.audio_dir = os.path.join("downloads", "audio")
        self.video_dir = os.path.join("downloads", "video")
        os.makedirs(self.audio_dir, exist_ok=True)
        os.makedirs(self.video_dir, exist_ok=True)

        # Get FFmpeg path once and reuse it
        self.ffmpeg_location = get_ffmpeg_path()

    def audio(self, url):
        thread = threading.Thread(target=self._download_audio, args=(url,))
        thread.daemon = True
        thread.start()

    def video(self, url):
        thread = threading.Thread(target=self._download_video, args=(url,))
        thread.daemon = True
        thread.start()

    def _download_audio(self, url):
        audio_dir = self.audio_dir
        os.makedirs(audio_dir, exist_ok=True)

        ydl_audio = {
            "format": "mp3/bestaudio/best",
            "outtmpl": os.path.join(audio_dir, "%(title)s.%(ext)s"),
            "postprocessors": [
                {"key": "FFmpegExtractAudio", "preferredcodec": "mp3"},
                {"key": "EmbedThumbnail"},
            ],
            "writethumbnail": True,
            "ffmpeg_location": self.ffmpeg_location,
        }

        with yt_dlp.YoutubeDL(ydl_audio) as ydl:
            ydl.download(url)

    def _download_video(self, url):
        video_dir = self.video_dir
        os.makedirs(video_dir, exist_ok=True)

        ydl_video = {
            "format": "bestvideo[height<=1080]+bestaudio/best",
            "outtmpl": os.path.join(video_dir, "%(title)s.%(ext)s"),
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"},
            ],
            "merge_output_format": "mp4",
            "ffmpeg_location": self.ffmpeg_location,
        }

        with yt_dlp.YoutubeDL(ydl_video) as ydl:
            ydl.download(url)


class Open:
    def __init__(self):
        self.audio_dir = os.path.join("downloads", "audio")
        self.video_dir = os.path.join("downloads", "video")

    def audio(self):
        os.makedirs(self.audio_dir, exist_ok=True)
        os.startfile(self.audio_dir)

    def video(self):
        os.makedirs(self.video_dir, exist_ok=True)
        os.startfile(self.video_dir)
