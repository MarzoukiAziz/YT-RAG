import youtube_dl


def download_audio(video_url: str) -> str:
    ydl_opts = {"format": "bestaudio/best", "outtmpl": "audio.%(ext)s"}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        filename = (
            ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3")
        )

    return filename
