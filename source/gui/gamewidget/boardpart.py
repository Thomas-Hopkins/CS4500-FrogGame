import tkinter as tk
from tkinter import ttk


class BoardPart(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)

        self.tmp_label = ttk.Label(
            self,
            text="🐸",
            font=("-size", 50, "-weight", "bold"),
        )
        self.tmp_label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = BoardPart(root)
    app.pack(fill="both", expand=True)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    root.mainloop()
