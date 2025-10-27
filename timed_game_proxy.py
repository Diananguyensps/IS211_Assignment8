import time

class TimedGameProxy:
    def __init__(self, game):
        self._game = game
        self._start_time = time.time()

    def play(self):
        print("Starting Timed Game (1-minute limit)...")
        current_player = self._game.player1

        while True:
            if time.time() - self._start_time > 60:
                print("\nTime's up!")
                self._declare_winner()
                break

            print(f"\nIt's {current_player.name}'s turn.")
            current_player.take_turn()

            if current_player.score >= 100:
                print(f"{current_player.name} wins!")
                break

            current_player = (
                self._game.player2 if current_player == self._game.player1 else self._game.player1
            )

    def _declare_winner(self):
        if self._game.player1.score > self._game.player2.score:
            print(f"{self._game.player1.name} wins with {self._game.player1.score} points!")
        elif self._game.player2.score > self._game.player1.score:
            print(f"{self._game.player2.name} wins with {self._game.player2.score} points!")
        else:
            print("It's a tie!")
