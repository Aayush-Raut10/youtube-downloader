from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from typing import Optional
from utils import extract_video_id
from downloader import download_video
import os

app = FastAPI()



class VideoRequest(BaseModel):
    url:str
    quality: Optional[int] = Field(default=720, description="max video heighht like 320, 720, 180")
    format: Optional[str] = Field(default="mp4", description="video format like mp4, mkv")


@app.post("/download")
def download(videorequest: VideoRequest):

    url = videorequest.url

    video_id = extract_video_id(url)
   
    if video_id is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid URL of Youtube")
    
    # Now get a actual url for downloading vido
    absolute_url = f"https://www.youtube.com/watch?v={video_id}"

    video_path = download_video(absolute_url)

    if not os.path.exists(video_path):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Downloaded file not found!")

    return FileResponse(path=video_path, filename=os.path.basename(video_path), media_type="video/mp4")