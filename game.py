class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        print("Welcome to Pig!")
        current_player = self.player1

        while self.player1.score < 100 and self.player2.score < 100:
            print(f"\nIt's {current_player.name}'s turn.")
            current_player.take_turn()

            if current_player.score >= 100:
                print(f"{current_player.name} wins!")
                break

            # Switch player
            current_player = self.player2 if current_player == self.player1 else self.player1
