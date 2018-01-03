#21 card game by Samuel Hendy
from random import *
import process
#Functions
def Player(playerBank):
		total=0
		player={
		"name": input("What is your name?"),
		"bal": process.draw(total),
		"lockIn": False,
		"bust": False
		}
		if player["bal"] > 21:
			player["bust"]=True
			print("Uh oh, ",player["name"], "  has gone bust!")

		print(player)
		playerBank.append(player)
	
def deal(bal):
	a = randint(1,12)
	b = randint(1,12)
	bal = a+b
	return bal


f = open("usedCards.txt", "w+")
f.write("")


play=True
counter=0
players=input("How many people are playing?\n")
playerBank=[]


for i in range(0, int(players)):
	Player(playerBank)

while play==True:
	for x in range(0, int(players)):
		for y in range(0, int(players)):
			if y["bust"] == True:
				counter=counter+1
		if counter==int(players):
			play=False
		else:
			counter=0
			pPick=x["bal"]
			process.pick(pPick)
			x["bal"]=pPick