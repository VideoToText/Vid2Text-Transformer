import os
from pytube import YouTube
import moviepy.editor as mp


def vid_download(gui, url, folder):
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=False)
    gui.statusmsg.set(f'Downloading YouTube audio')
    audio_file_path = yt.streams.filter(only_audio=True).first().download(folder)
    audio_name = os.path.splitext(audio_file_path)[0] + '.mp3'
    mp.AudioFileClip(audio_file_path).write_audiofile(audio_name)
    os.remove(audio_file_path)
    gui.progress['value'] = 15
    gui.statusmsg.set(f'Downloading YouTube video')
    yt.streams.get_highest_resolution().download(folder)
    gui.statusmsg.set(f'YouTube audio & video download completed')
    gui.progress['value'] = 30
