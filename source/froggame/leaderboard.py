class Leaderboard:
    """
    Loads and stores leaderboard data.
    """

    def __init__(self) -> None:
        # TODO: load data in from leaderboard file and store it in this class
        pass

    def add_score(
        self, player_name: str, time_played: int, num_moves: int, frogs_stacked: int
    ) -> None:
        # TODO: Save score in leaderboard file
        pass

    def get_top_ten(self) -> list:
        # TODO: return a list (or dict), of the top 10 players with their scores
        pass
