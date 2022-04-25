class Game:
    """
    Stores the gameboard data and handles all game logic.
    """

    def __init__(self, num_spaces: int) -> None:
        # TODO: build a gameboard of N spaces with a frog initially on each space
        # num_spaces = input("Enter the amount of spaces to play with: ")
        self.gameboard = [1 for x in range(int(num_spaces))]

    def set_selected_pad(self, index: int) -> None:
        # TODO: This will be called by the user interface when clicking on a frog/space. This will set the selected space
        # in the game, so that we can move all frogs on it with move_right/move_left
        self.selected_pad = index
        print(f" -> Selected pad {index}")

    def move_right(self) -> None:
        # TODO: Moves all frogs on the selected space right by N spaces if there is enough room on the board. N is
        # determined by how many frogs are on the selected space
        # Step 1: Decide the number of pads to jump
        pads_to_jump = self.gameboard[self.selected_pad]
        # Step 2: Ensure that the source & target pads are not empty
        if self.gameboard[self.selected_pad] < 1:
            err = f"Move right error!! Selected pad {self.selected_pad} is empty!!"
            print(err)
            return err
        if pads_to_jump > self.selected_pad:
            err = f"Move right error!! Cannot jump {pads_to_jump} frogs to the right from position {self.selected_pad}!!"
            print(err)
            return err
        if self.gameboard[self.selected_pad - pads_to_jump] < 1:
            err = f"Move right error!! Target pad cannot be empty!!"
            print(err)
            return err
        # Step 3: Do the jump
        self.gameboard[self.selected_pad - pads_to_jump] += pads_to_jump
        self.gameboard[self.selected_pad] = 0
        print(
            f" -> Moved (right) frogs from pad {self.selected_pad} to {self.selected_pad - pads_to_jump}"
        )

    def move_left(self) -> None:
        # TODO: Moves all frogs on the selected space left by N spaces if there is enough room on the board. N is
        # determined by how many frogs are on the selected space
        # Step 1: Decide the number of pads to jump
        pads_to_jump = self.gameboard[self.selected_pad]
        # Step 2: Ensure that the source & target pads are not empty
        if self.gameboard[self.selected_pad] < 1:
            err = f"Move left error!! Selected pad {self.selected_pad} is empty!!"
            print(err)
            return err
        if pads_to_jump + self.selected_pad >= len(self.gameboard):
            err = f"Move left error!! Cannot jump {pads_to_jump} frogs to the left from position {self.selected_pad}!!"
            print(err)
            return err
        if self.gameboard[pads_to_jump + self.selected_pad] < 1:
            err = f"Move left error!! Target pad cannot be empty!!"
            print(err)
            return err
        # Step 3: Do the jump
        self.gameboard[pads_to_jump + self.selected_pad] += pads_to_jump
        self.gameboard[self.selected_pad] = 0
        print(
            f" -> Moved (left) frogs from pad {self.selected_pad} to {self.selected_pad - pads_to_jump}"
        )

    def has_won(self) -> bool:
        # When called, returns true if game is won and false if game has not been won.
        pads_with_frogs = 0
        for i in range(len(self.gameboard)):
            if self.gameboard[i] > 0:
                pads_with_frogs += 1
        if pads_with_frogs == 1:
            return True
        return False

    def __repr__(self) -> str:
        return "TODO: return string representation of gameboard here for debugging purposes"


if __name__ == "__main__":
    g = Game(10)

    # Test move right method
    print(g.gameboard)
    g.set_selected_pad(3)
    g.move_right()
    print(g.gameboard)
    g.set_selected_pad(2)
    g.move_right()
    print(g.gameboard)
    g.set_selected_pad(2)
    g.move_right()
    print(g.gameboard)
    g.set_selected_pad(0)
    g.move_right()
    print(g.gameboard)
    g.set_selected_pad(4)
    g.move_right()
    print(g.gameboard)

    # Test move left method
    g.set_selected_pad(4)
    g.move_left()
    print(g.gameboard)
    g.set_selected_pad(1)
    g.move_left()
    print(g.gameboard)
    g.set_selected_pad(5)
    g.move_left()
    print(g.gameboard)
    g.set_selected_pad(7)
    g.move_left()
    print(g.gameboard)
    g.set_selected_pad(8)
    g.move_left()
    print(g.gameboard)

    # Test has won
    g = Game(3)
    print(g.gameboard)
    print(g.has_won())
    g.set_selected_pad(0)
    g.move_left()
    print(g.has_won())
    g.set_selected_pad(2)
    g.move_right()
    print(g.gameboard)
    print(g.has_won())
