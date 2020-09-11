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