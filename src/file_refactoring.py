import os


def delete_legacy_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    resource_dir = os.path.join(os.path.abspath(os.path.join(current_dir, os.pardir)), "resources")
    os.remove(os.path.join(resource_dir, "thumbnail.webp"))
    os.remove(os.path.join(resource_dir, "script.vtt"))
    os.remove(os.path.join(resource_dir, "video.mp4"))

