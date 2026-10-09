# YouTube Audio Downloader 🎵

A simple Python mini project that downloads audio streams from YouTube videos using `yt-dlp` and FFmpeg.

## 📌 Project Overview

The YouTube Audio Downloader is a Python-based application designed to retrieve audio streams from supported YouTube URLs. It demonstrates Python scripting, third-party library integration, command-line tools, and automated file handling.

## ✨ Features

* Download audio streams from supported YouTube URLs.
* Process multiple video URLs using Python.
* Use `yt-dlp` to retrieve available audio formats.
* Use FFmpeg for audio processing and conversion.
* Save downloaded files to a specified local folder.
* Display download progress and error messages.

## 🛠️ Technologies Used

* **Python** — application logic and automation.
* **yt-dlp** — media stream extraction and downloading.
* **FFmpeg** — audio processing and conversion.

## 📋 Requirements

* Python 3.10 or a compatible version.
* FFmpeg installed on your computer.
* An internet connection.
* The `yt-dlp` Python package.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

Replace the repository URL and folder name with your actual project details.

### 2. Install the required Python package

```bash
python -m pip install -U "yt-dlp[default]"
```

### 3. Install FFmpeg

Install FFmpeg using its official website:

https://ffmpeg.org/

Ensure FFmpeg is accessible from your system or configure its location in your Python script.

## ▶️ How to Run

1. Open the project folder in a terminal.
2. Add the YouTube URLs you are authorized to download to your Python script.
3. Verify that the output folder exists or is created by your program.
4. Run the script:

```bash
python main.py
```

Replace `main.py` with the actual name of your Python file.

## 📁 Project Structure

```text
youtube-audio-downloader/
├── main.py
├── README.md
├── .gitignore
├── old/          # Ignored by Git
└── songs/        # Ignored by Git
```

Your actual file and folder names may differ.

## ⚠️ Important Notes

* Audio quality depends on the source stream available from YouTube. Downloading cannot restore quality that was not present in the original source.
* Downloads may fail because of network issues, unavailable videos, or changes to the platform.
* Only download content you own or have permission to download, and follow YouTube's terms and applicable copyright laws.
* Downloaded media files are excluded from this repository through `.gitignore`.

## 🎯 Learning Outcomes

This project helped me practise:

* Python scripting and automation.
* Installing and using external Python libraries.
* Integrating command-line tools with Python.
* Handling errors during downloads.
* Managing project files with Git and GitHub.

## 👨‍💻 Author

**Kushal T R**

Python Mini Project

---

*Created for educational and learning purposes.*
