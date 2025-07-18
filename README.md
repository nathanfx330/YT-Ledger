# YT-Ledger: YouTube Archival & Reporting Pipeline

**YT-Ledger** is a powerful Python script that uses [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) to create a comprehensive archival pipeline for YouTube playlists and individual videos. It fetches detailed metadata, optionally downloads videos and subtitles, and generates professional, easy-to-read reports in **XLSX**, **HTML**, and **PDF** formats.

---

## 🔑 Key Features

- **Batch Processing**: Process multiple YouTube playlists and individual video URLs/IDs in one go.
- **Video Archiving**: Download videos, thumbnails, subtitles, and `.info.json` metadata files.
- **Cookie Support**: Use browser cookies to access age-restricted, private, or members-only videos.
- **High-Quality Downloads**: Automatically selects and merges the best video/audio formats (e.g., 1080p).
- **Multi-Format Reporting**:
  - **Excel (`.xlsx`)**: Spreadsheet with metadata and embedded thumbnails.
  - **HTML (`.html`)**: Searchable local webpage with clickable links.
  - **PDF (`.pdf`)**: Clean, portable summary report with Unicode font support.
- **Efficient**: Concurrent thumbnail downloading improves performance.
- **Configurable**: Fully managed via a single `config.ini` file.

---

## ⚙️ Requirements & Setup

### 1. Install FFmpeg

This is a **critical dependency** for downloading high-quality video/audio.

1. Download FFmpeg from: [ffmpeg.org/download.html](https://ffmpeg.org/download.html)  
   (Recommended: [gyan.dev builds](https://www.gyan.dev/ffmpeg/builds/) or [BtbN builds](https://github.com/BtbN/FFmpeg-Builds))
2. Extract the downloaded archive.
3. Find the `ffmpeg` executable in the `bin` folder.
4. **Copy** it to the root of your YT-Ledger folder (same level as `main.py`):  
   - `ffmpeg.exe` on Windows  
   - `ffmpeg` on macOS/Linux

### 2. Get the Fonts for PDF Reports

The PDF generator uses **DejaVu fonts** for full Unicode compatibility. Fonts are pre-included in the `fonts/` directory.

### 3. Clone the Project & Set Up Environment

#### Clone the Repo

```bash
git clone https://github.com/nathanfx330/YT-Ledger.git
cd YT-Ledger
```

#### Set Up Python Environment

Choose **one** of the following:

**A) Using `venv` + `pip`:**

```bash
python -m venv venv
# Activate the virtual environment
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

**B) Using Conda (Recommended):**

```bash
conda env create -f environment.yml
conda activate yt-ledger
```

---

## 🛠️ Configuration

### 4. Create Your `config.ini` File

```bash
 config.ini
```

Edit `config.ini` in your preferred text editor. At a minimum, set:

- `playlist_id` under `[youtube]`
- `ffmpeg_location` under `[downloads]`

For age-restricted/private content, provide your `cookies.txt` path under `cookies_file`.

---

## 🚀 Usage

Once your environment is activated and configuration is ready, run the script:

```bash
python main.py
```

Progress is logged to both the console and `yt_ledger.log`.

---

## 📄 Configuration Reference (`config.ini`)

| Section       | Setting                 | Description                                                          |
| ------------- | ----------------------- | -------------------------------------------------------------------- |
| `[youtube]`   | `playlist_id`           | Required. A `+` separated list of playlist IDs, video IDs, or URLs.  |
|               | `report_title`          | Optional title for reports. If blank, uses the current date.         |
| `[downloads]` | `download_videos`       | `true` to download videos; `false` for metadata-only reports.        |
|               | `video_folder`          | Folder to save videos and metadata.                                  |
|               | `archive_file`          | Path to a `.txt` file for download history (leave blank to disable). |
|               | `cookies_file`          | Optional path to `cookies.txt` for private/age-restricted access.    |
|               | `preferred_resolution`  | Max resolution to download (e.g., 1080).                             |
|               | `ffmpeg_location`       | Path to FFmpeg executable (e.g., `./ffmpeg.exe` or `./ffmpeg`).      |
| `[outputs]`   | `output_file_xls`       | Filename for Excel report.                                           |
|               | `output_file_html`      | Filename for HTML report.                                            |
|               | `output_file_pdf`       | Filename for PDF report.                                             |
|               | `thumbs_folder`         | Folder to store downloaded thumbnails.                               |
|               | `show_footer_watermark` | Set to `false` to remove the footer watermark from PDF.              |

---

## 📜 License
MIT License

Copyright (c) 2025 Nathaniel Westveer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


The incredible team behind yt-dlp for creating such a powerful and versatile tool.
This project includes the DejaVu Fonts, which are distributed under their own permissive license. The full license text is available in the fonts/dejavu-fonts LICENSE.txt file.
