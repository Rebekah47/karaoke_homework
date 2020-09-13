import unittest
from src.guest import *
from src.room import *
from src.song import *
from src.group import *
from src.kiosk import *

class TestGroup(unittest.TestCase):
    def setUp(self):

        self.kiosk = Kiosk("Sing Out", 500)

        self.group_1 = Group("One")
        self.group_2 = Group("Two")

        self.room_1 = Room("Blue", 4, 50)
        self.room_2 = Room("Red", 2, 40)
        self.room_3 = Room("Green", 1, 30)

        self.song_1 = Song("Yesterday", "The Beatles", 2)
        self.song_2 = Song("We Will Rock You", "Queen", 2)
        self.song_3 = Song("I Would Do Anything For Love", "Meatloaf", 2)

        self.guest_1 = Guest("Adam", 28, 60,)
        self.guest_2 = Guest("Michael", 26, 50)
        self.guest_3 = Guest("Andrew", 22, 30)

    def test_group_has_name(self):
        self.assertEqual("One", self.group_1.name)

    #add customer to group
    def test_add_customer_to_group(self):
        self.group_1.add_guest_to_group(self.guest_1)
        self.group_1.add_guest_to_group(self.guest_2)
        self.assertEqual(2, len(self.group_1.guests))
        self.assertEqual(2, self.group_1.group_amount)
        self.assertEqual(110, self.group_1.collective_money)

    #remove customer from group
    def test_remove_customer_from_group(self):
        self.group_1.add_guest_to_group(self.guest_1)
        self.group_1.remove_guest_from_group(self.guest_1)
        self.assertEqual(0, len(self.group_1.guests))
        self.assertEqual(0, self.group_1.group_amount)
        self.assertEqual(0, self.group_1.collective_money)
    
    #check size of group
    def test_group_size(self):
        self.group_1.add_guest_to_group(self.guest_1)
        self.assertEqual(1, self.group_1.check_group_size(self.group_1))
    
    def test_reduce_group_wallet(self):
        self.group_1.add_guest_to_group(self.guest_1)
        self.group_1.add_guest_to_group(self.guest_2)
        self.group_1.reduce_group_wallet(self.room_1)
        self.assertEqual(60, self.group_1.collective_money)


