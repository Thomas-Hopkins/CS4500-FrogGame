from os.path import exists as file_exists
import json


class Leaderboard:
    """
    Loads and stores leaderboard data.
    """

    file_path = "high-scores.json"

    def __init__(self) -> None:
        print(Leaderboard.file_path)
        # check if file exists, open to read if it does.
        if file_exists(Leaderboard.file_path):
            with open(Leaderboard.file_path, "r") as json_file:
                try:
                    self.leader_data = json.loads(json_file.read())
                except:
                    # In-case the file is malformed json, fallback to empty list
                    self.leader_data = []
                json_file.close()
        else:
            self.leader_data = []

    def add_score(
        self,
        player_name: str,
        time_played: int,
        num_moves: int,
        frogs_stacked: int,
        num_frogs: int,
    ) -> None:

        player_dict = {
            "name": player_name,
            "time": time_played * (-1),
            "moves": num_moves,
            "stacked": frogs_stacked,
            "frogs": num_frogs * (-1),
        }

        self.leader_data.append(player_dict)
        leader_count = len([i for i in self.leader_data if isinstance(i, dict)])

        self.leader_data = sorted(
            self.leader_data,
            key=lambda i: (i["stacked"], i["time"], i["frogs"], i["moves"]),
            reverse=True,
        )

        if leader_count > 10:
            # remove lowest score from list
            del self.leader_data[10]

        with open(Leaderboard.file_path, "w") as json_file:
            json.dump(self.leader_data, json_file)
            json_file.close()

    def get_top_ten(self) -> list:
        return self.leader_data


import unittest


class Test_leaderboard(unittest.TestCase):
    def test_init(self):
        lb = Leaderboard()
        self.assertIsInstance(lb, Leaderboard)

    def test_add_score(self):
        lb = Leaderboard()
        lb.add_score("wyatt", 1, 2, 3, 4)
        lb.add_score("thomas", 7, 8, 9, 10)
        lb.add_score("Nilima", 2, 3, 4, 5)
        lb.add_score("noah", 3, 4, 5, 6)
        # edge case where score is equal but time is less
        lb.add_score("thomas", 11, 11, 9, 11)
        # edge case where score and time is equal but frogs is higher then another score

        lb.add_score("thomas", 7, 8, 9, 12)

        player_d = {
            "name": "thomas",
            "time": 7 * (-1),
            "moves": 8,
            "stacked": 9,
            "frogs": 10 * (-1),
        }
        # checks that sorting is done properly
        self.assertEqual(lb.leader_data[0], player_d)


if __name__ == "__main__":
    unittest.main()
