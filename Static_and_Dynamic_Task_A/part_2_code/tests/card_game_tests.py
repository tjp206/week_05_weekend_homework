import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_ace = Card('spades', 1)
        self.card1 = Card('hearts', 10)
        self.card2 = Card('clubs', 5)
        self.card_game = CardGame()

    def test_check_for_ace(self):
        self.assertEquals(True, self.card_game.check_for_ace(self.card_ace))

    def test_highest_card(self):
        self.assertEquals(self.card1, self.card_game.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        cards = [self.card1, self.card2]
        self.assertEquals("You have a total of 15", self.card_game.cards_total(cards))

