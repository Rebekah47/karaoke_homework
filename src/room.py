from src.guest import *
from src.song import *

class Room:

    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.customer = []
        self.song = []
    
    def add_guest(self, guest):
        self.customer.append(guest)