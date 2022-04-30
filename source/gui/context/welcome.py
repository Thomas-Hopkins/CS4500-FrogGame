from tkinter import ttk, messagebox
import tkinter as tk
from functools import partial
from source.gui.context.base import ContextBase
from source.localization import localizer
from source.configuration.config import Config


class WelcomeContext(ContextBase):
    """
    Initial screen upon starting the game.
    """

    def __init__(self, *args, **kwargs) -> None:
        ContextBase.__init__(self, *args, **kwargs)

        self.use_dark_theme = tk.BooleanVar(
            value=True if self.using_theme == "dark" else False
        )
        self.selected_lang = tk.StringVar()

        # Top right version
        self.version_label = ttk.Label(
            self,
            padding=(20, 20),
            text=localizer.get("VERSION_LABEL") + " " + Config.get("version"),
        )
        self.version_label.grid(row=0, column=0, sticky="nw")

        # Bottom-Left options panel
        self.options_panel = ttk.Labelframe(
            self,
            padding=(20, 10),
            text=localizer.get("OPTIONS_PANEL"),
        )
        self.options_panel.grid(
            row=2, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        self.switch = ttk.Checkbutton(
            self.options_panel,
            text=localizer.get("DARK_OPTION"),
            variable=self.use_dark_theme,
            style="Switch.TCheckbutton" if self.using_theme else "",
            state="" if self.using_theme else "disabled",
            command=partial(print, "TODO: SWITCH THEME"),
        )
        self.switch.grid(row=0, column=0, padx=5, pady=10, sticky="sw")

        self.lang_combo = ttk.Combobox(
            self.options_panel,
            values=tuple(localizer.AVAILABLE_LANGS.values()),
            state="readonly",
            textvariable=self.selected_lang,
            width=15,
        )
        # Bind the selection event to change the language, postcommand attribute doesn't work correctly
        self.lang_combo.bind("<<ComboboxSelected>>", lambda e: self.__set_language())
        self.lang_combo.current(
            list(localizer.AVAILABLE_LANGS.keys()).index(Config.get("language"))
        )
        self.lang_combo.grid(row=1, column=0, padx=5, pady=5, sticky="sw")

        # Middle title panel
        self.title_panel = ttk.Frame(
            self,
            padding=(20, 10),
        )
        self.title_panel.grid(
            row=1, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew"
        )

        self.label_title = ttk.Label(
            self.title_panel,
            text=localizer.get("GAME_TITLE"),
            justify="center",
            font=("-size", 54, "-weight", "bold"),
        )
        self.label_title.pack()

        # Bottom-Middle buttons panel
        self.buttons_panel = ttk.Frame(
            self,
            padding=(20, 10),
        )
        self.buttons_panel.grid(
            row=2, column=1, padx=(20, 20), pady=(10, 10), sticky="nsew"
        )

        self.play_btn = ttk.Button(
            self.buttons_panel,
            text=localizer.get("PLAY_BUTTON"),
            command=partial(print, "TODO: GOTO PLAY GAME"),
            style="Accent.TButton" if self.using_theme else "",
        )
        self.play_btn.pack(
            anchor="se", expand=True, fill="both", padx=(10, 10), pady=(5, 5)
        )

        self.leaderboard_btn = ttk.Button(
            self.buttons_panel,
            text=localizer.get("HIGHSCORES_BUTTON"),
            command=partial(print, "TODO: GOTO HIGH SCORES"),
        )
        self.leaderboard_btn.pack(
            anchor="se", expand=True, fill="both", padx=(10, 10), pady=(5, 5)
        )

        # Credits/copyright
        self.copyright_panel = ttk.Labelframe(self, padding=(20, 10), text="Copyright")
        self.copyright_panel.grid(
            row=2, column=2, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        self.copyright_label = ttk.Label(
            self.copyright_panel,
            text=f"{localizer.get('GAME_TITLE')} {localizer.get('GAME_COPYRIGHT')}",
            wraplength=150,
            font=("-size", 8),
        )
        self.copyright_label.pack(pady=(5, 5), anchor="sw")

        if self.using_theme:
            self.theme_copyright_label = ttk.Label(
                self.copyright_panel,
                text=f"{localizer.get('THEME_NAME')} {localizer.get('THEME_COPYRIGHT')}",
                wraplength=150,
                font=("-size", 8),
            )
            self.theme_copyright_label.pack(pady=(5, 5), anchor="sw")

    def __set_language(self) -> None:
        # Clear selection because tkinter selects text upon changing the combobox value
        self.lang_combo.selection_clear()

        # If the selected language is the same as already loaded language return
        if self.selected_lang.get() == localizer.AVAILABLE_LANGS.get(
            Config.get("language")
        ):
            return

        Config.set(
            "language", localizer.AVAILABLE_LANGS_REVERSED.get(self.selected_lang.get())
        )
        Config.save_config()
        ret = messagebox.askokcancel(
            localizer.get("RELOAD_APP"), localizer.get("RELOAD_APP_MSG")
        )
        if ret:
            self.app.reload()

    def set_theme_cmd(self, command) -> None:
        self.switch.configure(command=command)

    def set_play_cmd(self, command) -> None:
        self.play_btn.configure(command=command)

    def set_highscores_cmd(self, command) -> None:
        self.leaderboard_btn.configure(command=command)


if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeContext(master=root, rows=3, columns=3)
    app.pack(fill="both", expand=True)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    root.mainloop()
