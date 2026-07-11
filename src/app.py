import downloader as dw
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("900x600")
root.resizable(False, False)
root.title("CryoDownloader")

# Main container frame that will center everything
main_frame = ttk.Frame(root)
main_frame.pack(expand=True)

# Your widgets inside main_frame
main_text = ttk.Label(main_frame, text="Youtube URL:")
main_text.pack(pady=10)

url_entry = tk.Entry(main_frame, width=60, justify="center")
url_entry.pack()

button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=20)

# open audio button
mp3_dir_button = ttk.Button(
    button_frame, text="📁", command=lambda: dw.open_audio_dir(), width=3
)

mp3_dir_button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=(10, 5))

# download audio button
mp3_button = ttk.Button(
    button_frame,
    text="Download Audio",
    command=lambda: dw.download_audio(url_entry.get()) if url_entry.get() else None,
)

mp3_button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=(5, 5))

# download video button
mp4_button = ttk.Button(
    button_frame,
    text="Download Video",
    command=lambda: dw.download_video(url_entry.get()) if url_entry.get() else None,
)

mp4_button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=(5, 5))

# open video button
mp4_dir_button = ttk.Button(
    button_frame, text="📁", command=lambda: dw.open_video_dir(), width=3
)

mp4_dir_button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=(5, 10))

root.mainloop()
