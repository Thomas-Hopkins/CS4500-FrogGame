class Game:
    """
    Stores the gameboard data and handles all game logic.
    """

    def __init__(self, num_spaces: int, want_debug_prints: bool = False) -> None:
        """
        builds a gameboard of N spaces with a frog initially on each space
        """
        self.gameboard = [1 for x in range(int(num_spaces))]
        self.selected_pad = None
        self.__DEBUG_PRINTS = want_debug_prints

    def get_selected_pad(self) -> int:
        """
        Returns the currently selected pad. None if no selected.
        """
        return self.selected_pad

    def set_selected_pad(self, index: int) -> None:
        """
        This will be called by the user interface when clicking on a frog/space. This will set the selected space
        # in the game, so that we can move all frogs on it with move_right/move_left
        """
        self.selected_pad = index

    def move_left(self) -> int:
        """
        Moves all frogs on the selected space left by N spaces if there is enough room on the board. N is
        determined by how many frogs are on the selected space. Returns the resulting number of spaces moved.
        """
        if self.selected_pad is None:
            self.__debug_print(f"Move left error, no selected pad")
            return 0
        # Step 1: Decide the number of pads to jump
        pads_to_jump = self.gameboard[self.selected_pad]
        # Step 2: Ensure that the source & target pads are not empty
        if self.gameboard[self.selected_pad] < 1:
            err = f"Move left error!! Selected pad {self.selected_pad} is empty!!"
            self.__debug_print(err)
            return 0
        if pads_to_jump > self.selected_pad:
            err = f"Move left error!! Cannot jump {pads_to_jump} frogs to the right from position {self.selected_pad}!!"
            self.__debug_print(err)
            return 0
        if self.gameboard[self.selected_pad - pads_to_jump] < 1:
            err = f"Move left error!! Target pad cannot be empty!!"
            self.__debug_print(err)
            return 0
        # Step 3: Do the jump
        self.gameboard[self.selected_pad - pads_to_jump] += pads_to_jump
        self.gameboard[self.selected_pad] = 0
        self.__debug_print(
            f" -> Moved (right) frogs from pad {self.selected_pad} to {self.selected_pad - pads_to_jump}"
        )
        return pads_to_jump

    def move_right(self) -> int:
        """
        Moves all frogs on the selected space right by N spaces if there is enough room on the board. N is
        determined by how many frogs are on the selected space. Returns the resulting number of spaces moved.
        """
        if self.selected_pad is None:
            self.__debug_print(f"Move right error, no selected pad")
            return 0
        # Step 1: Decide the number of pads to jump
        pads_to_jump = self.gameboard[self.selected_pad]
        # Step 2: Ensure that the source & target pads are not empty
        if self.gameboard[self.selected_pad] < 1:
            err = f"Move right error!! Selected pad {self.selected_pad} is empty!!"
            self.__debug_print(err)
            return 0
        if pads_to_jump + self.selected_pad >= len(self.gameboard):
            err = f"Move right error!! Cannot jump {pads_to_jump} frogs to the left from position {self.selected_pad}!!"
            self.__debug_print(err)
            return 0
        if self.gameboard[pads_to_jump + self.selected_pad] < 1:
            err = f"Move right error!! Target pad cannot be empty!!"
            self.__debug_print(err)
            return 0
        # Step 3: Do the jump
        self.gameboard[pads_to_jump + self.selected_pad] += pads_to_jump
        self.gameboard[self.selected_pad] = 0
        self.__debug_print(
            f" -> Moved (right) frogs from pad {self.selected_pad} to {self.selected_pad - pads_to_jump}"
        )
        return pads_to_jump

    def has_deadlock(self) -> bool:
        """
        returns True if deadlock is detected and no valid moves remain
        returns False if there are still valid moves
        """
        board_spaces = len(self.gameboard)
        for i in range(board_spaces):
            # check if current tile has frog on it
            if self.gameboard[i] > 0:

                # if not out of bounds check move left
                if i - self.gameboard[i] >= 0:
                    # check if 1ile to left has frogs, aka valid jump
                    if (self.gameboard[i - self.gameboard[i]]) > 0:
                        return False

                # if not out of bounds check move right
                if i + self.gameboard[i] < board_spaces:
                    # check if tile to right has frogs, aka valid jump
                    if (self.gameboard[i - self.gameboard[i]]) > 0:
                        return False

        # no valid moves found, deadlock detected
        return True

    def has_won(self) -> bool:
        """
        When called, returns true if game is won and false if game has not been won.
        """
        pads_with_frogs = 0
        for i in range(len(self.gameboard)):
            if self.gameboard[i] > 0:
                pads_with_frogs += 1
        if pads_with_frogs == 1:
            return True

        return False

    def __debug_print(self, msg: str) -> None:
        if self.__DEBUG_PRINTS:
            print(msg)

    def __repr__(self) -> str:
        return f"gameboard: {str(self.gameboard)} selected: {self.selected_pad}"


if __name__ == "__main__":
    debug = False
    g = Game(10, want_debug_prints=debug)

    # Test move right method
    print(g)
    g.set_selected_pad(3)
    g.move_left()
    print(g)
    g.set_selected_pad(2)
    g.move_left()
    print(g)
    g.set_selected_pad(2)
    g.move_left()
    print(g)
    g.set_selected_pad(0)
    g.move_left()
    print(g)
    g.set_selected_pad(4)
    g.move_left()
    print(g)

    # Test move left method
    g.set_selected_pad(4)
    g.move_left()
    print(g)
    g.set_selected_pad(1)
    g.move_left()
    print(g)
    g.set_selected_pad(5)
    g.move_left()
    print(g)
    g.set_selected_pad(7)
    g.move_left()
    print(g)
    g.set_selected_pad(8)
    g.move_left()
    print(g)

    # Test has won
    g = Game(3, want_debug_prints=debug)
    print(g)
    print(g.has_won())
    g.set_selected_pad(0)
    g.move_left()
    print(g.has_won())
    g.set_selected_pad(2)
    g.move_left()
    print(g)
    print(g.has_won())
