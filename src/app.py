import downloader as dw
import customtkinter as ctk  # Changed this import
import ctypes
from PIL import Image


class App(ctk.CTk):  # Use ctk.CTk instead of CTk
    def __init__(self):
        super().__init__()

        myappid = "CryoDL"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        # set the appearance mode to dark
        ctk.set_appearance_mode("dark")

        # configure the root window
        self.title("CryoDL")
        self.iconbitmap("assets/icon.ico")
        self.geometry("900x600")
        self.resizable(False, False)

        self.configure(fg_color="#09191B")

        # create instances of the classes
        self.downloader = dw.Download()
        self.opener = dw.Open()

        # Load icon
        self.icon_image = Image.open("assets/icon.ico")
        self.icon = ctk.CTkImage(
            light_image=self.icon_image, dark_image=self.icon_image, size=(50, 50)
        )

        # frame
        self.frame = ctk.CTkFrame(self, fg_color="#183335")
        self.frame.pack(expand=True)

        # icon
        self.icon_label = ctk.CTkLabel(self.frame, image=self.icon, text="")
        self.icon_label.pack(pady=(15, 5))

        # title
        self.title_label = ctk.CTkLabel(
            self.frame, text="CryoDL", font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=(0, 10))

        # url entry
        self.url = ctk.CTkEntry(
            self.frame,
            width=400,
            justify="center",
            fg_color="#09191B",
            border_color="#406F72",
            placeholder_text="Enter URL here",
            placeholder_text_color="#1F504C",
            font=("Arial", 14, "italic"),
        )
        self.url.pack()

        # button frame
        self.button_frame = ctk.CTkFrame(self.frame, fg_color="#183135")
        self.button_frame.pack(pady=20)

        # audio directory button
        self.audio_dir_button = ctk.CTkButton(self.button_frame, text="📁", width=3)
        self.audio_dir_button.configure(
            command=self.opener.audio,
            fg_color="#37A9B1",
            hover_color="#2B7A8B",
            font=("Arial", 14, "bold"),
        )
        self.audio_dir_button.pack(ipadx=5, ipady=5, side=ctk.LEFT, padx=(10, 5))

        # download audio button
        self.dw_audio_button = ctk.CTkButton(self.button_frame, text="Download Audio")
        self.dw_audio_button.configure(
            command=lambda: self.downloader.audio(self.url.get()),
            fg_color="#37A9B1",
            hover_color="#2B7A8B",
            font=("Arial", 14, "bold"),
        )
        self.dw_audio_button.pack(ipadx=5, ipady=5, side=ctk.LEFT, padx=(5, 5))

        # download video button
        self.dw_video_button = ctk.CTkButton(self.button_frame, text="Download Video")
        self.dw_video_button.configure(
            command=lambda: self.downloader.video(self.url.get()),
            fg_color="#37A9B1",
            hover_color="#2B7A8B",
            font=("Arial", 14, "bold"),
        )
        self.dw_video_button.pack(ipadx=5, ipady=5, side=ctk.LEFT, padx=(5, 5))

        # video directory button
        self.video_dir_button = ctk.CTkButton(self.button_frame, text="📁", width=3)
        self.video_dir_button.configure(
            command=self.opener.video,
            fg_color="#37A9B1",
            hover_color="#2B7A8B",
            font=("Arial", 14, "bold"),
        )
        self.video_dir_button.pack(ipadx=5, ipady=5, side=ctk.LEFT, padx=(5, 10))


if __name__ == "__main__":
    app = App()
    app.mainloop()
