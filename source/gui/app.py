import tkinter as tk
import os
from functools import partial
from gui.context.base import ContextBase
from gui.context.welcome import WelcomeContext
from gui.context.game import GameContext
from gui.context.leaderboard import LeaderboardContext
from gui.context.help import HelpContext
from localization import localizer
from configuration.config import Config
from util.utils import func_bundle

THEME_FILE = "../resources/sun-valley-theme/sun-valley.tcl"


class Application(tk.Tk):
    """
    Wrapper around the main Tk instance. Handles context switching, window setup,
    theme management, etc.

    Holds an instance of all contexts. Contexts do not know about other contexts,
    and so data should flow from a context <-> Application <-> other context if
    required.
    """

    def __init__(self) -> None:
        tk.Tk.__init__(self)
        Config.get_instance()

        # Set instance variables
        self.current_context: ContextBase = None
        self.previous_context: ContextBase = None
        self.using_theme: str = (
            Config.get("theme") if self.__has_themes_installed() else None
        )
        self.__import_theme()
        self.__load_everything()
        self.__set_window_size()

    def __load_everything(self) -> None:
        # Init all of the context GUIs this app will use
        self.welcome_context = WelcomeContext(
            master=self,
            theme=self.using_theme,
            rows=3,
            columns=3,
            name=localizer.get("WELCOME_SCREEN"),
        )
        self.gameboard_context = GameContext(
            master=self,
            theme=self.using_theme,
            rows=3,
            columns=3,
            name=localizer.get("GAMEBOARD_SCREEN"),
        )
        self.leaderboard_context = LeaderboardContext(
            master=self,
            theme=self.using_theme,
            rows=3,
            columns=3,
            name=localizer.get("LEADERBOARD_SCREEN"),
        )
        self.help_context = HelpContext(
            master=self,
            theme=self.using_theme,
            rows=3,
            columns=3,
            name=localizer.get("HELP_SCREEN"),
        )

        # Setup the GUIs commands
        self.welcome_context.set_theme_cmd(partial(self.__change_theme))

        self.welcome_context.set_play_cmd(
            partial(
                self.__switch_context,
                context=self.gameboard_context,
            )
        )
        self.welcome_context.set_highscores_cmd(
            partial(
                self.__switch_context,
                context=self.leaderboard_context,
                # When switching to leaderboard from welcome: refresh scores, disable back btn, enable main menu btn
                func=partial(
                    func_bundle,
                    (
                        self.leaderboard_context.refresh_scores,
                        partial(
                            self.leaderboard_context.set_back_btn_state, enabled=False
                        ),
                        partial(
                            self.leaderboard_context.set_mainmenu_btn_state,
                            enabled=True,
                        ),
                    ),
                ),
            )
        )

        self.leaderboard_context.set_mainmenu_cmd(
            partial(self.__switch_context, context=self.welcome_context)
        )

        self.leaderboard_context.set_back_cmd(
            partial(self.__switch_context, previous=True)
        )

        self.gameboard_context.set_mainmenu_cmd(
            partial(self.__switch_context, context=self.welcome_context)
        )

        self.gameboard_context.set_highscores_cmd(
            partial(
                self.__switch_context,
                context=self.leaderboard_context,
                # When switching to leaderboard from gameboard: refresh scores, enable back btn, disable main menu btn
                func=partial(
                    func_bundle,
                    (
                        self.leaderboard_context.refresh_scores,
                        partial(
                            self.leaderboard_context.set_back_btn_state, enabled=True
                        ),
                        partial(
                            self.leaderboard_context.set_mainmenu_btn_state,
                            enabled=False,
                        ),
                    ),
                ),
            )
        )

        self.gameboard_context.set_help_cmd(
            partial(self.__switch_context, context=self.help_context)
        )

        self.help_context.set_back_cmd(partial(self.__switch_context, previous=True))

        # Set welcome screen as current context and try to import/use theme
        self.__switch_context(self.welcome_context)

        self.update()

    def __set_window_size(self) -> None:
        # Get monitor size
        maxwidth = self.winfo_screenwidth()
        maxheight = self.winfo_screenheight()
        # Get requested size
        reqwidth = self.winfo_width()
        reqheight = self.winfo_height() + 50

        # If requested is greater than monitor, use monitor as min size
        if reqwidth > maxwidth:
            reqwidth = maxwidth
        if reqheight > maxheight:
            reqheight = maxheight

        # Restrict resizing to a min size, and position on center top of screen
        self.minsize(reqwidth, reqheight)
        xcoord = (maxwidth // 2) - (reqwidth // 2)
        ycoord = (maxheight // 3) - (reqheight // 2)

        # Ensure not off screen on small displays
        ycoord = ycoord if ycoord > 0 else 0
        self.geometry(f"{reqwidth}x{reqheight}+{xcoord}+{ycoord}")

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
            Config.set("theme", "light")
        else:
            self.tk.call("set_theme", "dark")
            Config.set("theme", "dark")
        Config.save_config()

    def __switch_context(
        self, context: ContextBase = None, previous: bool = False, func=None
    ):
        """
        Handles switching the context from one context to another.

        context: the context you wish to switch to
        previous: pass true if you wish to return to previous context. This will ignore context param.
        func: optionally pass a function to execute immediately after switching
        """
        # Store current size for later
        width = self.winfo_width()
        height = self.winfo_height()

        # Remove current context from the screen
        if self.current_context:
            self.current_context.pack_forget()

        # use previous context
        if previous or not context:
            context = self.previous_context

        # Set previous context to current context and current context to requested screen
        self.previous_context = self.current_context
        self.current_context = context
        self.current_context.pack(fill="both", expand=True)

        # Reset window size to previous, tkinter (annoyingly) automatically resizes
        if self.previous_context:
            self.geometry(f"{width}x{height}")

        # Update window title
        self.title(localizer.get("GAME_TITLE") + " - " + self.current_context.name)

        # Execute func if passed
        if func:
            func()

    def reload(self) -> None:
        self.__load_everything()
