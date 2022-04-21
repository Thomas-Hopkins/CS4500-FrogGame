from tkinter import ttk
import tkinter as tk
from functools import partial
from turtle import st
from gui.base import AppGuiBase
from localization import localizer


class Leaderboard(AppGuiBase):
    """
    Shows the top 10 scores.
    """

    def __init__(self, master, *args, **kwargs) -> None:
        AppGuiBase.__init__(self, master, *args, **kwargs)

        # Title
        self.title = ttk.Label(
            self,
            justify="center",
            font=("-size", 30, "-weight", "bold"),
            text=localizer.get("LEADERBOARD_TITLE"),
        )
        self.title.grid(row=0, column=1, padx=(10, 10), pady=(20, 10), sticky="n")

        # Middle High scores panel
        self.scores_panel = ttk.Labelframe(
            self,
            padding=(5, 5),
        )
        self.scores_panel.grid(
            row=1, column=0, columnspan=self.num_columns, sticky="nsew"
        )
        self.scores_panel.rowconfigure(index=0, weight=1, minsize=100)
        self.scores_panel.columnconfigure(index=0, weight=1, minsize=50)
        self.scores_panel.columnconfigure(index=1, weight=100, minsize=50)
        self.scores_panel.columnconfigure(index=2, weight=1, minsize=50)

        self.scores_scroll = ttk.Scrollbar(
            self.scores_panel,
            orient="vertical",
        )
        self.scores_scroll.grid(row=0, column=2, sticky="nsew")

        headings = ["Player", "# Moves", "Time Played", "Frogs Stacked", "Total Score"]
        self.scores_table = ttk.Treeview(
            self.scores_panel,
            columns=headings,
            show="headings",
            yscrollcommand=self.scores_scroll.set,
        )

        self.scores_scroll.configure(command=self.scores_table.yview)

        for heading in headings:
            self.scores_table.column(heading, anchor="center", width=80)
            self.scores_table.heading(heading, text=heading, anchor="center")

        self.scores_table.grid(row=0, column=1, sticky="nsew")

        # Bottom Buttons
        self.mainmenu_btn = ttk.Button(
            self,
            text=localizer.get("ARROW_LEFT") + localizer.get("MAIN_MENU_BUTTON"),
            command=partial(print, "TODO: GOTO MAIN MENU"),
        )
        self.mainmenu_btn.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

        self.back_btn = ttk.Button(
            self,
            text=localizer.get("BACK_BUTTON") + localizer.get("ARROW_RIGHT"),
            command=partial(print, "TODO: GOTO LAST CONTEXT"),
        )
        self.back_btn.grid(row=2, column=2, padx=(10, 10), pady=(10, 10))

    def __read_scores(self) -> list:
        # TODO: Read scroes from leaderboard, for now generate and return mock data
        import random

        scores = []
        for i in range(10):
            scores.append(
                {
                    "player": f"player_{i}",
                    "moves": random.randint(10, 100),
                    "time": random.randint(100, 200) * random.random(),
                    "frogs": random.randint(10, 50),
                    "total": random.randint(1_000, 10_000),
                }
            )
        return scores

    def set_back_cmd(self, command) -> None:
        self.back_btn.configure(command=command)

    def set_mainmenu_cmd(self, command) -> None:
        self.mainmenu_btn.configure(command=command)

    def set_back_btn_state(self, enabled: bool) -> None:
        self.back_btn.configure(state="enabled" if enabled else "disabled")

    def set_mainmenu_btn_state(self, enabled: bool) -> None:
        self.mainmenu_btn.configure(state="enabled" if enabled else "disabled")

    def refresh_scores(self) -> None:
        self.scores_table.delete(*self.scores_table.get_children())

        scores = self.__read_scores()
        for i, score in enumerate(scores):
            self.scores_table.insert(
                parent="", index=i, iid=i, text="", values=tuple(score.values())
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = Leaderboard(master=root, theme=None, rows=3, columns=3)
    app.pack(fill="both", expand=True)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    root.mainloop()
