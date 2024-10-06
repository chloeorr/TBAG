
import random

class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None #don't want every character to say the same thing so give None
    
    def describe(self):
        print(f"{self.name} is in this room.")
        print(f"{self.name} is {self.description}")

    def set_conversation(self, conversation):
        self.conversation = conversation 

    def talk(self):
        if self.conversation is not None:
            print(f"{self.name} says: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")

    
class Ally(Character):
    def __init__(self, char_name, char_description, riddle, answer, key):
        super().__init__(char_name, char_description)
        self.riddle = riddle
        self.answer = answer.lower()  # Store answer in lowercase for easier matching
        self.key = key

    def give_riddle(self):
        print(f"{self.name} has a riddle for you: {self.riddle}")
        player_answer = input("What's your answer? ").strip().lower()
        if player_answer == self.answer:
            print("Correct! You've earned a key.")
            return self.key
        else:
            print("Incorrect answer! Try again next time.")
            return None

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.power_item = None
    
    def get_power_item(self):
        return self.power_item
    
    def set_power_item(self, steal_item):
        self.power_item = steal_item

    def get_weakness(self):
        return self.weakness
    
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def fight(self, combat_item):
        if combat_item.lower() == self.weakness: #adding .lower() applies to all items and execution 
            print(f"You fought {self.name} off with the {combat_item}!")
            return True #Pulls you out the method, you win the fight
            #Ememy will be removed
        else:
            print(f"{self.name} crushes you, puny adventurer.\n GAME OVER!")
            return False #Game needs to end

    def steal(self, steal_item):
        print(f"{self.name} wants to see a magic trick.")
        diceroll = input("Enter to roll the dice:")
        steal_item = self.power_item
        diceroll = random.randint(1,6)
        if diceroll == 5:
            print(f"You rolled {diceroll}. Well done! You successfully stole {steal_item} from {self.name}.")
        else: 
            print(f"You rolled {diceroll}. Uh Oh! You FAILED to steal {steal_item} from {self.name}. \n {self.name} is mad. RUN!")