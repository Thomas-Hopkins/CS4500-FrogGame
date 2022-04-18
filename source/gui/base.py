from tkinter import ttk


class AppGuiBase(ttk.Frame):
    """
    The base layout of the game window.
    """

    def __init__(self, master, *args, **kwargs) -> None:
        ttk.Frame.__init__(self, master, *args, **kwargs)


if __name__ == "__main__":
    app = AppGuiBase(master=None)
    app.mainloop()
