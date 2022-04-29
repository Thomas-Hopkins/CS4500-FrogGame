from tkinter import ttk
import tkinter as tk


class AppGuiBase(ttk.Frame):
    """
    The base layout of the game window.
    """

    def __init__(
        self, master, rows: int, columns: int, *args, theme: str, **kwargs
    ) -> None:
        ttk.Frame.__init__(self, master, *args, **kwargs)

        self.using_theme: str = theme
        self.num_rows: int = rows
        for row in range(rows):
            self.rowconfigure(index=row, weight=1, minsize=100)

        self.num_columns: int = columns
        for column in range(columns):
            self.columnconfigure(index=column, weight=1, minsize=150)


if __name__ == "__main__":
    root = tk.Tk()
    app = AppGuiBase(master=root, rows=3, columns=3)
    app.pack(fill="both", expand=True)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    root.mainloop()