# report_html.py

from pathlib import Path
from urllib.parse import quote
from datetime import datetime
import logging

def create_html_report(video_list, thumb_map, report_title, project_name, template_path, output_filename):
    """Generates the final HTML report."""
    if not video_list:
        logging.info("No video data to generate HTML report.")
        return
    logging.info("\nBuilding HTML report...")
    try:
        template_content = template_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        logging.critical(f"CRITICAL ERROR: Template '{template_path}' not found.")
        return

    video_rows_html = ""
    # The base directory for creating relative paths is the parent of the HTML output file
    html_base_dir = output_filename.parent

    for video_data in video_list:
        video_id = video_data.get('id')
        video_title = video_data.get('title', 'N/A')
        channel_name = video_data.get('channel', 'N/A')
        youtube_url = f"https://www.youtube.com/watch?v={video_id}"

        thumb_src = ""
        if video_id in thumb_map:
            try:
                # Create a path for the thumbnail relative to the HTML file's location
                relative_thumb_path = thumb_map[video_id].relative_to(html_base_dir)
                thumb_src = quote(relative_thumb_path.as_posix())
            except ValueError:
                # Fallback if the path cannot be made relative (e.g., different drive on Windows)
                thumb_src = quote(thumb_map[video_id].as_uri())

        video_path = video_data.get('video_path')
        if video_path and video_path.name != "Not Downloaded":
            # --- THIS IS THE FIX ---
            # Create a relative path from the HTML file to the video file.
            # Then, URL-encode it to handle spaces and special characters safely.
            try:
                relative_video_path = video_path.relative_to(html_base_dir)
                local_file_href = quote(relative_video_path.as_posix())
            except ValueError:
                # Fallback to absolute URI if a relative path can't be made
                local_file_href = video_path.as_uri()
            
            local_file_html = f'<td><a class="local-file-link" href="{local_file_href}" target="_blank">Watch Local File</a></td>'
        else:
            local_file_html = '<td>Not Downloaded</td>'

        # --- UPDATED HTML ROW ---
        video_rows_html += f"""
        <tr>
            <td><a href="{youtube_url}" target="_blank"><img src="{thumb_src}" alt="Thumbnail for {video_title}"></a></td>
            <td class="video-title">{video_title}</td>
            <td class="channel-name">{channel_name}</td>
            <td>{video_data.get('upload_date', 'N/A')}</td>
            <td class="full-url-col"><a href="{youtube_url}" target="_blank">{youtube_url}</a></td>
            {local_file_html}
        </tr>"""

    generation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    footer_html = f"Generated by {project_name} on {generation_date}"
    final_html = template_content.replace('<!--REPORT_TITLE_PLACEHOLDER-->', report_title)
    final_html = final_html.replace('<!--VIDEO_ROWS_PLACEHOLDER-->', video_rows_html)
    final_html = final_html.replace('<!--FOOTER_PLACEHOLDER-->', footer_html)

    try:
        output_filename.write_text(final_html, encoding='utf-8')
        logging.info(f"✅ Success! HTML report saved as '{output_filename}'")
    except Exception as e:
        logging.error(f"❌ Error saving HTML file: {e}")
