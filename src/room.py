from src.guest import *
from src.song import *
from src.group import *

class Room:

    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.customer = []
        self.song = []
    
    def add_guest(self, guest):
        self.customer.append(guest)
    
    def remove_guest(self, guest):
        self.customer.remove(guest)
    
    def add_song(self, song):
        self.song.append(song)
    
    def remove_song(self, song):
        self.song.remove(song)
    
    # def group_room_check(self, the_group, the_room):
    #     group_size = Group.check_group_size(the_group)
    #     the_room = self.capacity
    #     if group_size <= the_room:
    #         return "Go On In"
    #     else:
    #         return "Sorry, you guys won't fit."