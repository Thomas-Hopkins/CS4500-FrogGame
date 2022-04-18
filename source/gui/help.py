from tkinter import ttk
from base import AppGuiBase


class Help(AppGuiBase):
    """
    Shows information about how this game works.
    """

    def __init__(self, master, *args, **kwargs) -> None:
        AppGuiBase.__init__(self, master, *args, **kwargs)


if __name__ == "__main__":
    app = Help(master=None)
    app.mainloop()
