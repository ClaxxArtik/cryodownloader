import downloader as dw
import tkinter as tk
from customtkinter import *


class App(CTk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title("CryoDownloader")
        self.geometry("900x600")
        self.resizable(False, False)

        # Create instances of the classes
        self.downloader = dw.Download()
        self.opener = dw.Open()

        # frame
        self.frame = CTkFrame(self)
        self.frame.pack(expand=True)

        # label
        self.label = CTkLabel(self.frame, text="Youtube URL:")
        self.label.pack(pady=10)

        # url entry
        self.url = CTkEntry(self.frame, width=400, justify="center")
        self.url.pack()

        # button frame
        self.button_frame = CTkFrame(self.frame)
        self.button_frame.pack(pady=20)

        # audio directory button
        self.audio_dir_button = CTkButton(self.button_frame, text="📁", width=3)
        self.audio_dir_button.configure(command=self.opener.audio)
        self.audio_dir_button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=(10, 5))

        # download audio button
        self.dw_audio_button = CTkButton(self.button_frame, text="Download audio")
        self.dw_audio_button.configure(
            command=lambda: self.downloader.audio(self.url.get())
        )
        self.dw_audio_button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=(5, 5))

        # download video button
        self.dw_video_button = CTkButton(self.button_frame, text="Download video")
        self.dw_video_button.configure(
            command=lambda: self.downloader.video(self.url.get())
        )
        self.dw_video_button.pack(ipadx=5, ipady=5, side=tk.LEFT, padx=(5, 5))

        # video directory button
        self.video_dir_button = CTkButton(self.button_frame, text="📁", width=3)
        self.video_dir_button.configure(command=self.opener.video)
        self.video_dir_button.pack(
            ipadx=5, ipady=5, side=tk.LEFT, padx=(5, 10)
        )  # Changed to (5, 10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
