      
# YT-Ledger: YouTube Archival & Reporting Pipeline

YT-Ledger is a powerful Python script that uses `yt-dlp` to create a comprehensive archival pipeline for YouTube playlists and individual videos. It fetches detailed metadata, optionally downloads the videos and subtitles, and generates professional, easy-to-read reports in **XLSX**, **HTML**, and **PDF** formats.

## Key Features

-   **Batch Processing:** Process multiple YouTube playlists and single video URLs/IDs in one go.
-   **Video Archiving:** Download videos, thumbnails, subtitles, and `.info.json` metadata files.
-   **Cookie Support:** Use browser cookies to download age-restricted, private, or members-only videos.
-   **High-Quality Downloads:** Automatically selects the best video and audio formats and merges them for resolutions like 1080p and higher.
-   **Multi-Format Reporting:**
    -   **Excel (`.xlsx`):** A spreadsheet with video details and embedded thumbnails.
    -   **HTML (`.html`):** A modern, interactive, and searchable local webpage with links.
    -   **PDF (`.pdf`):** A clean, portable summary of all processed videos, featuring Unicode-compatible fonts for full character support.
-   **Efficient:** Downloads all thumbnails concurrently to speed up the process.
-   **Highly Configurable:** Easily manage all settings from a single `config.ini` file.

## Requirements & Setup

Follow these steps to set up the project.

### 1. Install FFmpeg

This is a **critical dependency** for downloading high-quality video. The executable **must** be placed in the project's root folder.

1.  Go to the official FFmpeg Builds page: [ffmpeg.org/download.html](https://ffmpeg.org/download.html). The "gyan.dev" or "BtbN" builds are excellent choices.
2.  Download the latest release for your operating system (e.g., Windows, macOS, Linux).
3.  Unzip the downloaded archive.
4.  Find the main executable file inside the `bin` folder (it will be `ffmpeg.exe` on Windows, or just `ffmpeg` on macOS/Linux).
5.  **Copy that single executable file** into the root of your YT-Ledger project folder, right next to `main.py`.

### 2. Get the Fonts for PDF Reports

The project uses the DejaVu font family for its excellent Unicode support in PDF reports. For your convenience, the required font files are included in the `fonts` folder of this repository.

### 3. Clone the Project & Set Up the Environment

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/nathanfx330/YT-Ledger.git
    cd YT-Ledger
    ```

2.  **Set up the Python Environment (choose one method):**

    **A) Using `pip` and `venv` :**
    ```bash
    # Create and activate a virtual environment
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate

    # Install the locked package versions
    pip install -r requirements.txt
    ```

    **B) Using `Conda` (Recommended) :**
    ```bash
    # Create and activate the conda environment from the provided file
    conda env create -f environment.yml
    conda activate yt-ledger
    ```

### 4. Prepare the Configuration File
[youtube]
# The ID(s) or URL(s) of the playlist(s) and/or single video(s) you want to process.
# - To process multiple items, separate them with a plus sign (+).
# - You can mix and match raw IDs and full URLs.
#
# Example (single playlist ID): Lf2t3vRE19kfYXaMtwdYwy_xaNTg0Vabn
# Example (single video URL): https://www.youtube.com/watch?v=dZz8zegXcQ
# Example (mixed): PLf2t3vRE19kfYXaMtwdYwy_xaNTg0Vabn+dQw4w9WgXcQ+https://youtube.com/playlist?list=PL...
playlist_id = 

# An optional title for the HTML report. If left blank, a default will be used.
report_title =

[downloads]
# Set this to true to download all videos and create .info.json files.
# Set to false to fetch metadata only for a quick report.
download_videos = true

# The folder where your videos will be saved.
video_folder = ./videos

# Example (enabled): archive_file = ./download_archive.txt
# Example (disabled): archive_file =
archive_file =

# (Optional) Path to a cookies file to bypass bot detection or download private/age-restricted videos.
# Export this from your browser using an extension like "Get cookies.txt".
# Leave blank to disable. IE ./cookies.txt
cookies_file = 
# Set your desired maximum resolution (e.g., 1080, 720, 480).
preferred_resolution = 1080

# --- FFmpeg Location (Choose ONE method) ---
# This setting tells the script where to find the FFmpeg executable.

# Method 1: FFmpeg is already installed on your system (Common on Linux/macOS).
#   - To find the path, open your terminal and run: which ffmpeg
#   - Paste the output here.
#   - If the command works, you can often just leave this setting BLANK, and yt-dlp will find it automatically.
#
# Example for Linux:
# ffmpeg_location = /usr/bin/ffmpeg

# Method 2: Use a portable FFmpeg (Recommended for Windows).
#   - Place ffmpeg.exe (Windows) or ffmpeg (macOS/Linux) in this project's main folder.
#   - Use the path below that matches your operating system.
ffmpeg_location = ./ffmpeg.exe
#
# For macOS or Linux:
# ffmpeg_location = ./ffmpeg

[outputs]
# --- Report Filename Settings ---
output_file_xls = YouTube_Archive_Report.xlsx
output_file_html = YouTube_Archive_Report.html
template_file_html = template.html
output_file_pdf = YouTube_Archive_Report.pdf

thumbs_folder = ./thumbs

# Set to 'false' to hide the "Generated by..." text in the PDF footer.
show_footer_watermark = true




### License

This project is licensed under the MIT License. See the LICENSE file for the full text.
Copyright (c) 2025 Nathaniel Westveer
Acknowledgements

    The incredible team behind yt-dlp for creating such a powerful and versatile tool.

    This project includes the DejaVu Fonts, which are distributed under their own permissive license. The full license text is available in the fonts/dejavu-fonts LICENSE.txt file.
