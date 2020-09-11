import unittest
from src.guest import *
from src.room import *
from src.song import *
from src.group import *
from src.kiosk import *

class TestRoom(unittest.TestCase):
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

    def test_room_has_name(self):
        self.assertEqual("Blue", self.room_1.name)
    
    def test_room_has_capacity(self):
        self.assertEqual(4, self.room_1.capacity)
    
    def test_room_has_price(self):
        self.assertEqual(50, self.room_1.price)
    
    #add guest to room
    def test_add_guest_to_room(self):
        self.room_1.add_guest(self.guest_1)
        self.assertEqual(1, len(self.room_1.customer))
    
    #remove guest from room
    def test_remove_guest_from_room(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.remove_guest(self.guest_1)
        self.assertEqual(0, len(self.room_1.customer))

    #add song to room
    def test_add_song_to_room(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1, len(self.room_1.song))
    
    #remove song from room
    def test_remove_song_from_room(self):
        self.room_1.add_song(self.song_1)
        self.room_1.remove_song(self.song_1)
        self.assertEqual(0, len(self.room_1.song))
