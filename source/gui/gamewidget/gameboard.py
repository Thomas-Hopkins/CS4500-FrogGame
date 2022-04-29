import tkinter as tk
from tkinter import ttk
import random
from functools import partial
from source.froggame.game import Game
from PIL import Image, ImageTk


class GameboardPanel(ttk.Frame):
    def __init__(self, master, num_places: int, *args, size: int = 50, **kwargs):
        ttk.Frame.__init__(self, master, *args, **kwargs)

        self.app = master
        self.size = size
        self.canvas = tk.Canvas(
            self,
            bg="blue",
            height=size,
            width=num_places * size if num_places * size < 800 else 800,
            scrollregion=(0, 0, num_places * (size + 5), 0),
        )
        self.canvas.pack(side="top")

        image = Image.open("resources/ConcernedFroge.png")
        image.thumbnail((3 * size // 4, 3 * size // 4), Image.ANTIALIAS)
        self.image_thumb_big = ImageTk.PhotoImage(image=image)
        image.thumbnail((size // 3, size // 3), Image.ANTIALIAS)
        self.image_thumb = ImageTk.PhotoImage(image=image)

        # list of gameboard places, each index is a list with frog image ids list
        # Example: [[2, 5, 8], [], [0, 1], ...]
        self.gameboard_mapping = []
        self.gameboard = Game(num_spaces=num_places)

        # Create the lilypads.
        x1, y1 = (0, 0)
        x2, y2 = (size, size)
        for i in range(num_places):
            # TODO: Replace with image later?
            self.canvas.create_arc(
                (x1, y1, x2, y2),
                extent=300 + random.randint(0, 50),
                start=random.randint(0, 180),
                fill="green",
            )

            # Increment to next coordinate
            x1 += size + 5
            x2 += size + 5

        # Create frogs. We do this later because of stacking order.
        x1, y1 = (0, 0)
        x2, y2 = (size, size)
        for i in range(num_places):
            # Create frog
            img = self.canvas.create_image(
                x1 + (size // 2), y1 + (size // 2), image=self.image_thumb
            )
            # Bind this frog image select command
            self.canvas.tag_bind(img, "<Button-1>", partial(self.__select_space, i))

            # Store the mapping from board index to image index
            self.gameboard_mapping.append([img])

            # Increment to next coordinate
            x1 += size + 5
            x2 += size + 5

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

        self.left_btn = ttk.Button(
            self.button_panel, text="RIGHT", command=self.move_selected_right
        )
        self.left_btn.pack(side="right", expand=True, fill="both")

    def __lerp_left(self, img_id, units, speed=1):
        if units == 0:
            return
        self.canvas.move(img_id, -1 * speed, 0)
        self.app.after(5, self.__lerp_left, img_id, units - (1 * speed), speed)

    def __lerp_right(self, img_id, units, speed=1):
        if units == 0:
            return
        self.canvas.move(img_id, 1 * speed, 0)
        self.app.after(5, self.__lerp_right, img_id, units - (1 * speed), speed)

    def __lerp_frog(self, img_id, dir_units, speed, wait):
        if dir_units < 0:
            self.app.after(wait, self.__lerp_left, img_id, abs(dir_units), speed)
        else:
            self.app.after(wait, self.__lerp_right, img_id, abs(dir_units), speed)

    def __unselect_space(self, index):
        if index:
            img_ids = self.gameboard_mapping[index]
            for img_id in img_ids:
                self.canvas.itemconfigure(img_id, image=self.image_thumb)
            self.gameboard.set_selected_pad(None)

    def __select_space(self, index, event):
        """
        Called by the bind event on the frog image. Passes the index on the board and an event.
        """
        # Reset previously selected frog's size
        if self.gameboard.get_selected_pad() != None:
            prev_img_ids = self.gameboard_mapping[self.gameboard.get_selected_pad()]
            for img_id in prev_img_ids:
                self.canvas.itemconfigure(img_id, image=self.image_thumb)

        self.gameboard.set_selected_pad(index)
        img_ids = self.gameboard_mapping[index]

        # Make frogs on selected space bigger
        for img_id in img_ids:
            self.canvas.itemconfigure(img_id, image=self.image_thumb_big)

    def move_selected_left(self) -> None:
        """
        Move the selected frog left by num_spaces.
        """
        spaces_moved = self.gameboard.move_right()
        if spaces_moved > 0:
            img_ids = self.gameboard_mapping[self.gameboard.get_selected_pad()]
            new_index = self.gameboard.get_selected_pad() - spaces_moved

            # Move the images
            wait_amount = 0
            for img_id in img_ids:
                self.__lerp_frog(
                    img_id, -(self.size + 5) * spaces_moved, spaces_moved, wait_amount
                )
                # Move images ids to correct index of internal data
                self.gameboard_mapping[new_index].append(img_id)

                self.canvas.tag_bind(
                    img_id, "<Button-1>", partial(self.__select_space, new_index)
                )
                wait_amount += 300
            # update selected index to have no frogs
            self.gameboard_mapping[self.gameboard.get_selected_pad()] = []
            self.__unselect_space(new_index)
        else:
            self.__unselect_space(self.gameboard.get_selected_pad())

        if self.gameboard.has_won():
            # TODO: Show win screen and check for high score
            print("YOU WIN")

    def move_selected_right(self) -> None:
        """
        Move the selected frog right by num_spaces.
        """
        spaces_moved = self.gameboard.move_left()
        if spaces_moved > 0:
            img_ids = self.gameboard_mapping[self.gameboard.get_selected_pad()]
            new_index = self.gameboard.get_selected_pad() + spaces_moved

            # Move the images
            wait_amount = 0
            for img_id in img_ids:
                self.__lerp_frog(
                    img_id, (self.size + 5) * spaces_moved, spaces_moved, wait_amount
                )
                # Move images ids to correct index of internal data
                self.gameboard_mapping[new_index].append(img_id)

                self.canvas.tag_bind(
                    img_id, "<Button-1>", partial(self.__select_space, new_index)
                )
                wait_amount += 300

            # update selected index to have no frogs
            self.gameboard_mapping[self.gameboard.get_selected_pad()] = []
            self.__unselect_space(new_index)
        else:
            self.__unselect_space(self.gameboard.get_selected_pad())

        if self.gameboard.has_won():
            # TODO: Show win screen and check for high score
            print("YOU WIN")


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
