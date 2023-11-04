import tkinter as tk
import ttkbootstrap as ttk
from pytube import YouTube
import time 

def update_labels(title, views):
    label1['text'] = f"Title: {title}"
    label2['text'] = f"Views: {views}"

def clear_label():
    label1['text'] = ''
    
def download():
    url = entryvar.get()
    if not url:
        label1['text'] = 'No Link Provided'
        window.after(2500, clear_label)
        
    else:
        try:
            yt = YouTube(url)
            update_labels(yt.title, yt.views)
            yd = yt.streams.get_highest_resolution()
            yd.download(r'F:\projects\YouTubeVid downloader')
        except Exception as e:
            label1['text'] = 'Error: ' + str(e)

def create_ui():
    frame = ttk.Frame(window)
    frame.pack()

    # entry_style = ttk.Style()
    # entry_style.theme_use('info')

    entry = ttk.Entry(frame, bootstyle = 'dark' , textvariable=entryvar, width=40)
    entry.pack(pady=30)

    button = ttk.Button(frame, bootstyle = 'primary' , text='Download', command=download)
    button.pack()

    global label1, label2
    label1 = ttk.Label(frame, text='')
    label1.pack()

    label2 = ttk.Label(frame, text='')
    label2.pack()

window = ttk.Window()
window.geometry('600x200')
window.title("YouTube Video Downloader")

entryvar = tk.StringVar()

create_ui()

window.mainloop()
