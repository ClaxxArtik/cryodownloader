import downloader as dw
import tkinter as tk
from tkinter import ttk

# main window
root = tk.Tk()
root.geometry('900x600')
root.resizable(False, False)
root.title('Button Demo')

main_text = ttk.Label(root, text='Youtube URL:')
main_text.pack()

url_entry = ttk.Entry(root, width=40)
url_entry.pack(pady=10)

# exit button
mp3_button = ttk.Button(
    root,
    text='Download Audio',
    command=lambda: dw.download_audio([url_entry.get()]) 
    if url_entry.get() 
    else None
)

mp3_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

mp4_button = ttk.Button(
    root,
    text='Download Video',
    command=lambda: dw.download_video([url_entry.get()]) 
    if url_entry.get() 
    else None
)

mp4_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()