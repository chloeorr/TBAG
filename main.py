from room import Room
from character import Enemy
from character import Ally
import sys

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
exitroom = Room("Hidden Exit")

keys_collected = set()  # Set to hold collected keys
required_keys = {"key1", "key2", "key3"}  # Replace these with your specific keys

#Enemy 1 Dave in Dining Hall
dave =Enemy("Dave", "a smelly zombie")
dave.set_conversation("GRUUUUG, I'm Dave. I promise I won't eat your brains out....")
dave.set_weakness("piano") #create a clue for player to guess his weakness or make it the same clue as the riddle
dave.set_power_item("a 1930's locket")
dining_hall.set_character(dave) #putting dave in the dining hall


#Enemy 2 Mark in Kitchen 
mark = Enemy("Mark", "a green blob")
mark.set_conversation("Wobble, wobble. blurrrgh. My slime trail is on your shoe. Done eat it, it will kill you.") #Make mark's slime a superpower so the player holds an invisibiliy cloack or soemthing 
mark.set_weakness("darkness")
mark.set_power_item("a hammer")
kitchen.set_character(mark)

#Enemy 3 Drac in Ballroom 
drac = Enemy("Drac", "a vampire")
mark.set_conversation("Wobble, wobble. blurrrgh. My slime trail is on your shoe. Done eat it, it will kill you.") #Make mark's slime a superpower so the player holds an invisibiliy cloack or soemthing 
mark.set_weakness("candle")
mark.set_power_item("an urn")
ballroom.set_character(drac)

#Ally 1 in the Dining Hall (Dave)
susan = Ally("Susan", "a friendly wolf", "What has keys but can't open locks?", "piano", "key1")
susan.set_conversation("WOOF WOOOF, WHO ARE YOU?") #Make mark's slime a superpower so the player holds an invisibiliy cloack or soemthing 
dining_hall.set_character(susan)

#Ally 2 in the Kitchen (Mark)
paul = Ally("Paul", "an alien", "The more of this there is, the less you see. What is it?", "darkness", "key2")
paul.set_conversation("Hey, I'm Paul, I come from the STAAARS. But I've been trapped in this house for 20 years.") #Make mark's slime a superpower so the player holds an invisibiliy cloack or soemthing 
ballroom.set_character(paul)

#Ally 3 in the Ballrooom (Drac)
spikey = Ally("Spikey", "a wise caterpillar", "I’m tall when I’m young, and I’m short when I’m old. What am I?", "candle", "key3")
spikey.set_conversation("Ah my child what can I assist you with?") #Make mark's slime a superpower so the player holds an invisibiliy cloack or soemthing 
kitchen.set_character(spikey)

#Room Description 
kitchen.set_description("A dank and dirty room full of flies.")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate golden decor")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
exitroom.link_room(ballroom, "south")

#Main execution loop
print("Welcome to Annex3. You are trapped in the Annex with 3 different rooms. \n\nDining Hall \nKitchen \nBallroom \n \nTo navigate throught them you must move 'north', 'south', 'west' or 'east'. \n \nBeware whilst you may bump into some allies, you may also run into some enemies who want to trick you. Find their weakness and kill them to avoid being killed. (Your allies will help you gain a key and find your enemies weakness.) \n OPTIONS: \n 1. talk \n 2. fight \n 3. steal \n 4. unlock \n 5. exit ")
command = input("Press enter to continue.")

current_room = dining_hall

while True:
    print("\n")
    current_room.get_details()
    inhabitants = current_room.get_character()
    if inhabitants:
        for inhabitant in inhabitants:
            inhabitant.describe()
    else:
        print("The room is empty.")

    command = input("Please naviagte to another room or interact with a character > ").lower().strip()

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitants:
            for inhabitant in inhabitants:
                if isinstance(inhabitant, Ally):
                    key = inhabitant.give_riddle()
                    if key:
                        keys_collected.add(key)
                else:
                    inhabitant.talk()
                    command = input("Reply: ")

        else:
            print("Sorry mate, you'd be speaking to yourself in this room.")
    elif command == "fight":
        if inhabitants:
            for inhabitant in inhabitants:
                if isinstance(inhabitant, Enemy):
                    print("What will you fight with?")
                    fight_with = input("Enter item here: ")
                    if inhabitant.fight(fight_with):
                        current_room.remove_character(inhabitant)  #Remove enemy if defeated.
                else:
                    sys.exit() #Game is exited as player is dead.
        
        else:
            print("There is no one to fight with in this room. Move into a different room.")
    elif command == "steal":
        if inhabitants: #becoems the item stolen but want it to be transfered to you 
            for inhabitant in inhabitants:
                if isinstance(inhabitant, Enemy):
                    steal_item = inhabitant.power_item 
                    inhabitant.steal(steal_item) #Create player Class to add stolen item to inventory
        else:
            print("There is no one to steal from in this room. Move into a different room.")
    elif command == "unlock" and current_room == ballroom:
        if required_keys.issubset(keys_collected):
            print("Congratulations! You have unlocked the exit with your keys and escaped!")
            break  # Exit the loop, end the game
        else:
            missing_keys = required_keys - keys_collected
            print(f"You don't have all the keys needed to unlock the exit. Missing keys: {', '.join(missing_keys)}")
        print("The exit room is now locked.")
    elif command in ["quit", "exit"]:
        print("Thanks for playing!")
        sys.exit() #Game is exited
    else: 
        print("Invalid Option.")

#Given 3 clues to create a riddle. Guess the riddle. Opens the exit door to escape, south from ballroom. Lock rooms to unlock exit after finding all clues. 
