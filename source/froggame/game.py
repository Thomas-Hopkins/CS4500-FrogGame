class Game:
    """
    Stores the gameboard data and handles all game logic.
    """

    def __init__(self, num_spaces: int) -> None:
        # TODO: build a gameboard of N spaces with a frog initially on each space
        pass

    def set_selected_space(self, index: int) -> None:
        # TODO: This will be called by the user interface when clicking on a frog/space. This will set the selected space
        # in the game, so that we can move all frogs on it with move_right/move_left
        pass

    def move_right(self) -> None:
        # TODO: Moves all frogs on the selected space right by N spaces if there is enough room on the board. N is
        # determined by how many frogs are on the selected space
        pass

    def move_left(self) -> None:
        # TODO: Moves all frogs on the selected space left by N spaces if there is enough room on the board. N is
        # determined by how many frogs are on the selected space
        pass

    def has_won(self) -> bool:
        # When called, returns true if game is won and false if game has not been won.
        pass

    def __repr__(self) -> str:
        return "TODO: return string representation of gameboard here for debugging purposes"
