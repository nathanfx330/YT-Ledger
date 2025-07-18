# YT-Ledger: YouTube Archival & Reporting Pipeline

YT-Ledger is a powerful Python script that uses `yt-dlp` to create a comprehensive archival pipeline for YouTube playlists and individual videos. It fetches detailed metadata, optionally downloads the videos and subtitles, and generates professional, easy-to-read reports in **XLSX**, **HTML**, and **PDF** formats.

## Key Features

-   **Batch Processing:** Process multiple YouTube playlists and single video URLs/IDs in one go.
-   **Video Archiving:** Download videos, thumbnails, subtitles, and `.info.json` metadata files.
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
    cd yt-ledger
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

The script is controlled by a `config.ini` file. A template is provided.

```bash
# Copy the template to create your own personal config file
cp config.template.ini config.ini```
**Note:** `config.ini` is intentionally ignored by Git to prevent you from accidentally sharing your personal playlist IDs or settings.

## Usage

1.  **Customize `config.ini`**:
    Open `config.ini` with a text editor. At a minimum, you must provide a `playlist_id` and ensure the `ffmpeg_location` points to the executable you placed in the root folder.

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
| `[downloads]` | `ffmpeg_location`       | Path to the FFmpeg executable in the project root. **Must be set correctly for your OS** (e.g., `./ffmpeg.exe` for Windows, `./ffmpeg` for macOS/Linux). |
| `[outputs]`   | `output_file_xls`       | Filename for the generated Excel report.                                                                                                 |
| `[outputs]`   | `output_file_html`      | Filename for the generated HTML report.                                                                                                  |
| `[outputs]`   | `output_file_pdf`       | Filename for the generated PDF report.                                                                                                   |
| `[outputs]`   | `thumbs_folder`         | The directory where video thumbnails will be saved.                                                                                      |
| `[outputs]`   | `show_footer_watermark` | Set to `false` to hide the "Generated by..." text in the PDF footer for a cleaner look.                                                    |

## License

This project is licensed under the MIT License. See the `LICENSE` file for the full text.

Copyright (c) 2025 Nathaniel Westveer

## Acknowledgements

-   The incredible team behind [yt-dlp](https://github.com/yt-dlp/yt-dlp) for creating such a powerful and versatile tool.
-   This project includes the **DejaVu Fonts**, which are distributed under their own permissive license. The full license text is available in the `fonts/FONTS_LICENSE.txt` file.
