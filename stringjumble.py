"""
stringjumble.py
Author: Nathalie
Credit: <sources>

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
""" 
import random as rand

# Open the file is input is not there create one
try:
    in_text = open("in.txt", "r")
    out_text = open("out.txt", "w")
except IOError:
    print("File in.txt does not exist creating default one.")
    in_file = open("in.txt", "w")

    string = """\
We are a one of a kind server, as we do not use traditional method of playing.
We allow for all types of game styles. You are required to create an account
to join our network. The reason for this was to create features that no 
other server can provide, this is our game to website integration. We
reinvented the way you will play the game, as of this we use custom code that
differ from how you play on other servers. With this Each server that we run
is connected together, and you can connect to each server without 
reconnecting. We build our servers using high performance parts and custom
code to bring excellent experience to you.\
""".strip()

    print(string, file = in_file)
    in_file.close()
    in_text = open("in.txt", "r")
    out_text = open("out.txt", "w")

# Function to shuffle the chars around
def shuffle(word):
    if len(word) == 1:
        return word
    else:
        half = int(len(word) / 2)
        # First half in reverse
        first = word[:half][::-1]
        # Last half in reverse
        last = word[half:len(word)][::-1]

        # First + Last in reverse
        return str(first+last)[::-1]

# Function to scramble the word
def scramble(word):
    if len(word) < 3:
        return word

    first = word[:1]
    last = word[-1:]
    mid = word[1:-1]
    
    if last == "." or last == ",":
        last = word[-2:]
        mid = word[1:-2]

    return str(first) + str(shuffle(mid)) + str(last)

# Read the input and write the scrambled words to the output
for line in in_text:
    line = line.strip()
    new_line = ""

    for word in line.split(" "):
        new_line += scramble(word) + " "

    print(new_line, file = out_text)

# Close open files
in_text.close()
out_text.close()