from tkinter import ttk
from base import AppGuiBase


class Gameboard(AppGuiBase):
    """
    The main game window. Has the gameboard, all game buttons, etc.
    """

    def __init__(self, master, *args, **kwargs) -> None:
        AppGuiBase.__init__(self, master, *args, **kwargs)


if __name__ == "__main__":
    app = Gameboard(master=None)
    app.mainloop()
