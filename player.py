import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def take_turn(self):
        turn_total = 0
        while True:
            roll = random.randint(1, 6)
            print(f"{self.name} rolled a {roll}")

            if roll == 1:
                print(f"{self.name} loses turn points.")
                turn_total = 0
                break

            turn_total += roll
            print(f"{self.name}'s turn total: {turn_total}")

            decision = input("Roll again? (y/n): ").lower()
            if decision != 'y':
                break
        self.score += turn_total
        print(f"{self.name}'s total score: {self.score}\n")


class ComputerPlayer(Player):
    def take_turn(self):
        turn_total = 0
        while True:
            roll = random.randint(1, 6)
            print(f"{self.name} (computer) rolled a {roll}")

            if roll == 1:
                print(f"{self.name} loses turn points.")
                turn_total = 0
                break

            turn_total += roll
            # Computer strategy
            hold_threshold = min(25, 100 - self.score)
            if turn_total >= hold_threshold:
                print(f"{self.name} decides to hold.")
                break
        self.score += turn_total
        print(f"{self.name}'s total score: {self.score}\n")
