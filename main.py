import random


suits = ('Hearts','Diamonds', 'Spades', 'Clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,'seven':7, 'eight':8, 'nine':9, 'ten':10,
'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank + ' of ' + self.suit

#card_1 = Card('diamond','two')
#print(card_1)

class Deck:

	def __init__(self):

		self.all_cards = []

		for suit in suits:
			for rank in ranks:
				cards = Card(suit, rank) #the card class is being called
				self.all_cards.append(cards)

	def shuffle_deck(self):
		random.shuffle(self.all_cards)

	def pop_card(self):
		return self.all_cards.pop() #it's popping and returning it

mycard = Deck()

"""card_2 = Deck()
print(card_2.all_cards[3])

for cards in card_2.all_cards:
	print(cards)

card_2.shuffle_deck() #shuffle the deck
print(card_2.all_cards[0 ])

card_2.pop_card()#delete one card from the list
len(card_2.all_cards) #should return 51 then 50 and so on
"""
class Player:

	def __init__(self, name):
		self.name = name
		self.all_cards = []

	def remove_one(self):
		if len(self.all_cards) > 0:
			return self.all_cards.pop(0)
		else:
			pass
	def add_cards(self,new_cards):
		if type(new_cards) == type([]):
			self.all_cards.extend(new_cards)
		else:
			self.all_cards.append(new_cards)
		

	def __str__(self):
		return f'PLayer {self.name} has {len(self.all_cards)} cards'

"""
player_1 = Player("Erfan")
print(player_1)
player_1.add_cards(mycard)
print(player_1)
player_1.add_cards([mycard,mycard,mycard])#adding more then 1 cards
print(player_1)
#remove card

player_1.remove_one()
print(player_1)

"""

#Game setup
player1 = Player('Bot1')
player2 = Player('Bot2')

new_deck = Deck()
new_deck.shuffle_deck()

for x in range(26):
	player1.add_cards(new_deck.pop_card())
	player2.add_cards(new_deck.pop_card())
print(len(player1.all_cards))

##while game_on
game_on = True
round_num = 0
while game_on:
	round_num += 1
	print(f'Round {round_num}')

	if len(player1.all_cards) == 0:
		print(f'{player1} has lost')
		game_on = False

	if len(player2.all_cards) == 0:
		print(f"{player2} has lost")
		game_on = False


	#start a new round
	player1_cards = []
	player1_cards.append(player1.remove_one()) #grab one card and remove it

	player2_cards = []
	player2_cards.append(player2.remove_one()) # grab one card and remove it

	#while_at_war

	at_war = True

	while at_war: # comparing the 2 cards
		if player1_cards[-1].value > player2_cards[-1].value:
			player1.add_cards(player1_cards)
			player1.add_cards(player2_cards)

			at_war = False

		elif player2_cards[-1].value > player1_cards[-1].value:
			player2.add_cards(player1_cards)
			player2.add_cards(player2_cards)

			at_war = False

		else:
			print("War")

			if len(player1.all_cards) < 3:
				print(f"{player1} not have enough cards for next round \n {player2} Wins!")

				game_on = False
				break #exit out of at_war

			elif len(player2.all_cards) < 3:
				print(f"{player2} not enough cards for next round \n {player1} Wins!")

				game_on = False
				break 

			else:
				for num in range(3):
					player2_cards.append(player1.remove_one())
					player2_cards.append(player2.remove_one())
