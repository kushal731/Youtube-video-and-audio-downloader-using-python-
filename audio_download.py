ur=["https://youtu.be/IGti1RTS1wc?list=RDIGti1RTS1wc",
    "https://youtu.be/5vrntlvQor8?list=RD5vrntlvQor8",
    "https://youtu.be/F2m4HPLvj-4?list=RDF2m4HPLvj-4",
    "https://youtu.be/tOM-nWPcR4U?list=RDtOM-nWPcR4U",
    "https://youtu.be/tYSrY4iPX6w?list=RDtYSrY4iPX6w",
    "https://youtu.be/jZEA2mMwL1k?list=RDjZEA2mMwL1k",
    "https://youtu.be/dR9B_gPxjkk?list=RDdR9B_gPxjkk",
    "https://youtu.be/TFTnJzWRTJ8?list=RDdR9B_gPxjkk",
    "https://youtu.be/8of5w7RgcTc?list=RDdR9B_gPxjkk",
    "https://youtu.be/zaFGQEIcetM?list=RDdR9B_gPxjkk",
    "https://youtu.be/El9lOzNyPb4?list=RDdR9B_gPxjkk",
    "https://youtu.be/a3Ue-LN5B9U?list=RDdR9B_gPxjkk",
    "https://youtu.be/n2dVFdqMYGA?list=RDdR9B_gPxjkk",
    "https://youtu.be/sUf2PtEZris?list=RDdR9B_gPxjkk",
    "https://youtu.be/cL0KKSPjZf8?list=RDdR9B_gPxjkk",
    "https://youtu.be/RLzC55ai0eo?list=RDdR9B_gPxjkk",
    "https://youtu.be/GVizJ_jpUnw?list=RDdR9B_gPxjkk"]
import yt_dlp

# url = input("Enter YouTube music URL: ")
for url in ur:
    options = {
        "format": "bestaudio/best",
        "outtmpl": r"C:\Users\Ravi\Desktop\youtube download\songs\%(title)s.%(ext)s",
        "noplaylist": True,
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

        print("\nAudio download completed!")

    except Exception as error:
        print("Download failed:", error)