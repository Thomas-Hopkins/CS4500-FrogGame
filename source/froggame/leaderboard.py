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
                print(self.leader_data)
                json_file.close()
        else:
            with open(Leaderboard.file_path, "w") as new_file:
                new_file.close()
                self.leader_data = []

        pass

    def add_score(
        self, player_name: str, time_played: int, num_moves: int, frogs_stacked: int
    ) -> None:

        player_dict = {
            "name": player_name,
            "time": time_played,
            "moves": num_moves,
            "stacked": frogs_stacked,
        }
        self.leader_data.append(player_dict)
        leader_count = len([i for i in self.leader_data if isinstance(i, dict)])
        # print("laeader count ", leader_count)
        if leader_count > 10:
            low_score = frogs_stacked
            index = leader_count - 1

            # TODO Change Deletion priority based on time or number of moves
            for z in range(leader_count):
                if self.leader_data[z]["stacked"] < low_score:
                    low_score = self.leader_data[z]["stacked"]
                    index = z
                elif (
                    self.leader_data[z]["stacked"] == low_score
                    and self.leader_data[z]["stacked"]
                    < self.leader_data[index]["stacked"]
                ):
                    index = z

            # print(self.leader_data)
            # remove lowest score from list
            del self.leader_data[index]

        # print(self.leader_data)

        with open(Leaderboard.file_path, "w") as json_file:
            json.dump(self.leader_data, json_file)
            json_file.close()

        # TODO: Save score in leaderboard file
        pass

    def get_top_ten(self) -> list:
        return self.leader_data
        pass


# 1AM - 3:30am logged this time on 4/19
# 45 min
# 8 -10AM
