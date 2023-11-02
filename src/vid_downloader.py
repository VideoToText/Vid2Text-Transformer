import time
from pytube import YouTube


def vid_download(gui, url, folder):
    gui.statusmsg.set('Preparing to download YouTube video')
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=False)
    num_streams = len(yt.streams)

    for idx, stream in enumerate(yt.streams, 1):
        for _ in range(3):
            vd_progress = idx / num_streams
            gui.statusmsg.set(f'Downloading YouTube video: {round(vd_progress * 100)}% completed.')
            time.sleep(0.5)
            gui.progress['value'] = vd_progress * 30
            gui.root.update_idletasks()
        print(stream)

    yt.streams.get_highest_resolution().download(folder)

    video_filter = yt.streams.filter(mime_type="video/mp4", res="720p", progressive=True)

    for stream in video_filter:
        print(stream)