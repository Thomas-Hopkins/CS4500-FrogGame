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
                self.leader_data = json.loads(json_file.read())
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
            "frogs": num_frogs,
        }

        self.leader_data.append(player_dict)
        leader_count = len([i for i in self.leader_data if isinstance(i, dict)])
        # print("laeader count ", leader_count)

        self.leader_data = sorted(self.leader_data, key=lambda i: (i['time'], i['stacked']),reverse=True)

        if leader_count > 10:
            # remove lowest score from list
            del self.leader_data[10]


        with open(Leaderboard.file_path, "w") as json_file:
            json.dump(self.leader_data, json_file)
            json_file.close()

    def get_top_ten(self) -> list:
        return self.leader_data





