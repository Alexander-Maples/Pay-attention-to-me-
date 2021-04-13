import os
import random
import time
import sys

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
x=1
typing('Hi, %s.' % name)
print("")
while x == 1:
	sys.exit("ERROR")