import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog as fd
from tkinter import ttk
from threading import Thread

from src.file_refactoring import delete_legacy_files
from src.script_to_text import vtt_to_string
from src.vid_downloader import vid_download, thumbnail_download, get_video_title, is_valid_video, script_download
from src.text_extractor import extract_text_from_video
from src.gpt_processor import process_video_contents_with_gpt, setup_gpt
from src.pdf_generator import generate_pdf_from_text

VER = 'v0.1'

current_dir = os.path.dirname(os.path.abspath(__file__))
resource_dir = os.path.join(os.path.abspath(os.path.join(current_dir, os.pardir)), "resources")


class VidToPdf:
    def __init__(self):
        self.flag = True
        self.video_title = 'vid2pdf'
        self.saveto = ''

        self.root = tk.Tk()
        self.root.iconbitmap(os.path.join(resource_dir, 'vid2pdf_favicon.ico'))
        self.root.title(f'Youtube Video Converter - VID2PDF {VER}')
        self.root.resizable(width=False, height=False)

        self.statusmsg = tk.StringVar()
        self.statusmsg.set('Waiting')
        self.vtitlemsg = tk.StringVar()
        self.vtitlemsg.set(self.video_title)

        self.logo_panel = None

        # 병합된 create_widgets 함수의 내용
        content = ttk.Frame(self.root, padding=10)
        content.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        self.logo_panel = ttk.Frame(content)
        url_panel = ttk.Frame(content, relief='groove', padding=(6, 6, 6, 6))
        status_panel = ttk.Frame(content, relief='groove', padding=(6, 6, 10, 10))
        progress_panel = ttk.Frame(content, relief='groove', padding=(6, 6, 6, 6))

        self.logo_panel.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        url_panel.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        status_panel.grid(column=0, row=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        progress_panel.grid(column=0, row=3, sticky=(tk.N, tk.W, tk.E, tk.S))

        try:
            self.vid_to_pdf_logo = ImageTk.PhotoImage(Image.open(
                os.path.join(resource_dir, 'vid2pdf_logo_img.jpg')))
            logo_label = ttk.Label(self.logo_panel, image=self.vid_to_pdf_logo)
            logo_label.image = self.vid_to_pdf_logo
            logo_label.grid(row=0, column=1, pady=10, sticky="n")
            self.logo_panel.grid_columnconfigure(0, weight=1)
            self.logo_panel.grid_columnconfigure(2, weight=1)

        except Exception as e:
            print(e)

        url_label = ttk.Label(url_panel, text='Youtube video URL:  ', anchor=tk.W)
        saveto_label = ttk.Label(url_panel, text='Save PDF to:  ', anchor=tk.W)
        self.urlentry = ttk.Entry(url_panel, width=55)
        self.savetoentry = ttk.Entry(url_panel, width=55)
        self.set_button = ttk.Button(url_panel, text="Set", command=self.set)
        self.folder_button = ttk.Button(url_panel, text="Folder", command=self.folder)

        url_label.grid(row=0, column=0, sticky=tk.W)
        self.urlentry.grid(row=0, column=1, columnspan=2, pady=10, sticky=tk.W)
        self.set_button.grid(row=0, column=3, sticky=tk.W, padx=(5, 0))
        saveto_label.grid(row=1, column=0, sticky=tk.W)
        self.savetoentry.grid(row=1, column=1, sticky=tk.W)
        self.folder_button.grid(row=1, column=3, sticky=tk.W, padx=(5, 0))

        vtitle_label = ttk.Label(status_panel, text='Video Title:   ', anchor=tk.W)
        status_label = ttk.Label(status_panel, text='Status :   ', anchor=tk.W)
        self.vtitle = ttk.Label(status_panel, textvariable=self.vtitlemsg, anchor=tk.W)
        self.status = ttk.Label(status_panel, textvariable=self.statusmsg, anchor=tk.W)

        vtitle_label.grid(row=0, column=0, padx=5, pady=10, sticky=tk.W)
        self.vtitle.grid(row=0, column=1, sticky=tk.W)
        status_label.grid(row=1, column=0, padx=5, sticky=tk.W)
        self.status.grid(row=1, column=1, sticky=tk.W)

        progress_label = ttk.Label(progress_panel, text='Progress:   ', anchor=tk.W)
        self.progress = ttk.Progressbar(progress_panel, orient=tk.HORIZONTAL, length=330, mode='determinate')
        self.start_button = ttk.Button(progress_panel, text="Start", command=self.start)

        progress_label.grid(row=0, column=0, sticky=tk.W)
        self.progress.grid(row=0, column=1, sticky=tk.W)
        self.start_button.grid(row=0, column=2, padx=45, sticky=tk.W)

        self.root.mainloop()

    def folder(self, *args):
        self.saveto = fd.askdirectory()
        if self.saveto == '':
            return

        self.savetoentry.delete(0, tk.END)
        self.savetoentry.insert(0, self.saveto)

    def start(self, *args):
        Thread(target=self.process_video).start()

    def process_video(self):
        url = self.urlentry.get()
        folder = self.savetoentry.get()
        if url == '':
            self.root.after(0, self.update_status, 'Enter Youtube URL for converting Video', 'red')
            return
        elif folder == '':
            self.root.after(0, self.update_status, 'Enter file location to save your PDF', 'red')
            return
        else:
            setup_gpt()

            self.set_button.config(state="disabled")
            self.folder_button.config(state="disabled")
            self.start_button.config(state="disabled")

            # Download video
            video_path = os.path.join(resource_dir, "video.mp4")
            vid_download(self, url, resource_dir)

            # Script download
            script_download(self, url, resource_dir)
            script_path = os.path.join(resource_dir, "script.en.vtt")
            script_text = vtt_to_string(self, script_path)

            # OCR Script Generate
            video_text = extract_text_from_video(self, video_path)

            structured_output = process_video_contents_with_gpt(self, script_text, video_text)
            generate_pdf_from_text(self, structured_output, "output.pdf")
            delete_legacy_files()

    def set(self, *args):
        url = self.urlentry.get()
        folder = self.savetoentry.get()
        if url == '':
            self.root.after(0, self.update_status, 'Enter Youtube URL for converting Video', 'red')
            return

        if not is_valid_video(url):
            self.video_title = "vid2pdf"
            self.vtitlemsg.set(self.video_title)
            self.root.after(0, self.update_status, 'Video Not Found', 'red')
            self.root.after(0, self.update_status, 'Youtube URL is not valid', 'red')
            logo_label = self.logo_panel.winfo_children()[0]
            logo_label.configure(image=self.vid_to_pdf_logo)
            logo_label.image = self.vid_to_pdf_logo
            logo_label.grid(row=0, column=1, pady=10)
            return

        self.video_title = get_video_title(url)
        self.vtitlemsg.set(self.video_title)

        # Download the thumbnail image and set paths
        thumbnail_download(url, resource_dir)
        thumbnail_filename = "thumbnail.webp"
        thumbnail_path = os.path.join(resource_dir, thumbnail_filename)

        img = Image.open(thumbnail_path)
        img = img.resize((625, 306), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        logo_label = self.logo_panel.winfo_children()[0]
        logo_label.configure(image=img_tk)
        logo_label.image = img_tk
        logo_label.grid(row=0, column=1, pady=10)
        self.logo_panel.grid_columnconfigure(0, weight=1)
        self.logo_panel.grid_rowconfigure(0, weight=1)

        self.video_title = get_video_title(url)
        self.vtitlemsg.set(self.video_title)
        if folder == '':
            self.root.after(0, self.update_status, 'Select Directory to Save PDF', 'black')
        else:
            self.root.after(0, self.update_status, 'Press Start Button to Convert', 'black')


    def update_status(self, msg, color):
        self.statusmsg.set(msg)
        self.status.config(foreground=color)


if __name__ == '__main__':
    obj = VidToPdf()
    obj.root.mainloop()


