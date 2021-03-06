"""
User facing strings should be defined here and referenced by variable as needed
"""

VERSION_LABEL = "Version"
LANGUAGE_LABEL = "Language:"
OPTIONS_PANEL = "Options"
DARK_OPTION = "Dark Mode"
GAME_TITLE = "Frog Game"
PLAY_BUTTON = "Play Game"
HIGHSCORES_BUTTON = "High Scores"
GAME_COPYRIGHT = "© 2022 Pythonic Four"
THEME_COPYRIGHT = "© 2021 rdbende"
THEME_NAME = "Sun-Valley-ttk-theme"
LEADERBOARD_TITLE = "High Scores"
MAIN_MENU_BUTTON = "Return to Main Menu"
BACK_BUTTON = "Go Back"
PAUSE_BUTTON = "Pause Game"
UNPAUSE_BUTTON = "Unpause Game"
TIMER_LABEL = "Timer: "
PAUSED_TEXT = "PAUSED"
START_BUTTON = "Start Game"
QUIT_MESSAGE = "Are you sure you want to quit?"
NUM_FROGS_LABEL = "Number of Frogs:"
HOWTO_SHORT_LABEL = (
    "To win, get all frogs on the same lilypad! Watch out though, frogs on the same space jump together. "
    + "Each frog on the lilypad adds one jump to the total number of jumps they ALL will make. You can only jump frogs "
    + "to a lilypad that already has frogs."
)
HINT_LABEL = "HINT: The more frogs, the higher your score, but the harder the game!"
RELOAD_APP = "Reloading Application"
RELOAD_APP_MSG = (
    "This change requires an application reload. Do you wish to reload now?"
)
WIN_LABEL = "YOU WIN!"
LOST_LABEL = "Game Over."
SCORE_NAME_LABEL = "Enter your name:"
SAVE_SCORE_BTN = "Save Score"
HELP_TITLE = "How to Play Frog Game"
HELP_MOVE_SUBTITLE = "Frog Movement"
HELP_MOVEMENT = (
    "Frogs can move either left or right. To move a frog click it with the mouse. Then click the right or left "
    + "buttons to move it right or left! ALL frogs on that space will follow with the first frog.\n\n"
    + "The number of frogs on the selected frog's space determines how many spaces the frogs will move.\n\n"
    + "Finally, frogs can only jump to spaces which already have frogs on them, they like to be with their frog friends."
)
HELP_HINT_SUBTITLE = "Tips & Hints"
HELP_HINTSTIPS = (
    "Getting higher scores in this game is best done through playing with a higher number of frogs.\n\n"
    + "You might notice though, its pretty hard to solve this game when you play with a high number of frogs without getting"
    + "some frogs stuck!\n\n"
    + "Did you know that every size board is able to be solved though?!\n\n"
    + "Thats right! Every board is able to be solved, what's even cooler is higher number boards can be solved in the exact same "
    + "method as some of the lower number ones!\n\n"
    + "For example, if you know how to solve the 3 frog board... You should be able to apply the same method to: 6, 9, 12, 15, 18, "
    + "21, ... wait... do you see the pattern? Its counting by three!\n\n"
    + "Solving any of these boards involves dividing the board up into groups of 3 frogs, and solving each of those the same way you "
    + "solved the simple 3 frog board. Move the 1st frog right to the center, and the 3rd frog left to the center. Once you've done "
    + "that, you can start combining all of them together.\n\n"
    + "The easiest way to combine them together is to now divide the board up into the next multiple of 3, so 6! Move your groups of "
    + "frogs to every sixth space. If you have a bigger board, go to the next multiple until you can finally combine them all together.\n\n"
    + "Can you figure out the trick for multiples of 4 boards? (4, 8, 12, 17, ...) HINT: It's very similar to the threes!\n\n"
    + "What about prime numbers?? (Numbers that aren't able to be broken up into anything but 1 and itself) 7 is a good board to try this with!"
)
GIVEUP_TITLE = "Give up?"
GIVEUP_MESSAGE = "We've detected this game may be unbeatable in it's current state.\nDo you want to give up?"

ARROW_LEFT = "<< "
ARROW_RIGHT = " >>"

WELCOME_SCREEN = "Main Menu"
GAMEBOARD_SCREEN = "Game"
LEADERBOARD_SCREEN = "High Scores"
HELP_SCREEN = "Help"
