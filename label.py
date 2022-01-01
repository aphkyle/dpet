import random
import tkinter as tk

from send2trash import send2trash
from tkinterdnd2 import DND_FILES

from config import sprite_sets


class AnimatedLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        self.sprite_set = next(sprite_sets.glob("*"))
        self.sprite = "drag1.png"
        self.image = tk.PhotoImage(file=f"{self.sprite_set}\\{self.sprite}") # to keep reference
        super().__init__(*args, **kwargs, image=self.image)
        # tkinterdnd2 requires __init__ first
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.drag_and_drop)

    def update(self, replace):
        self.image = tk.PhotoImage(file=f"{replace}\\{self.sprite}") # to keep reference
        self.configure(image=self.image)
        self.sprite_set = replace

    def drag_and_drop(self, event):
        for x in dir(event):
            print(x, eval(f"event.{x}", {"event": event}))
        send2trash(event.data)

