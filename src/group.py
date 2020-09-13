from src.guest import * 

class Group:
    def __init__(self, name):
        self.name = name
        self.group_amount = 0
        self.guests = []
        self.collective_money = 0
    
    def add_guest_to_group(self, guest):
        self.guests.append(guest)
        self.group_amount += 1
        self.collective_money += guest.wallet

    def remove_guest_from_group(self, guest):
        self.guests.remove(guest)
        self.group_amount -= 1
        self.collective_money -= guest.wallet
    
    def check_group_size(self, the_group):
        group_size = len(the_group.guests)
        return group_size 
    
    def reduce_group_wallet(self, room_price):
        self.collective_money -= room_price.price
    
    

    
