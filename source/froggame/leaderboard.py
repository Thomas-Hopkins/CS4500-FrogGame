from os.path import exists as file_exists
import json
import os
import unittest

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

        with open(self.file_path, "w") as json_file:
            json.dump(self.leader_data, json_file)
            json_file.close()

    def get_top_ten(self) -> list:
        view_list = []
        i = 0
        for i in range(len(self.leader_data)):
            view_list.append(self.leader_data[i])
            view_list[i]["time"] *= -1
            view_list[i]["frogs"] *= -1

        return view_list


class TestLeaderboard(unittest.TestCase):
    lb = Leaderboard()
    lb.file_path = "Unit_test_highscore.json"

    # need to set leader data to blank list so existing highscores don't get loaded and mess up tests
    nl = []
    lb.leader_data = nl

    def test_init(self):
        self.assertIsInstance(self.lb, Leaderboard)

    def test_add_score(self):

        self.lb.add_score("wyatt", 1, 3, 3, 4)
        self.lb.add_score("thomas", 7, 8, 9, 10)
        self.lb.add_score("Nilima", 2, 3, 4, 5)
        self.lb.add_score("noah", 3, 4, 5, 6)
        # edge case where score is equal but time is less
        self.lb.add_score("thomas", 11, 11, 9, 11)
        # edge case where score and time is equal but frogs is higher then another score
        self.lb.add_score("thomas", 7, 8, 9, 12)

        player_d = {
            "name": "thomas",
            "time": 7 * (-1),
            "moves": 8,
            "stacked": 9,
            "frogs": 10 * (-1),
        }
        palyer_d2 = {
            "name": "wyatt",
            "time": 1 * (-1),
            "moves": 3,
            "stacked": 3,
            "frogs": 4 * (-1),
        }
        self.assertEqual(len(self.lb.leader_data), 6)
        # checks that sorting is done properly
        self.assertEqual(self.lb.leader_data[0], player_d)
        self.assertEqual(self.lb.leader_data[5], palyer_d2)

    def test_get_top_ten(self):
        ld = self.lb.get_top_ten()
        i = 0
        for i in range(len(self.lb.leader_data)):
            self.assertGreaterEqual(ld[i]["time"], 0)
            self.assertGreaterEqual(ld[i]["frogs"], 0)

        os.remove(self.lb.file_path)


if __name__ == "__main__":
    unittest.main()


