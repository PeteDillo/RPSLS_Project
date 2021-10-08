from human import Human 
from ai import AI
class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        self.round_count = 1
        
    def round_outcome(self):
        if self.player_one.choice == self.player_two.choice:
            print("Both players selected {self.player_one.choice}. You tied.")
        elif self.player_one.choice == "rock":
            if self.player_two.choice == "scissors":
                print("Rock crushes scissors {self.player_one} wins this round")
                self.player_one.score += 1