import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('hearts', 1)
        self.card2 = Card('spades', 7)
        self.card3 = Card('diamonds', 10)
        self.cards = [self.card1, self.card2, self.card3]

    def test_check_for_ace(self):
        # breakpoint()
        result = CardGame.check_for_ace(self, self.card1)
        expected = True
        self.assertEqual(expected, result)

    def test_highest_card(self):
        result = CardGame.highest_card(self, self.card1, self.card2)
        expected = self.card2
        self.assertEqual(expected, result)

    def test_cards_total(self):
        result = CardGame.cards_total(self, self.cards)
        expected = 'You have a total of 18'
        self.assertEqual(expected, result)