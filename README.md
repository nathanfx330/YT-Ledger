YT-Ledger: YouTube Archival & Reporting Pipeline

YT-Ledger is a powerful Python script that uses yt-dlp to create a comprehensive archival pipeline for YouTube playlists and individual videos. It fetches detailed metadata, optionally downloads videos and subtitles, and generates professional, easy-to-read reports in XLSX, HTML, and PDF formats.

🔑 Key Features

Batch Processing: Process multiple YouTube playlists and single video URLs/IDs in one go.

Video Archiving: Download videos, thumbnails, subtitles, and .info.json metadata files.

Cookie Support: Use browser cookies to download age-restricted, private, or members-only videos.

High-Quality Downloads: Automatically selects the best video/audio formats and merges them (e.g., for 1080p).

Multi-Format Reporting:

Excel (.xlsx): Spreadsheet with video metadata and embedded thumbnails.

HTML (.html): Interactive, searchable local webpage with video links.

PDF (.pdf): Portable, clean summary report with full Unicode support.

Efficient: Concurrent thumbnail downloads improve performance.

Highly Configurable: Controlled entirely through a single config.ini file.

⚙️ Requirements & Setup

1. Install FFmpeg

This is a critical dependency for downloading high-quality video/audio.

Download FFmpeg from: ffmpeg.org/download.html(Recommended: gyan.dev builds or BtbN builds)

Extract the downloaded archive.

Find the ffmpeg executable in the bin folder.

Copy it to the root of your YT-Ledger folder (same level as main.py):

ffmpeg.exe on Windows

ffmpeg on macOS/Linux

2. Get the Fonts for PDF Reports

The PDF generator uses DejaVu fonts for full Unicode compatibility. Font files are already included in the fonts/ directory.

3. Clone the Project & Set Up Environment

Clone the Repo:

git clone https://github.com/nathanfx330/YT-Ledger.git
cd YT-Ledger

Set Up Python Environment

Choose one of the following:

A) Using pip + venv:

python -m venv venv
# Activate the virtual environment
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt

B) Using Conda (Recommended):

conda env create -f environment.yml
conda activate yt-ledger

🛠️ Configuration

4. Create Your config.ini File

cp config.template.ini config.ini

Edit config.ini in your preferred text editor. At a minimum, set:

playlist_id under [youtube]

ffmpeg_location under [downloads]

For age-restricted/private content, provide your cookies.txt path under cookies_file.

🚀 Usage

Once your environment is activated and configuration is ready, run the script:

python main.py

Progress is logged to both the console and yt_ledger.log.

📄 Configuration Reference (config.ini)

Section

Setting

Description

[youtube]

playlist_id

Required. A + separated list of playlist IDs, video IDs, or URLs.



report_title

Optional title for reports. If blank, uses the current date.

[downloads]

download_videos

true to download videos; false for metadata-only reports.



video_folder

Folder to save videos and metadata.



archive_file

Path to a .txt file for download history (leave blank to disable).



cookies_file

Optional path to cookies.txt for private/age-restricted access.



preferred_resolution

Max resolution to download (e.g., 1080).



ffmpeg_location

Path to FFmpeg executable (e.g., ./ffmpeg.exe or ./ffmpeg).

[outputs]

output_file_xls

Filename for Excel report.



output_file_html

Filename for HTML report.



output_file_pdf

Filename for PDF report.



thumbs_folder

Folder to store downloaded thumbnails.



show_footer_watermark

Set to false to remove the footer watermark from PDF.

📜 License

This project is licensed under the MIT License.See the LICENSE file for full terms.

🙏 Acknowledgements

Huge thanks to the yt-dlp team for their outstanding work.

This project includes DejaVu Fonts, distributed under a permissive license (see fonts/dejavu-fonts/LICENSE.txt).

Let me know if you'd like a short badge section, project logo, or automated deployment instructions added.
