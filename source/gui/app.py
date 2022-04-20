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


class Application(tk.Tk):
    """
    Wrapper around the main Tk instance. Handles context switching, window setup, etc.
    """

    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.current_context = None
        self.using_theme = DEFAULT_THEME if self.__has_themes_installed() else None
        self.welcome_screen = Welcome(
            master=self, theme=self.using_theme, rows=3, columns=3
        )
        self.gameboard_screen = Gameboard(
            master=self, theme=self.using_theme, rows=3, columns=3
        )
        self.leaderboard_screen = Leaderboard(
            master=self, theme=self.using_theme, rows=3, columns=3
        )
        self.help_screen = Help(master=self, theme=self.using_theme, rows=3, columns=3)

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

        self.update()

        # Restrict resizing to a min size, and position on center of screen
        self.minsize(self.winfo_width(), self.winfo_height())
        xcoord = (self.winfo_screenwidth() // 2) - (self.winfo_width() // 2)
        ycoord = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{xcoord}+{ycoord}")

    def __has_themes_installed(self) -> bool:
        if os.path.exists(THEME_FILE):
            return True
        return False

    def __import_theme(self):
        if self.using_theme:
            self.tk.call("source", THEME_FILE)
            self.tk.call("set_theme", self.using_theme)

    def __change_theme(self):
        if self.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
            self.tk.call("set_theme", "light")
        else:
            self.tk.call("set_theme", "dark")

    def __switch_context(self, screen: AppGuiBase):
        if self.current_context:
            self.current_context.pack_forget()

        self.current_context = screen
        self.current_context.pack(fill="both", expand=True)
