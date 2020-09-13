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
    
    def test_increase_till(self):
        self.kiosk.increase_till(100)
        self.assertEqual(600, self.kiosk.till)
    
    def test_put_room_in_use(self):
        self.kiosk.put_room_in_use(self.room_1)
        self.assertEqual(2, self.kiosk.rooms_available)
    
    def test_make_room_available(self):
        self.kiosk.put_room_in_use(self.room_1)
        self.kiosk.make_room_available(self.room_1)
    
    def test_add_room_to_list(self):
        self.kiosk.add_room_to_list(self.room_1)
        self.assertEqual(1, len(self.kiosk.room_list))
    
    def test_remove_room_from_list(self):
        self.kiosk.add_room_to_list(self.room_1)
        self.kiosk.remove_room_from_list(self.room_1)
        self.assertEqual(0, len(self.kiosk.room_list))
    
    def test_book_room(self):
        self.kiosk.book_room(self.room_1)
        self.assertEqual(1, len(self.kiosk.room_list))
        self.assertEqual(2, self.kiosk.rooms_available)
    
    def test_unbook_room(self):
        self.kiosk.book_room(self.room_1)
        self.kiosk.unbook_room(self.room_1)
        self.assertEqual(0, len(self.kiosk.room_list))
        self.assertEqual(3, self.kiosk.rooms_available)

    #check if any room is free
    def test_check_if_rooms_available(self):
        self.assertEqual("Free", self.kiosk.check_if_rooms_available())
    
    def test_check_if_specfic_room_is_free(self):
        self.kiosk.book_room(self.room_1)
        self.assertEqual("Room in Use", self.kiosk.room_check(self.room_1))
        self.assertEqual("Free", self.kiosk.room_check(self.room_2))
