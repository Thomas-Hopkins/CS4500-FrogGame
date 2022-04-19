from operator import truediv
import tkinter as tk
import os
from functools import partial
from gui.base import AppGuiBase
from gui.welcome import Welcome
from gui.gameboard import Gameboard
from gui.leaderboard import Leaderboard
from gui.help import Help

THEME_FILE = f"{os.getcwd()}\gui\Sun-Valley-ttk-theme\sun-valley.tcl"
DEFAULT_THEME = "light"


class Application:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.current_context = None
        self.using_theme = self.__has_themes_installed()
        self.welcome_screen = Welcome(
            master=self.root, theme=self.using_theme, rows=3, columns=3
        )
        self.gameboard_screen = Gameboard(
            master=self.root, theme=self.using_theme, rows=3, columns=3
        )
        self.leaderboard_screen = Leaderboard(
            master=self.root, theme=self.using_theme, rows=3, columns=3
        )
        self.help_screen = Help(
            master=self.root, theme=self.using_theme, rows=3, columns=3
        )

        self.welcome_screen.set_theme_cmd(partial(self.__change_theme))

        self.welcome_screen.set_play_cmd(
            partial(self.__switch_context, screen=self.gameboard_screen)
        )
        self.welcome_screen.set_highscores_cmd(
            partial(self.__switch_context, screen=self.leaderboard_screen)
        )

        self.leaderboard_screen.set_back_cmd(
            partial(self.__switch_context, screen=self.welcome_screen)
        )

        self.gameboard_screen.set_back_cmd(
            partial(self.__switch_context, screen=self.welcome_screen)
        )

        self.__switch_context(self.welcome_screen)
        self.__import_theme()

        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        x_cordinate = int(
            (self.root.winfo_screenwidth() / 2) - (self.root.winfo_width() / 2)
        )
        y_cordinate = int(
            (self.root.winfo_screenheight() / 2) - (self.root.winfo_height() / 2)
        )
        self.root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

    def __has_themes_installed(self) -> str:
        if os.path.exists(THEME_FILE):
            return DEFAULT_THEME
        return None

    def __import_theme(self):
        if self.using_theme:
            self.root.tk.call("source", THEME_FILE)
            self.root.tk.call("set_theme", self.using_theme)

    def __change_theme(self):
        if self.root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
            self.root.tk.call("set_theme", "light")
        else:
            self.root.tk.call("set_theme", "dark")

    def __switch_context(self, screen: AppGuiBase):
        if self.current_context:
            self.current_context.pack_forget()

        self.current_context = screen
        self.current_context.pack(fill="both", expand=True)

    def mainloop(self):
        self.root.mainloop()
