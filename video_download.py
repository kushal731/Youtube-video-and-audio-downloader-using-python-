
import yt_dlp

url = input("Enter YouTube video URL: ")

options = {
    "format": "bestvideo+bestaudio/best",
    "merge_output_format": "mkv",
    "outtmpl": r"C:\Users\Ravi\Desktop\%(title)s.%(ext)s",
    "noplaylist": True,

    # Exact FFmpeg installation folder
    "ffmpeg_location": (
        r"C:\Users\Ravi\AppData\Local\Microsoft\WinGet\Packages"
        r"\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe"
        r"\ffmpeg-9.0.2-full_build\bin"
    ),

    "progress": True,
}

try:
    with yt_dlp.YoutubeDL(options) as downloader:
        downloader.download([url])

    print("\nDownload completed successfully!")

except Exception as error:
    print(f"\nDownload failed: {error}")