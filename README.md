# YT-Ledger: YouTube Archival & Reporting Pipeline

![YT-Ledger Demo](https://i.imgur.com/your-demo-image.gif) <!-- Optional: Create a gif/image of your script running and reports being generated -->

YT-Ledger is a powerful Python script that uses `yt-dlp` to create a comprehensive archival pipeline for YouTube playlists and individual videos. It fetches detailed metadata, optionally downloads the videos and subtitles, and generates professional, easy-to-read reports in **XLSX**, **HTML**, and **PDF** formats.

## Key Features

-   **Batch Processing:** Process multiple YouTube playlists and single video URLs/IDs in one go.
-   **Video Archiving:** Download videos, thumbnails, subtitles, and `.info.json` metadata files.
-   **High-Quality Downloads:** Automatically selects the best video and audio formats and merges them for resolutions like 1080p and higher.
-   **Multi-Format Reporting:**
    -   **Excel (`.xlsx`):** A spreadsheet with video details and embedded thumbnails.
    -   **HTML (`.html`):** A modern, interactive, and searchable local webpage with links.
    -   **PDF (`.pdf`):** A clean, portable summary of all processed videos, perfect for sharing.
-   **Efficient:** Downloads all thumbnails concurrently to speed up the process.
-   **Highly Configurable:** Easily manage all settings from a single `config.ini` file.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1.  **Python** (version 3.8 or newer is recommended).
2.  **FFmpeg**: This is a **critical dependency**. `yt-dlp` requires FFmpeg to merge the separate video and audio streams that YouTube provides for high-quality downloads (1080p and above).
    -   **Official Website:** [ffmpeg.org](https://ffmpeg.org/download.html)
    -   **Installation Guides:** A helpful guide for Windows, macOS, and Linux can be found [here](https://phoenixnap.com/kb/install-ffmpeg-windows).
    -   The easiest way to use it is to place the `ffmpeg` (or `ffmpeg.exe` on Windows) executable in the same directory as the script, or add it to your system's PATH.

## Installation

Follow these steps to set up the project on your local machine.

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/yt-ledger.git
    cd yt-ledger
    ```

2.  **Set up the Python Environment:**

    Choose one of the two methods below. Using a virtual environment is highly recommended.

    **A) Using `pip` and `venv` (Recommended):**
    ```bash
    # Create and activate a virtual environment
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate

    # Install the required Python packages
    pip install -r requirements.txt
    ```

    **B) Using `Conda`:**
    ```bash
    # Create and activate the conda environment from the provided file
    conda env create -f environment.yml
    conda activate yt-ledger
    ```

3.  **Prepare the Configuration File:**

    The script is controlled by a `config.ini` file. A template is provided.
    ```bash
    # Copy the template to create your own personal config file
    cp config.template.ini config.ini
    ```
    **Note:** The `config.ini` file is intentionally ignored by Git to prevent you from accidentally sharing your personal playlist IDs or settings.

## Usage

1.  **Customize `config.ini`**:
    Open `config.ini` with a text editor and fill in the details. See the **Configuration** section below for a full explanation of all available options. At a minimum, you must provide a `playlist_id`.

2.  **Run the Script:**
    Once your environment is activated and your configuration is set, run the main script from your terminal:
    ```bash
    python main.py
    ```
    The script will log its progress to both the console and the `yt_ledger.log` file.

## Configuration (`config.ini`)

All settings are managed in `config.ini`.

| Section       | Setting                 | Description                                                                                                                              |
| :------------ | :---------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| `[youtube]`   | `playlist_id`           | **Required.** A `+` separated list of YouTube playlist IDs, video IDs, or full URLs.                                                     |
| `[youtube]`   | `report_title`          | An optional title for your reports. If left blank, a default title with the current date is used.                                        |
| `[downloads]` | `download_videos`       | Set to `true` to download videos or `false` to only fetch metadata for reports.                                                          |
| `[downloads]` | `video_folder`          | The directory where videos and their metadata will be saved.                                                                             |
| `[downloads]` | `archive_file`          | Path to a `.txt` file used to track and skip already downloaded videos. Leave blank to disable this feature.                             |
| `[downloads]` | `preferred_resolution`  | The maximum video resolution to download (e.g., 1080, 720).                                                                              |
| `[downloads]` | `ffmpeg_location`       | Optional. Full path to your `ffmpeg` executable. **Leave blank if FFmpeg is in the script's folder or in your system's PATH.**           |
| `[outputs]`   | `output_file_xls`       | Filename for the generated Excel report.                                                                                                 |
| `[outputs]`   | `output_file_html`      | Filename for the generated HTML report.                                                                                                  |
| `[outputs]`   | `output_file_pdf`       | Filename for the generated PDF report.                                                                                                   |
| `[outputs]`   | `thumbs_folder`         | The directory where video thumbnails will be saved.                                                                                      |
| `[outputs]`   | `show_footer_watermark` | Set to `false` to hide the "Generated by..." text in the PDF footer for a cleaner look.                                                    |

## License

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
## Acknowledgements

-   The incredible team behind [yt-dlp](https://github.com/yt-dlp/yt-dlp) for creating such a powerful and versatile tool.
-   The developers of the Python libraries used in this project.
