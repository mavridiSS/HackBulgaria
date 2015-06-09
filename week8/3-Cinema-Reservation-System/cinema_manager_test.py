from cinema_manager import CinemaManager
from settings import DB_NAME
import unittest
import create_database
from settings import ROWS, COLUMNS
import sqlite3


class CinemaManagerTest(unittest.TestCase):
    def setUp(self):
        create_database.main()
        self.conn = sqlite3.connect(DB_NAME)
        self.cm = CinemaManager(self.conn)

    def test_get_movies_ordered_by_rating(self):
        res = self.cm.get_movies_ordered_by_rating()
        test = [(2, "Her", 8.3),
                (3, "Wreck-It Ralph", 7.9),
                (1, "The Hunger Games: Catching Fire", 7.8)]
        self.assertEqual(res, test)

    def test_get_movie_by_id(self):
        res = self.cm.get_movie_by_id(3)
        movie = ("Wreck-It Ralph", 7.9)
        self.assertEqual(res, movie)

    def test_get_projection_by_id(self):
        res = self.cm.get_projection_by_id(1)
        proj = ("2014-04-01", "19:10", "3D")
        self.assertEqual(res, proj)

    def test_get_projections_for_movie(self):
        res = self.cm.get_projections_for_movie(3)
        proj = [(4, "2014-04-05", "20:20", "2D", 0)]
        self.assertEqual(res, proj)

    def test_get_seats_for_projection(self):
        res = self.cm.get_seats_for_projection(4)
        self.assertEqual(res, [])

    def test_check_if_seat_is_free(self):
        self.cm.create_hall()
        res = self.cm.check_if_seat_is_free(3, 3)
        self.assertTrue(res)

    def test_take_seats(self):
        self.cm.create_hall()
        self.cm.take_seats([(0, 0)])
        res = self.cm.check_if_seat_is_free(1, 1)
        self.assertFalse(res)

    def test_make_new_reservation(self):
        self.cm.make_new_reservation('ivan', 4, 1, 1)
        res = self.cm.get_seats_for_projection(4)
        self.assertEqual(res, [(0, 0)])

    def test_delete_reservation(self):
        self.cm.delete_reservation('ivan')
        res = self.cm.get_seats_for_projection(4)
        self.assertEqual(res, [])

if __name__ == '__main__':
    unittest.main()
