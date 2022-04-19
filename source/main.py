from froggame.game import Game
from froggame.leaderboard import Leaderboard

WANT_GUI = True

if __name__ == "__main__":
    if WANT_GUI:
        from gui.app import Application

        app = Application()
        app.mainloop()

    frog_game = Game(num_spaces=6)
    print(frog_game)
