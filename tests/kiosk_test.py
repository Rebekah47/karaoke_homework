import unittest
from src.guest import *
from src.room import *
from src.song import *
from src.group import *
from src.kiosk import *

class TestKiosk(unittest.TestCase):
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
    
    def test_kiosk_has_name(self):
        self.assertEqual("Sing Out", self.kiosk.name)
    
    def test_kiosk_has_till(self):
        self.assertEqual(500, self.kiosk.till)