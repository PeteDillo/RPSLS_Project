from human import Human 
from ai import AI
import random

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        self.round_count = 1
        
    
    def display_rule(self):
        print(
            """Rule #1: Select a gesture and battle against your opponet"""
            """Rule #2: Certain gestures beat others here is the power scaling"""
            """Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock"""
            """Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock"""
            """Rule #3: No points for ties""")
    
    def select_game_mode(self):
        game_mode_one = "Human vs Human" #validation
        game_mode_two = "Human vs AI"
        select = input("Which game mode would you like to play? ")
        print("Human vs Human \n Human vs AI ")
        if select == game_mode_one:
            self.player_two = Human()
        elif select == game_mode_two:
            self.player_two = AI()
            
    

    def round_outcome(self):
        if self.player_one.choice == self.player_two.choice:
            print(f"Both players selected {self.player_one.choice}. You tied.")
        elif self.player_one.choice == "rock":
            if self.player_two.choice == "scissors":
                print(f"Rock crushes scissors {self.player_one} wins this round")
                self.player_one.score += 1
            elif self.player_two.choice == "lizard":
                print(f"Rock crushes lizard! {self.player_one.name} wins this round!")
                self.player_one.score += 1
            elif self.player_two.choice == "spock":
                print(f"Spock vaporizes rock! {self.player_two.name} wins this round.")
                self.player_two.score += 1
            elif self.player_two.choice == "paper":
                print(f"Paper covers rock! {self.player_two.name} wins this round.") 
                self.player_two.score += 1   
        elif self.player_one.choice == "paper":
            if self.player_two.choice == "rock":
                print(f"Paper covers rock! {self.player_one.name} wins this round!")
                self.player_one.score += 1
            elif self.player_two.choice == "spock":
                print(f"Paper disproves spock! {self.player_one.name} wins this round!")
                self.player_one.score += 1
            elif self.player_two.choice == "lizard":
                print(f"Lizard eats paper! {self.player_two.name} wins this round.")
                self.player_two.score += 1
            elif self.player_two.choice == "scissors":
                print(f"Scissors cuts paper! {self.player_two.name} wins this round.")
                self.player_two.score += 1
        elif self.player_one.choice == "scissors":
            if self.player_two.choice == " ":
                pass

    def display_winners(self):
        if (self.player_one.score == 2):
            print(f"{self.player_one.name} wins!")
        elif (self.player_two.score == 2):
            print(f"{self.player_two.name} wins!")             