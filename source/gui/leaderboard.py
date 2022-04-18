from tkinter import ttk
from base import AppGuiBase


class Leaderboard(AppGuiBase):
    """
    Shows the top 10 scores.
    """

    def __init__(self, master, *args, **kwargs) -> None:
        AppGuiBase.__init__(self, master, *args, **kwargs)


if __name__ == "__main__":
    app = Leaderboard(master=None)
    app.mainloop()
