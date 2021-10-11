from human import Human 
from ai import AI
import random

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        
    
    def display_rule(self):
        print(
            """Rule #1: Select a gesture and battle against your opponet"""
            """Rule #2: Certain gestures beat others here is the power scaling"""
            """Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock"""
            """Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock"""
            """Rule #3: No points for ties""")
    
    def select_game_mode(self):
        game_mode_one = 1
        game_mode_two = 2
        select = int(input("Which game mode would you like to play? \n Press '1' to play Human vs AI. \n Press '2' to play Human vs Human "))
        if select != int and select < 1 and select > 2:
            self.select_game_mode()
        if select == game_mode_one:
            self.player_two = AI()
        elif select == game_mode_two:
            self.player_two = Human()
            
    

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


    def run_game(self):
        print("Welcome to RPSLS!")                                      # welcome
        self.display_rules()
        self.select_game_mode()                                         # select game mode
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.gesture_select()                            # player_one choose gesture
            self.player_two.gesture_select()                            # player_two choose gesture
            self.round_outcome()                                        # run round outcome
            print(f"Player one's score is: {self.player_one.score}")
            print(f"Player two's score is: {self.player_two.score}")                                    # print player_one and player_two score
        self.winner()                                                   # display winner
        self.play_again()                                               # reprompt play again?


   
    def play_again(self):
        choice = int(input("Do you want to play again? \n Press '1' for yes. \n Press '2' for no"))
        if choice == 1:
            self.run_game()
        else:
            pass


    def validation(self, choice):
        if choice != int:
            self.validation
        elif choice < 1 or choice > 5:
            self.validation
        else:
            pass
        