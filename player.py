from random import choice
from getpass import getpass


class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = ""
        self.gesture_list = ["rock","paper","scissors","lizard","spock"]


    def gesture_select(self):
        print("Choose your gesture:")
        index = 0
        for gesture in self.gesture_list:
            print(f"Press {index} for {gesture}")
            index += 1
        player_choice = getpass("Insert a number: ")
        valid_player_choice = self.validation(player_choice)
        self.choice = self.gesture_list[valid_player_choice]
        print(f"{self.name} selects {self.choice}!")


    def validation(self, choice):
        if choice.isnumeric() == False or int(choice) < 0 or int(choice) > 4:
            choice = self.reselector()
            return int(choice)
        else: 
            return int(choice)
            

    def reselector(self):
        choice = -1
        while int(choice) < 0 or int(choice) > 4:
            print("Invalid input, please choose another gesture:")
            index = 0
            for gesture in self.gesture_list:
                print(f"Press {index} for {gesture}")
                index += 1
            choice = input()
        return int(choice)
        