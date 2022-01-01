import tkinterdnd2.TkinterDnD as tk

from float_win import FloatingWindow

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.wm_attributes("-transparentcolor", "#f0f0f0")
        self.floater = FloatingWindow(self)

app = App()
app.mainloop()

