from player import Player, ComputerPlayer

class PlayerFactory:
    @staticmethod
    def create_player(player_type, name):
        if player_type.lower() == "human":
            return Player(name)
        elif player_type.lower() == "computer":
            return ComputerPlayer(name)
        else:
            raise ValueError("Invalid player type. Choose 'human' or 'computer'.")
