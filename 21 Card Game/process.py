from random import *

def Class():
	r = randint(1,4)
	if r == 1:
		classVal="H"
	elif r == 2:
		classVal="D"
	elif r == 3:
		classVal="S"
	else:
		classVal="C"
	return classVal


def draw(total):
	add=open("usedCards.txt", "a")
	read=open("usedCards.txt", "r")
	content = read.read()
	reroll=False
	a = randint(1,13)
	cardA = (a,Class())

	if str(cardA) in content:
		reroll=True

		while reroll==True:
			a = randint(1,13)
			cardA = (a,Class())

			if str(cardA) not in content:
				reroll=False
				add.write(str(cardA))
	else:
		add.write(str(cardA))

	b = randint(1,13)
	cardB = (b,Class())

	if str(cardB) in content:
		reroll=True

		while reroll==True:
			b = randint(1,13)
			cardB = (b,Class())

			if str(cardB) not in content:
				reroll=False
				add.write(str(cardB))
	else:
		add.write(str(cardB))
	total = a+b
	print("Picked a total of", total, ". This consists of: ", cardA, " and ", cardB)
	return total

def pick(total):
	add=open("usedCards.txt", "a")
	read=open("usedCards.txt", "r")
	content = read.read()
	reroll=False
	a = randint(1,13)
	cardA = (a,Class())

	if str(cardA) in content:
		reroll=True

		while reroll==True:
			a = randint(1,13)
			cardA = (a,Class())

			if str(cardA) not in content:
				reroll=False
				add.write(str(cardA))
	else:
		add.write(str(cardA))
	print("You got: ", cardA)
	total = total + a
	return total