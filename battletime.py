from human import Human 
from ai import AI
import random

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        self.ai = AI()
        self.round_count = 1
        
    def round_outcome(self):
        if self.player_one.choice == self.player_two.choice:
            print("Both players selected {self.player_one.choice}. You tied.")
        elif self.player_one.choice == "rock":
            if self.player_two.choice == "scissors":
                print("Rock crushes scissors {self.player_one} wins this round")
                self.player_one.score += 1

    def display_rule(self):
        print(
            """Rule #1: Select a gesture and battle against your opponet"""
            """Rule #2: Certain gestures beat others here is the power scaling"""
            """Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock"""
            """Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock"""
            """Rule #3: No points for ties""")
    
    def select_game_mode(self):
        game_mode_one = "Human vs Human"
        game_mode_two = "Human vs AI"
        select = input("Which game mode would you like to play? ")
        print("Human vs Human \n Human vs AI ")
        if select == game_mode_one:
            self.human_vs_human
        elif select == game_mode_two:
            self.human_vs_AI
            
    def human_vs_human(self, player_one, player_two):
        self.goes_first()
        play = True
        while self.round_count <= 0 :
            play = False
            return play
            pass

    def human_vs_AI(self, player_one, ai):
        self.goes_first()
    
    
    def goes_first(self, player_one, player_two):
        goes_first = random.choice(player_one, player_two)
        return goes_first
