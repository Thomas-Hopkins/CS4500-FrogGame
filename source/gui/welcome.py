from tkinter import ttk
from base import AppGuiBase


class Welcome(AppGuiBase):
    """
    Initial screen upon starting the game.
    """

    def __init__(self, master, *args, **kwargs) -> None:
        AppGuiBase.__init__(self, master, *args, **kwargs)


if __name__ == "__main__":
    app = Welcome(master=None)
    app.mainloop()
