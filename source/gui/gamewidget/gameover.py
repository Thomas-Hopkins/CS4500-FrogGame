from enum import Enum
from tkinter import ttk
import tkinter as tk
from functools import partial
from source.localization import localizer


class GameoverState(Enum):
    won = 1
    lost = 2


class GameoverPanel(ttk.Frame):
    def __init__(self, master, state: GameoverState, savescore_func, *args, **kwargs):
        ttk.Frame.__init__(self, master, *args, **kwargs)

        self.rowconfigure(index=0, weight=5, minsize=50)
        self.rowconfigure(index=1, weight=90, minsize=50)
        self.rowconfigure(index=2, weight=5, minsize=50)

        self.player_name = tk.StringVar(value="Player Name")

        self.label = ttk.Label(self, font=("-size", 24, "-weight", "bold"))
        if state == GameoverState.won:
            self.label.configure(text=localizer.get("WIN_LABEL"))
        elif state == GameoverState.lost:
            self.label.configure(text=localizer.get("LOST_LABEL"))
        self.label.grid(row=0, column=0, padx=(10, 10))

        self.score_panel = ttk.Frame(self)
        self.score_panel.grid(row=1, column=0, padx=(10, 10))

        self.score_label = ttk.Label(
            self.score_panel, font=("-size", 14), text=localizer.get("SCORE_NAME_LABEL")
        )
        self.score_label.pack(side="left", expand=True, fill="both", padx=(10, 10))

        self.score_box = ttk.Entry(
            self.score_panel, font=("-size", 14), textvariable=self.player_name
        )
        self.score_box.pack(side="right", expand=True, fill="both", padx=(10, 10))

        self.save_score = ttk.Button(
            self,
            text=localizer.get("SAVE_SCORE_BTN"),
            command=partial(savescore_func, self.player_name),
        )
        self.save_score.grid(row=2, column=0, padx=(10, 10))


if __name__ == "__main__":
    root = tk.Tk()
    from source.configuration.config import Config

    Config.get_instance()
    app = GameoverPanel(master=root, state=GameoverState.lost)
    app.pack()

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    root.mainloop()
