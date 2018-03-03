#Blackjack or 21 
#from __future__ import print_function
import random
# Dealer cards
Dealer_cards = []
# Player cards
Player_cards = []
# Deal card
	# Dealer card
while Dealer_cards != 2:
	Dealer_cards.append(random.randint(1,11))
	if Dealer_cards == 2:
		print ("Dealer has X & ", Dealer_cards[1])

# Player cards

while Player_cards != 2:
	Player_cards.append(random.randint(1,11))
	if Player_cards == 2:
		print("You have ", Player_cards)

# sum of dealer cards
if sum(Dealer_cards) == 21:
	print ("Dealer has 21 and wins!")
elif sum(Dealer_cards) > 21:
	print ("Dealer has busted")

while sum(Player_cards) < 21:
	action_taken = str(raw_input("Do you want to hit or stay? "))
	if action_taken == hit:
		Player_cards.append(random.randint(1,11))
		print ("You now have "+ str(sum(Player_cards)) + "with these cards", Player_cards)
	else:
		print ("You have " + str(sum(Player_cards)) + "with cards", Player_cards)
		print ("Dealer have" + str(sum(Dealer_cards)) + "with cards", Dealer_cards)
		if sum(Dealer_cards) > sum(Player_cards):
			print ("Dealer wins!")
		else:
			print ("You win!")

if sum(Player_cards) > 21:
	print ("You busted!")
elif sum(Player_cards) == 21:
	print ("You have BLACKJACK and win!")


