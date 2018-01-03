from random import *
import process


f = open("usedCards.txt", "w+")
f.write("")

total = 0
pBust=False
bBust=False
lockIn=False
botLockIn=False

#Player Draw
print("Player:")
Player = process.draw(total)
if Player > 21:
	print("Uh oh, you've gone bust!")
	pBust=True
	lockIn=True

#Player Pick
while lockIn == False:
	cardPick=input("Would you like to take another card? ")
	if cardPick.upper() == "Y":   
		Player=process.pick(Player)
		print("Your new total is: ", Player)
		if Player > 21:
			print("Uh oh, you've gone bust!")
			pBust=True
			lockIn=True
	elif cardPick.upper() == "N":
		lockIn=True
		print("Cards locked in.")
	else:
		print("Please enter Y or N")


#Bot Draw
print("\nBot:")
Bot = process.draw(total)
if Bot > 21:
	print("Uh oh, the Bot has gone bust!")
	bBust=True
	botLockIn=True

#Bot Pick
while botLockIn == False:
	if Bot < 21-6: 
		Bot=process.pick(Bot)
		print("The bots new total is: ", Bot)
		if Bot > 21:
			print("Uh oh, you've gone bust!")
			bBust=True
	else:
		botLockIn=True
		print("Bot cards locked in.")

#Compare Scores
if bBust==True:
	if pBust==True:
		print("No winners, both of you are bust!")
	else:
		print("Well done player, you won!")
elif pBust==True:
	print("Unlucky, the bot beat you.")
else:
	playerScore = 21-Player
	botScore = 21-Bot
	if playerScore < botScore:
		print("Well done player, you won!")
	elif playerScore == botScore:
		print("It is a draw, well done to both of you!")
	else:
		print("Unlucky, the bot beat you.")
input()