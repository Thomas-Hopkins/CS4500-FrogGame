import tkinter as tk
from tkinter import ttk
from gui.gamewidget.boardpart import BoardPart


class GameboardPanel(ttk.Frame):
    def __init__(self, master, num_places: int, *args, **kwargs):
        ttk.Frame.__init__(self, master, *args, **kwargs)

        self.board_places = []

        self.board = ttk.Labelframe(
            self,
        )
        self.board.pack()

        for i in range(num_places):
            place = BoardPart(self.board, relief="raised", borderwidth=5)
            place.grid(row=0, column=i, padx=(2, 2), pady=(10, 10))
            self.board_places.append(place)

        self.scroll = ttk.Scrollbar(self, orient="horizontal")
        self.scroll.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = GameboardPanel(root)
    app.pack(fill="both", expand=True)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    root.mainloop()
