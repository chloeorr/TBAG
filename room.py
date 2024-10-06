class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None #None is own unique data type, has a value of 'None'. Do not need to provide in constructor.
        self.linked_rooms = {} #contains rooms and links to each other, south, north etc 
        self.characters = [] 

    def get_description(self):
        return self.description
    
    def set_description(self, room_description):
        self.description = room_description #overwriting 'None'
    
    def describe(self):
        print(self.description)
    
    def set_name(self, room_name):
        self.name = room_name
    
    def get_name(self):
        return self.name

    def set_character(self, new_character):
        self.characters.append(new_character)  # Append character to the list

    def get_character(self):
        return self.characters  # Return the list of characters

    def remove_character(self, character):
        if character in self.characters:
            self.characters.remove(character) 
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link #access dictionary

    def get_details(self):
        print(f"You are in the {self.name}.")
        print("-------------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction] #for each directions exist in get linked rooms dictionary it will print attached room. 
            print(f"The {room.get_name()} is {direction}.")
    
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way!")
            return self