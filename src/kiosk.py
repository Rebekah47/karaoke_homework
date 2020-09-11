from src.guest import *
from src.room import *
from src.song import *
from src.group import *

class Kiosk:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.rooms_available = 3
        self.room_list = []

    def increase_till(self, amount):
        self.till += amount
    
    def put_room_in_use(self, the_room):
            self.rooms_available -= 1
    
    def add_room_to_list(self, the_room):
        self.room_list.append(the_room)
    
    def book_room(self, the_room):
        self.put_room_in_use(the_room)
        self.add_room_to_list(the_room)
    
    def check_if_rooms_available(self):
        if self.rooms_available > 0:
            return "Free"
        else:
            return "No Rooms Available"

    
    # def check_free_room(self, the_room):
    #     for the_room in self.rooms:
    #         if len(Room.customer) == 0:
    #             return True

    #if len(the_room.customer) == 0:
