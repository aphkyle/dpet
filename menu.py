import platform
import subprocess
import tkinter as tk
from tkinter import filedialog

from config import sprite_sets


class SpriteMenu(tk.Menu):
    def __init__(self, event, *args, **kwargs):
        super().__init__(*args, **kwargs, tearoff=False)
        self.fire_event = event
        self.add_command(label="Select Sprite set", command=self.select_sprite_set)
        self.add_separator()
        self.add_command(label="Open recycle bin", command=self.open_recycle_bin)
        self.add_separator()
        self.add_command(label="Quit", command=quit)

    def select_sprite_set(self):
        self.fire_event(
            filedialog.askdirectory(initialdir=sprite_sets, title="Select sprite set")
        )

    def open_recycle_bin(self):
        if platform.system() == "Windows":
            subprocess.run(["start", "shell:RecycleBinFolder"], shell=True)
            # require shell
