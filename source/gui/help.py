from tkinter import ttk
from gui.base import AppGuiBase
from functools import partial


class Help(AppGuiBase):
    """
    Shows information about how this game works.
    """

    def __init__(self, master, *args, **kwargs) -> None:
        AppGuiBase.__init__(self, master, *args, **kwargs)

        self.label = ttk.Label(
            self,
            padding=(10, 10),
            justify="center",
            font=("-size", 45, "-weight", "bold"),
            text="TODO: HELP SCREEN",
        )
        self.label.pack()

        self.back_btn = ttk.Button(
            self, text="BACK", command=partial(print, "TODO: GOTO WELCOME")
        )
        self.back_btn.pack()

    def set_back_cmd(self, command) -> None:
        self.back_btn.configure(command=command)


if __name__ == "__main__":
    app = Help(master=None)
    app.mainloop()
