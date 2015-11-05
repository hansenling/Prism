import random

class Card:

	def __init__(self, suit, number):
		self.suit = suit
		self.number = number

	def __str__(self):
		return "{0} of {1}".format(self.number, self.suit)

class Deck:

	def __init__(self):
		self.cards = []
		for suit in ["Diamonds", "Hearts", "Spades", "Clubs"]:
			for number in range(2, 11):
				self.cards.append(Card(suit, number))
			for face in ["King", "Queen", "Jack", "Ace"]:
				self.cards.append(Card(suit, face))

	def __str__(self):
		retstring = ""
		for card in self.cards:
			retstring += str(card) + "\n"
			
		return retstring

	def Shuffle(self):
		self.__init__()
		return random.shuffle(self.cards)

	def GetNextCard(self):
		try:
			a = self.cards.pop()
		except IndexError:
			 print("Oh no! The Deck is empty! Shuffle to refill the deck.")
