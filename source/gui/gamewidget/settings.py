from tkinter import ttk
import tkinter as tk
import re
from localization import localizer

DEF_VALUE = 6
MAX_VALUE = 50
MIN_VALUE = 3


class SettingsPanel(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)

        self.num_frogs = tk.StringVar(value=DEF_VALUE)

        self.info_text = ttk.Label(
            self,
            justify="center",
            font=("-size", 16),
            text=localizer.get("HOWTO_SHORT_LABEL"),
            wraplength=700,
        )
        self.info_text.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(5, 5),
            padx=(10, 10),
        )

        self.separator = ttk.Separator(
            self,
        )
        self.separator.grid(
            row=1, column=0, columnspan=2, padx=(20, 10), pady=10, sticky="ew"
        )

        self.frogs_label = ttk.Label(
            self,
            font=("-size", 14, "-weight", "bold"),
            text=localizer.get("NUM_FROGS_LABEL"),
        )
        self.frogs_label.grid(row=2, column=0, pady=(5, 5), padx=(10, 10), sticky="e")

        self.frogs_selector = ttk.Spinbox(
            self,
            from_=MIN_VALUE,
            to=MAX_VALUE,
            wrap=True,
            textvariable=self.num_frogs,
            validatecommand=self.__validate_num_frogs,
            invalidcommand=self.__warn_invalid,
            validate="all",
        )
        self.frogs_selector.grid(
            row=2, column=1, pady=(5, 5), padx=(10, 10), sticky="w"
        )

        self.hint_label = ttk.Label(
            self, justify="center", font=("-size", 12), text=localizer.get("HINT_LABEL")
        )
        self.hint_label.grid(row=3, column=0, columnspan=2, pady=(5, 5), padx=(10, 10))

    def __warn_invalid(self) -> None:
        self.focus()

    def __validate_num_frogs(self) -> bool:
        num_frogs = self.num_frogs.get()
        if not num_frogs.isdigit():
            return False

        num_frogs = int(num_frogs)
        if num_frogs > MAX_VALUE or num_frogs < MIN_VALUE:
            return False
        return True

    def get_num_frogs(self) -> int:
        self.__validate_num_frogs()
        num_frogs = self.num_frogs.get()
        if not num_frogs.isdigit():
            # Try to remove non-digits
            fixed_num_frogs = ""
            for match in re.findall("(\d+)", num_frogs):
                fixed_num_frogs += match
            num_frogs = fixed_num_frogs

        # Ensure is in range
        num_frogs = int(num_frogs)
        if num_frogs > MAX_VALUE:
            return MAX_VALUE
        elif num_frogs < MIN_VALUE:
            return MIN_VALUE
        else:
            return num_frogs


if __name__ == "__main__":
    root = tk.Tk()
    app = SettingsPanel(root)
    app.pack(fill="both", expand=True)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    root.mainloop()
