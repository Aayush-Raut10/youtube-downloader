import os
import yt_dlp

PATH_TO_DOWNLOAD = "downloads"

def download_video(url:str):
    if not os.path.exists(PATH_TO_DOWNLOAD):
        os.makedirs(PATH_TO_DOWNLOAD)


    ydl_opts = {
        'outtmpl':f"{PATH_TO_DOWNLOAD}/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)
    
    return file_path