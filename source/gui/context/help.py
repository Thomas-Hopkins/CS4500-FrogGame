from tkinter import ttk
from source.gui.context.base import ContextBase
from functools import partial


class HelpContext(ContextBase):
    """
    Shows information about how this game works.
    """

    def __init__(self, height=1000, *args, **kwargs) -> None:
        ContextBase.__init__(
            self, height=height, scrollregion=(0, 0, 0, height), *args, **kwargs
        )

        self.scroll_height = height

        # Right scrollbar
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.yview)
        self.scroll.pack(side="right", expand=False, fill="y", anchor="e")

        self.configure(yscrollcommand=self.scroll.set)

        self.frame = ttk.Frame(self, height=self.scroll_height)

        self.frame_id = self.create_window(0, 0, window=self.frame, anchor="nw")

        self.label = ttk.Label(
            self.frame,
            padding=(10, 10),
            justify="center",
            font=("-size", 45, "-weight", "bold"),
            text="TODO: HELP SCREEN",
        )
        self.label.pack()

        self.back_btn = ttk.Button(
            self.frame, text="BACK", command=partial(print, "TODO: GOTO WELCOME")
        )
        self.back_btn.pack()

    def __scroll_wheel(self, event):
        self.yview_scroll(-1 * (event.delta // 120), "units")

    def __update_size(self, event):
        self.frame.configure(height=self.winfo_height())
        self.itemconfigure(
            self.frame_id, width=self.winfo_width() - 25, height=self.scroll_height
        )

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
    app = HelpContext(master=None)
    app.mainloop()
