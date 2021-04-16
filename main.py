import os
import random
import time
import sys
from replit import db

db["y"] = "1"
db["n"] = "0"
value = db["n"]

my_secret = os.environ['hidden mode']

text = 0

def clear():
	os.system("clear")

def fastt(word):
				word
				for char in word:
								time.sleep(random.choice([0.03, 0.02, 0.04, 0.028]))
								sys.stdout.write(char)
								sys.stdout.flush()

def typing(words):
				words
				for char in words:
								time.sleep(random.choice([0.04, 0.04, 0.05, 0.05, 0.04, 0.038, 0.05]))
								sys.stdout.write(char)
								sys.stdout.flush()

typing('What is your name?\n')
name = input("")
name = name.capitalize()
x = 1
clear()
if name == my_secret:
	typing(os.environ['hidden mode response'])
else:
	typing('Hi, %s.' % name)
print("")
while x == 1:
	sys.exit("ERROR: Unfinished Code")
	text = random.choice([1, 2, 3, 5, 6, 7, 8, 9, 10])
	if text == 1:
		typing("Are you still paying attention to me? (y or n only)")
		response = input("")
		if response == "y":
			fastt("Good.")
		elif response == "n":
			typing("Well screw you then!")
			sys.exit()
		else:
			typing("What does that even mean?")
			sys.exit()
		