import unittest
from unittest.mock import patch

import tictactoe
from tictactoe import *

class TestGameSetup(unittest.TestCase):
    def test_new_game(self):
        self.fail("not implemented")

    def test_get_starting_player(self):
        self.assertIsInstance(get_starting_player(), bool)

class TestGamePlay(unittest.TestCase):
    def test_humans_move(self):
        game = ""
        expected = ""

        # patch the input function to always return '2'
        with patch.object(tictactoe, "input", create=True,
                            return_value='2'):
            self.assertEqual(humans_move(game), expected)

    def test_computers_move(self):
        self.fail("not implemented")

    def test_check_winner(self):
	def test_human_wins(self):
		self.assertEqual(check_winner('XXXEOEEOO'), True)	
	def test_computer_wins(self):
		self.assertEqual(check_winner('EEOXEOXXO'), True)
	def test_draw(self):	
		self.assertEqual(check_winner('XOOOXXOXX'), True)	
	def test_none(self):	
		self.assertEqual(check_winner('EEEEEOXEX'), True)		
if __name__ == '__main__':
    unittest.main()

