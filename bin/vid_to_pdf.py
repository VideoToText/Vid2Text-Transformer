import os
import re
import requests
import tkinter as tk
from io import BytesIO
from bs4 import BeautifulSoup
from PIL import ImageTk, Image
from tkinter import filedialog as fd
from tkinter import ttk
from src.main import main as video_to_pdf_main
# from threading import Thread
# from downloader import download

__author__ = "sonjh.dev@gmail.com"
VER = 'v0.1'

current_dir = os.path.dirname(os.path.abspath(__file__))
resource_dir = os.path.abspath(os.path.join(current_dir, os.pardir))


class VidToPdf:
    def __init__(self):
        self.flag = True
        self.saveto = ''

        self.root = tk.Tk()
        self.root.iconbitmap(os.path.join(resource_dir, 'resources/vid2pdf_favicon.ico'))
        self.root.title(f'Youtube Video Converter - VID2PDF {VER}')
        self.root.resizable(width=False, height=False)

        self.statusmsg = tk.StringVar()
        self.statusmsg.set('Waiting...')
        self.vtitlemsg = tk.StringVar()
        self.vtitlemsg.set('vid2pdf')

        self.logo_panel = None
        self.create_widgets()

    def create_widgets(self):
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
            vid_to_pdf_logo = ImageTk.PhotoImage(Image.open(
                os.path.join(resource_dir, 'resources/vid2pdf_logo_img.jpg')))
            logo_label = ttk.Label(self.logo_panel, image=vid_to_pdf_logo)
            logo_label.image = vid_to_pdf_logo
            logo_label.grid(row=0, column=1, pady=10, sticky="n")
            self.logo_panel.grid_columnconfigure(0, weight=1)
            self.logo_panel.grid_columnconfigure(2, weight=1)

        except Exception as e:
            print(e)

        url_label = ttk.Label(url_panel, text='Youtube video URL:  ', anchor=tk.W)
        saveto_label = ttk.Label(url_panel, text='Save PDF to:  ', anchor=tk.W)
        self.urlentry = ttk.Entry(url_panel, width=55)
        self.savetoentry = ttk.Entry(url_panel, width=55)
        set_button = ttk.Button(url_panel, text="Set", command=self.set)
        folder_button = ttk.Button(url_panel, text="Folder", command=self.folder)

        url_label.grid(row=0, column=0, sticky=tk.W)
        self.urlentry.grid(row=0, column=1, columnspan=2, pady=10, sticky=tk.W)
        set_button.grid(row=0, column=3, sticky=tk.W, padx=(5, 0))
        saveto_label.grid(row=1, column=0, sticky=tk.W)
        self.savetoentry.grid(row=1, column=1, sticky=tk.W)
        folder_button.grid(row=1, column=3, sticky=tk.W, padx=(5, 0))

        vtitle_label = ttk.Label(status_panel, text='Video Title:   ', anchor=tk.W)
        status_label = ttk.Label(status_panel, text='Status :   ', anchor=tk.W)
        self.vtitle = ttk.Label(status_panel, textvariable=self.vtitlemsg, anchor=tk.W)
        self.status = ttk.Label(status_panel, textvariable=self.statusmsg, anchor=tk.W)

        vtitle_label.grid(row=0, column=0, padx=5, pady=10, sticky=tk.W)
        self.vtitle.grid(row=0, column=1, sticky=tk.W)
        status_label.grid(row=1, column=0, padx=5, sticky=tk.W)
        self.status.grid(row=1, column=1, sticky=tk.W)

        progress_label = ttk.Label(progress_panel, text='Progress:   ', anchor=tk.W)
        progress = ttk.Progressbar(progress_panel, orient=tk.HORIZONTAL, length=330, mode='determinate')
        start_button = ttk.Button(progress_panel, text="Start", command=self.start)

        progress_label.grid(row=0, column=0, sticky=tk.W)
        progress.grid(row=0, column=1, sticky=tk.W)
        start_button.grid(row=0, column=2, padx=45, sticky=tk.W)

    def folder(self):
        self.saveto = fd.askdirectory()
        if self.saveto == '':
            return

        self.savetoentry.delete(0, tk.END)
        self.savetoentry.insert(0, self.saveto)

    def start(self):
        url = self.urlentry.get()
        folder = self.savetoentry.get()
        if url == '':
            self.statusmsg.set('Enter Youtube URL for converting Video!!')
            return
        elif folder == '':
            self.statusmsg.set('Enter file location to save your PDF!!')
            return
        else:
            self.set()
            video_to_pdf_main()

    def set(self):
        url = self.urlentry.get()
        vid_to_pdf_logo = ImageTk.PhotoImage(Image.open('resources/vid2pdf_logo_img.jpg'))
        if url == '':
            self.statusmsg.set('Enter Youtube URL for converting Video!!')
            return
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            video_id = re.findall(r'(?<=v=)[\w-]+', url)[0]
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"

            img_data = requests.get(thumbnail_url).content
            img = Image.open(BytesIO(img_data))
            img = img.resize((625, 306), Image.ANTIALIAS)
            img_tk = ImageTk.PhotoImage(img)

            logo_label = self.logo_panel.winfo_children()[0]
            logo_label.configure(image=img_tk)
            logo_label.image = img_tk
            logo_label.grid(row=0, column=1, pady=10)
            self.logo_panel.grid_columnconfigure(0, weight=1)
            self.logo_panel.grid_rowconfigure(0, weight=1)

            title = str(soup.find('title').string).split("- YouTube")[0].strip()
            if title == '':
                raise
            self.vtitlemsg.set(title)
            self.statusmsg.set("Waiting...")

        except Exception:
            self.vtitlemsg.set("vid2pdf")
            self.statusmsg.set(f"Video Not Found!!")
            logo_label = self.logo_panel.winfo_children()[0]
            logo_label.configure(image=vid_to_pdf_logo)
            logo_label.image = vid_to_pdf_logo
            logo_label.grid(row=0, column=1, pady=10)

    def cancel(self):
        self.flag = False

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    obj = VidToPdf()
    obj.run()
