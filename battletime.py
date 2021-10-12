from human import Human 
from ai import AI
import random
import os

class Game:
    def __init__(self):
        self.player_one = Human("")
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
        select = int(input("Which game mode would you like to play? \n Press '1' to play Human vs AI. \n Press '2' to play Human vs Human. \n "))
        if select != int and select < 1 and select > 2:
            self.select_game_mode()
        elif select == game_mode_one:
            self.player_one = Human(input("Player one, Please enter a name: "))
            self.player_two = AI('Siri')
            print(f"{self.player_one.name} VS. {self.player_two.name}")
        elif select == game_mode_two:
            self.player_one = Human(input("player one, Please enter a name: "))
            self.player_two = Human(input('Player two, Please enter a name: '))
            print(f"{self.player_one.name} VS. {self.player_two.name}")
            
    

    def round_outcome(self):
        if self.player_one.choice == self.player_two.choice:
            print(f"Both players selected {self.player_one.choice}. You tied.")
        elif self.player_one.choice == "rock" :
            if self.player_two.choice == "scissors" or self.player_two.choice == "lizard":
                print(f"{self.player_one.choice} crushes {self.player_two.choice}, {self.player_one.name} wins this round")
                self.player_one.score += 1
            elif self.player_two.choice == "spock" or self.player_two.choice == "paper":
                print(f"{self.player_two.choice} vaporizes {self.player_one.choice}! {self.player_two.name} wins this round.")
                self.player_two.score += 1  
        elif self.player_one.choice == "paper":
            if self.player_two.choice == "rock" or self.player_two.choice == "spock":
                print(f"{self.player_one.choice} covers {self.player_two.choice}! {self.player_one.name} wins this round!")
                self.player_one.score += 1
            elif self.player_two.choice == "lizard" or self.player_two.choice == "scissors":
                print(f"{self.player_two.choice} eats {self.player_one.choice}! {self.player_two.name} wins this round.")
                self.player_two.score += 1
        elif self.player_one.choice == "scissors":
            if self.player_two.choice == "paper" or self.player_two.choice == "lizard":
                print(f"{self.player_one.choice} cuts {self.player_two.choice}! {self.player_one.name} wins this round!")
                self.player_one.score += 1
            elif self.player_two.choice == "spock" or self.player_two.choice == "rock":
                print(f"{self.player_two.choice} smashes {self.player_one.choice}! {self.player_two.name} wins this round.")
                self.player_two.score += 1
        elif self.player_one.choice == "lizard":
            if self.player_two.choice == "spock" or self.player_two.choice == "paper":
                print(f"{self.player_one.choice} poisons {self.player_two.choice}! {self.player_one.name} wins this round!")
                self.player_one.score += 1
            elif self.player_two.choice == "rock" or self.player_two.choice == "scissors":
                print(f"{self.player_two.choice} crushes {self.player_one.choice}! {self.player_two.name} wins this round.")
                self.player_two.score += 1
        elif self.player_one.choice == "spock":
            if self.player_two.choice == "scissors" or self.player_two.choice == "rock":
                print(f"{self.player_one.choice} smashes {self.player_two.choice}! {self.player_one.name} wins this round!")
                self.player_one.score += 1
            elif self.player_two.choice == "paper" or self.player_two.choice == "lizard":
                print(f"{self.player_two.choice} disaproves {self.player_one.choice}! {self.player_two.name} wins this round.")
                self.player_two.score += 1
        
                
    
    def display_winners(self):
        if (self.player_one.score == 2):
            print(f"{self.player_one.name} wins!")
        elif (self.player_two.score == 2):
            print(f"{self.player_two.name} wins!")


    def run_game(self):
        print("Welcome to RPSLS!")                                               # welcome
        self.display_rule()
        self.select_game_mode()                                                  # select game mode
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.gesture_select()                                     # player_one choose gesture
            self.player_two.gesture_select()                                     # player_two choose gesture
            self.round_outcome()
            self.clearConsole()                                                 # run round outcome
            print(f"Player one's score is: {self.player_one.score}")
            print(f"Player two's score is: {self.player_two.score}")             # print player_one and player_two score
        self.display_winners()                                                   # display winner
        self.play_again()                                                        # reprompt play again?
        

   
    def play_again(self):
        self.player_one.score = 0
        self.player_two.score = 0
        choice = int(input("Do you want to play again? \nPress '1' for yes. \nPress '2' for no. \n"))
        if choice == 1:
            self.run_game()
        else:
            print("Thank you for playing RPSLS!")
            pass


    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

