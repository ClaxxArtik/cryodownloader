import downloader as dw
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title("CryoDownloader")
        self.geometry("900x600")
        self.resizable(False, False)

        # frame
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True)

        # label
        self.label = ttk.Label(self.frame, text="Youtube URL:")
        self.label.pack(pady=10)

        # url entry
        self.url = ttk.Entry(self.frame, width=60, justify="center")
        self.url.pack()

        # button frame
        self.button_frame = ttk.Frame(self.frame)
        self.button_frame.pack(pady=20)

        # audio directory button
        self.audio_dir_button = ttk.Button(self.button_frame, text="📁", width=3)
        self.audio_dir_button["command"] = dw.Open.audio
        self.audio_dir_button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=(10, 5))

        # download audio button
        self.dw_audio_button = ttk.Button(self.button_frame, text="Download audio")
        self.dw_audio_button["command"] = lambda: dw.Download.audio(self.url.get())
        self.dw_audio_button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=(5, 5))

        # download video button
        self.dw_video_button = ttk.Button(self.button_frame, text="Download video")
        self.dw_video_button["command"] = lambda: dw.Download.video(self.url.get())
        self.dw_video_button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=(5, 5))

        # video directory button
        self.video_dir_button = ttk.Button(self.button_frame, text="📁", width=3)
        self.video_dir_button["command"] = dw.Open.video
        self.video_dir_button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=(10, 5))


if __name__ == "__main__":
    app = App()
    app.mainloop()
