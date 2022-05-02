import tkinter as tk
from tkinter import ttk
import random
from functools import partial
from source.froggame.game import Game
from PIL import Image, ImageTk


class GameboardPanel(ttk.Frame):
    def __init__(
        self, master, num_places: int, win_func, *args, size: int = 50, **kwargs
    ):
        ttk.Frame.__init__(self, master, *args, **kwargs)

        self.win_func = win_func
        self.app = master
        self.size = size
        self.num_places = num_places
        self.num_moves = 0
        # list of gameboard places, each index is a list with frog image ids list
        # Example: [[2, 5, 8], [], [0, 1], ...]
        self.gameboard2frogids = []
        self.gameboard2labelids = []

        self.canvas = tk.Canvas(
            self,
            bg="blue",
            height=size,
            width=num_places * size if num_places * size < 800 else 800,
            scrollregion=(0, 0, num_places * (size + 5), 0),
        )
        self.canvas.pack(side="top", expand=True, fill="both", anchor="nw")

        self.frog_image = Image.open("resources/frog.png")

        self.gameboard = Game(num_spaces=self.num_places)
        self.__draw_board()

        # Bottom scrollbar
        self.scroll = ttk.Scrollbar(
            self, orient="horizontal", command=self.canvas.xview
        )
        self.scroll.pack(side="bottom", expand=True, fill="both")

        self.canvas.configure(xscrollcommand=self.scroll.set)

        self.button_panel = ttk.Frame(self, padding=(5, 5))
        self.button_panel.pack(
            side="bottom", expand=True, fill="both", before=self.scroll
        )

        self.left_btn = ttk.Button(
            self.button_panel, text="LEFT", command=self.move_selected_left
        )
        self.left_btn.pack(side="left", expand=True, fill="both")

        self.right_btn = ttk.Button(
            self.button_panel, text="RIGHT", command=self.move_selected_right
        )
        self.right_btn.pack(side="right", expand=True, fill="both")

        self.app.bind("<Configure>", self.__update_size)
        self.enable_scroll()

    def __draw_board(self):
        """
        This will draw (or re-draw) the gameboard. Including lilypads, frogs, and frog counts.

        This is called on initial gameboard creation and on resize.
        """
        # Clear canvas
        self.canvas.delete("all")

        # Calculate frog image sizes
        height, width = self.frog_image.size

        new_height = self.size
        image = self.frog_image.resize(
            (new_height, new_height * width // height), Image.LANCZOS
        )
        self.image_thumb_big = ImageTk.PhotoImage(image=image)

        new_height = 2 * new_height // 3
        image = self.frog_image.resize(
            (new_height, new_height * width // height), Image.LANCZOS
        )
        self.image_thumb = ImageTk.PhotoImage(image=image)

        # clear previous mappings
        self.gameboard2frogids.clear()
        self.gameboard2labelids.clear()

        # Create the lilypads.
        x1, y1 = (0, 0)
        x2, y2 = (self.size, self.size)
        for place in range(self.num_places):
            self.canvas.create_arc(
                (x1, y1, x2, y2),
                extent=300 + random.randint(0, 50),
                start=random.randint(0, 180),
                fill="green",
            )

            # Increment to next coordinate
            x1 += self.size + 5
            x2 += self.size + 5

        # Create frogs. We do this later because of stacking order.
        x1, y1 = (0, 0)
        x2, y2 = (self.size, self.size)
        for place in range(self.num_places):
            num_frogs = self.gameboard.gameboard[place]
            # Create a frog for each frog on this space (initally only one frog on the space)
            # This is meant to handle re-draws when frogs have moved on the board
            frogs = []
            for _ in range(num_frogs):
                # Create frog
                img = self.canvas.create_image(
                    x1 + (self.size // 2), y1 + (self.size // 2), image=self.image_thumb
                )
                # Bind this frog image select command
                self.canvas.tag_bind(
                    img, "<Button-1>", partial(self.__select_space, place)
                )

                frogs.append(img)

            # Store the mappings from board index to image index
            self.gameboard2frogids.append(frogs)

            # Increment to next coordinate
            x1 += self.size + 5
            x2 += self.size + 5

        # Create labels.
        x1, y1 = (0, 0)
        x2, y2 = (self.size, self.size)
        for place in range(self.num_places):
            label = self.canvas.create_text(
                x1 + 10 + 3 * (self.size // 4),
                y1 + 10 + 3 * (self.size // 4),
                text=str(self.gameboard.gameboard[place]),
                fill="white",
                font=("Helvetica", 18, "bold"),
            )

            # Store the mapping from board index to label index
            self.gameboard2labelids.append([label])

            # Increment to next coordinate
            x1 += self.size + 5
            x2 += self.size + 5

    def __update_size(self, event):
        new_size = (event.height // 100) * 100
        new_size = new_size - 100 if new_size >= 100 else 100
        if new_size == self.size:
            return
        self.size = new_size
        print("changing size")
        self.canvas.configure(
            width=self.num_places * self.size,
            height=self.size,
            scrollregion=(0, 0, self.num_places * (self.size + 5), 0),
        )
        self.__draw_board()

    def __scroll_wheel(self, event):
        self.canvas.xview_scroll(-1 * (event.delta // 120), "units")

    def __check_win(self, wait_mult: int) -> None:
        if self.gameboard.has_won():
            self.left_btn.configure(state="disabled")
            self.right_btn.configure(state="disabled")
            self.win_func(int(1800 + wait_mult * 1.05))

    def __lerp_left(self, img_id: int, units: int, speed: int = 1) -> None:
        if units <= 0:
            # If we've overshot, move back to the correct pos
            self.canvas.move(img_id, -units, 0)
            return
        self.canvas.move(img_id, -1 * speed, 0)
        self.app.after(5, self.__lerp_left, img_id, units - (1 * speed), speed)

    def __lerp_right(self, img_id: int, units: int, speed: int = 1) -> None:
        if units <= 0:
            # If we've overshot, move back to the correct pos
            self.canvas.move(img_id, units, 0)
            return
        self.canvas.move(img_id, 1 * speed, 0)
        self.app.after(5, self.__lerp_right, img_id, units - (1 * speed), speed)

    def __lerp_frog(self, img_id: int, dir_units: int, speed: int, wait: int) -> None:
        if dir_units < 0:
            self.app.after(wait, self.__lerp_left, img_id, abs(dir_units), speed)
        else:
            self.app.after(wait, self.__lerp_right, img_id, abs(dir_units), speed)

    def __update_counts(self) -> None:
        for i, num_frogs in enumerate(self.gameboard.gameboard):
            label_id = self.gameboard2labelids[i]
            self.canvas.itemconfigure(label_id, text=num_frogs)

    def __unselect_space(self, index: int) -> None:
        if index is not None:
            img_ids = self.gameboard2frogids[index]
            for img_id in img_ids:
                self.canvas.itemconfigure(img_id, image=self.image_thumb)
            self.gameboard.set_selected_pad(None)

    def __select_space(self, index: int, event) -> None:
        """
        Called by the bind event on the frog image. Passes the index on the board and an event.
        """
        # Reset previously selected frog's size
        if self.gameboard.get_selected_pad() != None:
            prev_img_ids = self.gameboard2frogids[self.gameboard.get_selected_pad()]
            for img_id in prev_img_ids:
                self.canvas.itemconfigure(img_id, image=self.image_thumb)

        self.gameboard.set_selected_pad(index)
        img_ids = self.gameboard2frogids[index]

        # Make frogs on selected space bigger
        for img_id in img_ids:
            self.canvas.itemconfigure(img_id, image=self.image_thumb_big)

    def move_selected_left(self) -> None:
        """
        Move the selected frog left by num_spaces.
        """
        spaces_moved = self.gameboard.move_right()
        selected_space = self.gameboard.get_selected_pad()
        if spaces_moved > 0:
            self.num_moves += 1
            img_ids = self.gameboard2frogids[selected_space]
            new_index = selected_space - spaces_moved

            # Move the images
            wait_amount = 0
            for img_id in img_ids:
                self.__lerp_frog(
                    img_id,
                    -(self.size + 5) * spaces_moved,
                    spaces_moved * self.size * 0.02,
                    wait_amount,
                )
                # Move images ids to correct index of internal data
                self.gameboard2frogids[new_index].append(img_id)

                self.canvas.tag_bind(
                    img_id, "<Button-1>", partial(self.__select_space, new_index)
                )
                wait_amount += 300
            # update selected index to have no frogs
            self.gameboard2frogids[selected_space] = []
            self.__unselect_space(new_index)
            self.__check_win(wait_amount)
            self.__update_counts()

        self.__unselect_space(selected_space)

    def move_selected_right(self) -> None:
        """
        Move the selected frog right by num_spaces.
        """
        spaces_moved = self.gameboard.move_left()
        selected_space = self.gameboard.get_selected_pad()
        if spaces_moved > 0:
            self.num_moves += 1
            img_ids = self.gameboard2frogids[selected_space]
            new_index = selected_space + spaces_moved

            # Move the images
            wait_amount = 0
            for img_id in img_ids:
                self.__lerp_frog(
                    img_id,
                    (self.size + 5) * spaces_moved,
                    spaces_moved * self.size * 0.02,
                    wait_amount,
                )
                # Move images ids to correct index of internal data
                self.gameboard2frogids[new_index].append(img_id)

                self.canvas.tag_bind(
                    img_id, "<Button-1>", partial(self.__select_space, new_index)
                )
                wait_amount += 300

            # update selected index to have no frogs
            self.gameboard2frogids[selected_space] = []
            self.__unselect_space(new_index)
            self.__check_win(wait_amount)
            self.__update_counts()

        self.__unselect_space(selected_space)

    def enable_scroll(self) -> None:
        self.canvas.bind_all("<MouseWheel>", self.__scroll_wheel)

    def get_num_moves(self) -> int:
        return self.num_moves

    def get_num_frogs(self) -> int:
        return self.num_places

    def get_num_stacked(self) -> int:
        return len(max(self.gameboard2frogids, key=len))


if __name__ == "__main__":
    root = tk.Tk()
    app = GameboardPanel(root, num_places=10)
    app.pack()

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    root.mainloop()
