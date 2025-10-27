import argparse
from player_factory import PlayerFactory
from game import Game
from timed_game_proxy import TimedGameProxy

def main():
    parser = argparse.ArgumentParser(description="Play the Pig game!")
    parser.add_argument("--player1", choices=["human", "computer"], required=True)
    parser.add_argument("--player2", choices=["human", "computer"], required=True)
    parser.add_argument("--timed", action="store_true", help="Enable timed mode (1 minute limit)")

    args = parser.parse_args()

    player1 = PlayerFactory.create_player(args.player1, "Player 1")
    player2 = PlayerFactory.create_player(args.player2, "Player 2")

    game = Game(player1, player2)

    if args.timed:
        proxy = TimedGameProxy(game)
        proxy.play()
    else:
        game.play()

if __name__ == "__main__":
    main()
