import yt_dlp

def download_audio(url):
    ydl_audio = {
    'format': 'mp3/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3'
        }]
    }
    
    with yt_dlp.YoutubeDL(ydl_audio) as ydl:
        error_code = ydl.download(url)

def download_video(url):
    ydl_video = {
    'format': 'bestvideo[height<=1080]+bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4'
        }]
    }

    with yt_dlp.YoutubeDL(ydl_video) as ydl:
        error_code = ydl.download(url)
