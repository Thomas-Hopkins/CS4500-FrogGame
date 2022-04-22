from tkinter import ttk
import tkinter as tk


class ContextBase(ttk.Frame):
    """
    The base layout of a context. Each context represents an entirely different screen of
    the app. Contexts do not know about other contexts. If a context needs to know some data
    in a different context, it is preferred to have the main application use a getter on the
    context with the needed data, and then to use a setter on the context which needs the data.

    This class should be inherited by all contexts.
    """

    def __init__(
        self,
        master: tk.Tk,
        rows: int,
        columns: int,
        theme: str,
        name: str,
        *args,
        **kwargs
    ) -> None:
        ttk.Frame.__init__(self, master, *args, **kwargs)

        # Instance variables
        self.name: str = name
        self.using_theme: str = theme
        self.num_rows: int = rows
        self.num_columns: int = columns
        self.app: tk.Tk = master  # Reference back to application

        # Setup rows/columns
        for row in range(rows):
            self.rowconfigure(index=row, weight=1, minsize=100)

        for column in range(columns):
            self.columnconfigure(index=column, weight=1, minsize=150)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContextBase(master=root, rows=3, columns=3)
    app.pack(fill="both", expand=True)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    root.mainloop()
