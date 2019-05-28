import random

print("Welcome to Hangman!")

words = []
dash = []
not_finished = True
Trig = False
count = 6

with open('sowpods.txt', 'r') as f:
	line = f.readline().split()
	for line in f:
		words.append(line)

idx = random.randint(0, len(words))

choosen_word = words[idx]

for i in range(len(choosen_word)):
	dash.append("_")

dashes = " ".join(dash)

print(dashes)

# print win
def win():
	print("Congratulations, you won! >.<")

# print Lose
def lose():
	print("You lost!")

# For restarting the game (TODO)
def start_again():
	val = input("Do you want to play another game? ")
	if (val == "yes") or (val == "YES") or (val == "Yes"):
		return True
	else:
		return False


while not_finished:

	x = input ("Guess your letter: ")

	if x in choosen_word:
		for i in range(len(choosen_word)):
			if x == choosen_word[i]:
				dash[i] = x
	else:
		Trig = True

	if Trig is True:
		count -= 1
		print("You have %d clues left." % count)
		print("Incorrect!!!\n")
		Trig = False

	dashes = " ".join(dash)

	print(dashes)

	if "_" in dash and count >= 1:
		continue
	elif count <= 0:
		lose()
		break
	else:
		win()
		break

