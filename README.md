# YouTube Audio & Video Downloader 🎵🎬

A Python-based mini project for downloading audio and video streams from supported YouTube URLs using `yt-dlp` and FFmpeg.

## 📌 Project Overview

The YouTube Audio & Video Downloader is a Python application that supports downloading available audio streams and video content. It demonstrates Python automation, third-party library integration, media processing, and file management.

## ✨ Features

* 🎵 Download available audio streams.
* 🎬 Download available video formats.
* 🔗 Process multiple YouTube URLs.
* ⚙️ Use FFmpeg for media processing and merging audio with video when needed.
* 📂 Save downloaded files to a specified local folder.
* 📊 Display download progress and error messages.
* 🛠️ Handle common download errors.

## 🛠️ Technologies Used

* **Python** — application logic and automation.
* **yt-dlp** — media stream extraction and downloading.
* **FFmpeg** — audio/video processing, format conversion, and stream merging.

## 📋 Requirements

* Python 3.10 or a compatible version.
* FFmpeg installed on your computer.
* An internet connection.
* The `yt-dlp` Python package and its recommended dependencies.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Install yt-dlp

```bash
python -m pip install -U "yt-dlp[default]"
```

### 3. Install FFmpeg

Download FFmpeg from its official website:

https://ffmpeg.org/

Ensure FFmpeg is accessible through your system PATH or configure its location in your Python script.

## ▶️ How to Run

1. Open the project folder in PowerShell or a terminal.
2. Run your Python script:

```bash
python main.py
```

3. Provide the required YouTube URLs according to your script's input format.
4. Select or configure audio-only or video downloading, if supported by your program.
5. Find the downloaded files in your configured output folder.

Replace `main.py` with your actual Python filename.

## 📁 Project Structure

```text
youtube-audio-video-downloader/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── old/          # Excluded from Git
└── songs/        # Excluded from Git
```

*This is an example structure. Your actual project may differ.*

## 🎯 Learning Outcomes

Through this project, I practised:

* Python scripting and automation.
* Integrating external Python libraries.
* Using FFmpeg for media processing.
* Handling exceptions and download errors.
* Managing files and output directories.
* Using Git and GitHub for version control.

## ⚠️ Important Notes

* The available audio and video quality depends on the source streams.
* Some downloads may fail because of network issues, unavailable content, or changes to the platform.
* Only download content you own or have permission to download, and follow YouTube's terms and applicable copyright laws.
* Downloaded media files are excluded from this GitHub repository.

## 👨‍💻 Author

**Kushal T R**

Python Mini Project

---

*Created for educational purposes and personal learning.*
