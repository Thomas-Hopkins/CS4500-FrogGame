from cgitb import enable
import tkinter as tk
import os
from functools import partial
from gui.base import AppGuiBase
from gui.welcome import Welcome
from gui.gameboard import Gameboard
from gui.leaderboard import Leaderboard
from gui.help import Help
from localization import localizer

THEME_FILE = f"{os.getcwd()}\gui\Sun-Valley-ttk-theme\sun-valley.tcl"
DEFAULT_THEME = "light"


class Application(tk.Tk):
    """
    Wrapper around the main Tk instance. Handles context switching, window setup, etc.
    """

    def __init__(self) -> None:
        tk.Tk.__init__(self)

        # Set instance variables
        self.current_context: AppGuiBase = None
        self.previous_context: AppGuiBase = None
        self.using_theme: str = DEFAULT_THEME if self.__has_themes_installed() else None

        # Init all of the GUIs this app will use
        self.welcome_screen = Welcome(
            master=self,
            theme=self.using_theme,
            rows=3,
            columns=3,
            name=localizer.get("WELCOME_SCREEN"),
        )
        self.gameboard_screen = Gameboard(
            master=self,
            theme=self.using_theme,
            rows=3,
            columns=3,
            name=localizer.get("GAMEBOARD_SCREEN"),
        )
        self.leaderboard_screen = Leaderboard(
            master=self,
            theme=self.using_theme,
            rows=3,
            columns=3,
            name=localizer.get("LEADERBOARD_SCREEN"),
        )
        self.help_screen = Help(
            master=self,
            theme=self.using_theme,
            rows=3,
            columns=3,
            name=localizer.get("HELP_SCREEN"),
        )

        # Setup the GUIs commands
        self.welcome_screen.set_theme_cmd(partial(self.__change_theme))

        self.welcome_screen.set_play_cmd(
            partial(self.__switch_context, screen=self.gameboard_screen)
        )
        self.welcome_screen.set_highscores_cmd(
            partial(
                self.__switch_context,
                screen=self.leaderboard_screen,
                # When switching to leaderboard from welcome screen: refresh scores, disable back btn, enable main menu btn
                funcs=(
                    self.leaderboard_screen.refresh_scores,
                    partial(self.leaderboard_screen.set_back_btn_state, enabled=False),
                    partial(
                        self.leaderboard_screen.set_mainmenu_btn_state, enabled=True
                    ),
                ),
            )
        )

        self.leaderboard_screen.set_mainmenu_cmd(
            partial(self.__switch_context, screen=self.welcome_screen)
        )

        self.leaderboard_screen.set_back_cmd(
            partial(self.__switch_context, previous=True)
        )

        self.gameboard_screen.set_mainmenu_cmd(
            partial(self.__switch_context, screen=self.welcome_screen)
        )

        self.gameboard_screen.set_highscores_cmd(
            partial(
                self.__switch_context,
                screen=self.leaderboard_screen,
                # When switching to leaderboard from welcome screen: refresh scores, enable back btn, disable main menu btn
                funcs=(
                    self.leaderboard_screen.refresh_scores,
                    partial(self.leaderboard_screen.set_back_btn_state, enabled=True),
                    partial(
                        self.leaderboard_screen.set_mainmenu_btn_state, enabled=False
                    ),
                ),
            )
        )

        self.gameboard_screen.set_help_cmd(
            partial(self.__switch_context, screen=self.help_screen)
        )

        self.help_screen.set_back_cmd(partial(self.__switch_context, previous=True))

        # Set welcome screen as current context and try to import/use theme
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

    def __switch_context(
        self, screen: AppGuiBase = None, previous: bool = False, funcs: tuple = None
    ):
        """
        Handles switching the context from one screen to another.

        screen: the screen you wish to switch to
        previous: pass true if you wish to return to previous screen. This will ignore screen param.
        funcs: optionally pass a tuple of functions to execute immediately after switching
        """
        # Remove current context from the screen
        if self.current_context:
            self.current_context.pack_forget()

        # use previous context
        if previous or not screen:
            screen = self.previous_context

        # Set previous context to current context and current context to requested screen
        self.previous_context = self.current_context
        self.current_context = screen
        self.current_context.pack(fill="both", expand=True)

        # Execute functions from passed funcs if exists
        if funcs:
            for func in funcs:
                func()
