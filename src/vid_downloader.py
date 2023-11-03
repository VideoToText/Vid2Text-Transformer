import json
import time
import yt_dlp


def get_video_info(url):
    ydl_opts = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        return json.dumps(ydl.sanitize_info(info), ensure_ascii=False)


def get_video_title(url):
    video_info = json.loads(get_video_info(url))
    video_title = video_info.get('title', None)
    if len(video_title) < 73:
        return video_title
    else:
        return video_title[:70] + '..'


def is_valid_video(url):
    ydl_opts = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return True
        except yt_dlp.utils.DownloadError:
            return False


def thumbnail_download(url, folder):
    ydl_opts = {
        'skip_download': True,
        'outtmpl': f"{folder}/thumbnail.webp",
        'writethumbnail': True,
    }

    try:
        yt_dlp.YoutubeDL(ydl_opts).download([url])
    except yt_dlp.utils.DownloadError as e:
        return f'Error: {e}'


def vid_download(gui, url, folder):
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': f"{folder}/video.mp4",
        'merge_output_format': 'mp4'
    }
    gui.progress['value'] = 10
    gui.root.after(0, gui.update_status, 'Downloading video...', 'black')
    try:
        yt_dlp.YoutubeDL(ydl_opts).download([url])
        gui.progress['value'] = 20
        gui.root.after(0, gui.update_status, 'Downloading video... Complete', 'black')
        time.sleep(1)
    except yt_dlp.utils.DownloadError as e:
        return f'Error: {e}'


def script_download(gui, url, folder):
    ydl_opts = {
        'skip_download': True,
        'outtmpl': f"{folder}/script.%(ext)s",
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['ko'],
        'subtitlesformat': 'vtt'
    }
    gui.progress['value'] = 30
    gui.root.after(0, gui.update_status, 'Downloading Script...', 'black')
    try:
        yt_dlp.YoutubeDL(ydl_opts).download([url])
        gui.progress['value'] = 40
        gui.root.after(0, gui.update_status, 'Downloading Script... Complete', 'black')
        time.sleep(1)
    except yt_dlp.utils.DownloadError as e:
        return f'Error: {e}'
