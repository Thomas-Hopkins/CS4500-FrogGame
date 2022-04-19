from tkinter import ttk, Tk
from functools import partial
from gui.base import AppGuiBase


class Gameboard(AppGuiBase):
    """
    The main game window. Has the gameboard, all game buttons, etc.
    """

    def __init__(self, master, *args, **kwargs) -> None:
        AppGuiBase.__init__(self, master, *args, **kwargs)

        self.label = ttk.Label(
            self,
            padding=(10, 10),
            justify="center",
            font=("-size", 45, "-weight", "bold"),
            text="TODO: GAMEBOARD SCREEN",
        )
        self.label.pack()

        self.back_btn = ttk.Button(
            self, text="BACK", command=partial(print, "TODO: GOTO WELCOME")
        )
        self.back_btn.pack()

    def set_back_cmd(self, command) -> None:
        self.back_btn.configure(command=command)


if __name__ == "__main__":
    root = Tk()
    app = Gameboard(master=root, rows=3, columns=3)
    app.pack(fill="both", expand=True)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    root.mainloop()
