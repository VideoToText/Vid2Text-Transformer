import time
from pytube import YouTube


def vid_download(gui, url, folder):
    """
    Download YouTube Video To Folder, resources
    """
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=False)
    gui.progress['value'] = 5
    time.sleep(2)
    gui.statusmsg.set(f'Downloading YouTube video')
    yt.streams.get_highest_resolution().download(folder)
    gui.progress['value'] = 10
    time.sleep(2)
    gui.statusmsg.set(f'YouTube video download completed')
    gui.progress['value'] = 15
    time.sleep(2)
