import random

print("Welcome to Hangman!")

not_finished = True

def open_file():
	words = []

	with open('sowpods.txt', 'r') as f:
		line = f.readline().split()
		for line in f:
			words.append(line)
	
	return words

def get_word(words):
	idx = random.randint(0, len(words))

	choosen_word = words[idx]

	return choosen_word

def get_dashes(choosen_word):
	dash = []

	for i in range(len(choosen_word)):
		dash.append("_")

	dashes = " ".join(dash)

	return dash, dashes

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
	elif (val == "no") or (val == "NO") or (val == "No"):
		return False

def run(choosen_word, dash, dashes):
	count = 6
	Trig = False

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

def main(words):
	choosen_word = get_word(words)
	dash, dashes = get_dashes(choosen_word)
	print(dashes)
	run(choosen_word, dash, dashes)

words = open_file()
main(words)

while start_again():
	main(words)

print("\n Bye Bye! \n")