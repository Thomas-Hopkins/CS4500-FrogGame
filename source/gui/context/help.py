from tkinter import ttk
import tkinter as tk
from source.localization import localizer
from source.gui.context.base import ContextBase
from functools import partial


class HelpContext(ContextBase):
    """
    Shows information about how this game works.
    """

    def __init__(self, height=1000, *args, **kwargs) -> None:
        ContextBase.__init__(self, *args, **kwargs)

        self.scroll_height = height
        self.wrap_texts = []  # Labels that ned dynamically updating text wrapping

        self.canvas = tk.Canvas(
            self,
            bg="blue",
            height=self.scroll_height,
            scrollregion=(0, 0, 0, self.scroll_height),
        )
        self.canvas.grid(
            row=0,
            column=0,
            rowspan=self.num_rows,
            columnspan=self.num_columns,
            sticky="nsew",
        )

        # Right scrollbar
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scroll.grid(row=0, column=3, rowspan=self.num_rows, sticky="ns")

        self.canvas.configure(yscrollcommand=self.scroll.set)

        # One column frame
        self.frame = ttk.Frame(self.canvas, height=self.scroll_height)
        self.frame.columnconfigure(0, weight=100)

        self.frame_id = self.canvas.create_window(0, 0, window=self.frame, anchor="nw")

        self.label = ttk.Label(
            self.frame,
            padding=(10, 10),
            justify="center",
            font=("-size", 45, "-weight", "bold"),
            text=localizer.get("HELP_TITLE"),
        )
        self.label.grid(row=0, column=0)

        self.separator = ttk.Separator(
            self.frame,
            orient="horizontal",
        )
        self.separator.grid(row=1, column=0, sticky="ew")

        self.moving_label = ttk.Label(
            self.frame,
            justify="left",
            font=("-size", 24),
            text=localizer.get("HELP_MOVE_SUBTITLE"),
        )
        self.moving_label.grid(row=2, padx=(10, 5), pady=(10, 5), column=0, sticky="ew")

        self.moving_textblock = ttk.Label(
            self.frame, font=("-size", 15), text=localizer.get("HELP_MOVEMENT")
        )
        self.moving_textblock.grid(
            row=3, column=0, padx=(10, 10), pady=(5, 5), sticky="ew"
        )
        self.wrap_texts.append(self.moving_textblock)

        self.separator_moving = ttk.Separator(
            self.frame,
            orient="horizontal",
        )
        self.separator_moving.grid(row=4, column=0, pady=(25, 0), sticky="ew")

        self.hint_label = ttk.Label(
            self.frame,
            justify="left",
            font=("-size", 24),
            text=localizer.get("HELP_HINT_SUBTITLE"),
        )
        self.hint_label.grid(row=5, padx=(10, 5), pady=(10, 5), column=0, sticky="ew")

        self.hint_textblock = ttk.Label(
            self.frame, font=("-size", 15), text=localizer.get("HELP_HINTSTIPS")
        )
        self.hint_textblock.grid(
            row=6, column=0, padx=(10, 10), pady=(5, 5), sticky="ew"
        )
        self.wrap_texts.append(self.hint_textblock)

        self.back_btn = ttk.Button(
            self,
            text="BACK",
            command=partial(print, "TODO: GOTO WELCOME"),
            style="Accent.TButton" if self.using_theme else "",
        )
        self.back_btn.grid(row=3, column=0, columnspan=self.num_columns, sticky="ew")

    def __scroll_wheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def __update_size(self, event):
        scroll_width = 25
        self.frame.configure(height=self.winfo_height())
        self.canvas.itemconfigure(
            self.frame_id,
            width=self.winfo_width() - scroll_width,
            height=self.scroll_height,
        )
        for text in self.wrap_texts:
            text.configure(wraplength=self.winfo_width() - scroll_width * 2)

    def leave_context(self):
        self.unbind_all("<MouseWheel>")
        self.unbind("<Configure>")
        return ContextBase.leave_context(self)

    def enter_context(self):
        self.bind("<Configure>", self.__update_size)
        self.bind_all("<MouseWheel>", self.__scroll_wheel)
        return ContextBase.enter_context(self)

    def set_back_cmd(self, command) -> None:
        self.back_btn.configure(command=command)


if __name__ == "__main__":
    root = tk.Tk()
    from source.configuration.config import Config

    Config.get_instance()
    app = HelpContext(master=root, rows=3, columns=3, theme=None, name="")
    app.pack(side="left", fill="both", expand=True)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    root.mainloop()
