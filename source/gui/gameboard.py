from tkinter import ttk, Tk, messagebox
from functools import partial
from gui.base import ContextBase
from localization import localizer


class GameboardContext(ContextBase):
    """
    The main game window. Has the gameboard, all game buttons, etc.
    """

    def __init__(self, *args, **kwargs) -> None:
        ContextBase.__init__(self, *args, **kwargs)

        self.rowconfigure(index=0, weight=5, minsize=100)
        self.rowconfigure(index=1, weight=90, minsize=100)
        self.rowconfigure(index=2, weight=5, minsize=100)
        # Title
        self.title = ttk.Label(
            self,
            justify="center",
            font=("-size", 30, "-weight", "bold"),
            text=localizer.get("GAME_TITLE"),
        )
        self.title.grid(row=0, column=1, padx=(10, 10), pady=(20, 10), sticky="n")

        self.timer = ttk.Label(
            self,
            justify="center",
            font=("-size", 18, "-weight", "bold"),
            text="Timer: 00:00",
        )
        self.timer.grid(row=0, column=0, padx=(10, 10), pady=(20, 10), sticky="sw")

        self.help_btn = ttk.Button(
            self, text="HELP", command=partial(print, "TODO: GOTO HELP")
        )
        self.help_btn.grid(row=0, column=2, padx=(10, 10), sticky="se")

        # Middle panel
        self.scores_panel = ttk.Labelframe(
            self,
            padding=(5, 5),
        )
        self.scores_panel.grid(
            row=1, column=0, columnspan=self.num_columns, sticky="nsew"
        )

        # Bottom Buttons
        self.mainmenu_btn = ttk.Button(
            self,
            text=localizer.get("ARROW_LEFT") + localizer.get("MAIN_MENU_BUTTON"),
            command=partial(
                self.__confirm_quit, partial(print, "TODO: RETURN MAIN MENU")
            ),
        )
        self.mainmenu_btn.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

        self.highscores_btn = ttk.Button(
            self,
            text=localizer.get("HIGHSCORES_BUTTON") + localizer.get("ARROW_RIGHT"),
            command=partial(print, "TODO: GOTO LAST CONTEXT"),
        )
        self.highscores_btn.grid(row=2, column=2, padx=(10, 10), pady=(10, 10))

    def __confirm_quit(self, func) -> None:
        ret = messagebox.askyesno(
            title="Are you sure?", message="Are you sure you want to quit?"
        )
        if ret:
            func()

    def set_mainmenu_cmd(self, command) -> None:
        self.mainmenu_btn.configure(command=partial(self.__confirm_quit, command))

    def set_highscores_cmd(self, command) -> None:
        self.highscores_btn.configure(command=command)

    def set_help_cmd(self, command) -> None:
        self.help_btn.configure(command=command)


if __name__ == "__main__":
    root = Tk()
    app = GameboardContext(master=root, rows=3, columns=3, theme=None, name="")
    app.pack(fill="both", expand=True)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    root.mainloop()
