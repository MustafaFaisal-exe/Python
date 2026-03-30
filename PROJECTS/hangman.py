from os import system, name
import random
def display(mistakes):
    print ("_______________________________")
    print ("|                             |")
    print ("|                             |")
    if mistakes >= 1:
        print ("|                           _____")
        print ("|                          /x  x \\")
        print ("|                          |     |")
        print ("|                          \\_____/")
    if mistakes == 2:
        print ("|                              |")
        print ("|                              |")
        print ("|                              |")
        print ("|                              |")
        print ("|                              |")
        print ("|                              |")
        print ("|                              |")
        print ("|                              |")
        print ("|                              |")
        print ("|                              |")
        print ("|                              |")
    if mistakes >= 3:
        print ("|                              |")
        print ("|                              |")
        print ("|                           ___|___")
        print ("|                          /   |   \\")
        print ("|                         /    |    \\")
        print ("|                        /     |     \\")
        print ("|                       /      |      \\")
        print ("|                              |")
        print ("|                              |")
        print ("|                              |")
        print ("|                              |")
    if mistakes >= 4:
        print ("|                             / \\")
        print ("|                            /   \\")
        print ("|                           /     \\")
        print ("|                          /       \\")
    print ("|")
    print ("|")
    print ("|")
    print ("|")
    print ("|")
    print ("|")
    print ("|")
    print ("|")
    print ("|")
    if mistakes < 2:
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
    if mistakes < 1:
        print ("|")
        print ("|")
        print ("|")
        print ("|")
    print ("")
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def clear():
    if name == 'nt':
        _ = system('cls')
def replace_string(instring, item, rep):
    temp = ""
    found = 0
    for i in instring:
        if i == item and found == 0:
            temp += rep
            found += 1
        else:
            temp += i
    return temp
def Word():
    file = open("hangman.txt", "r")
    index = random.randint(0, 9) % 4
    for i in range(index * 4):
        temp = file.readline().strip()
    temp = file.readline().strip()
    hint1 = file.readline().strip()
    hint2 = file.readline().strip()
    hint3 = file.readline().strip()
    return temp, hint1, hint2, hint3
def Game():
    score = 100
    mistakes = 0
    hint_count = 2
    display(mistakes)
    word, hint1, hint2, hint3 = Word()
    word_guess = ["_" for i in range(len(word))]
    word_omitted = []
    print ("")
    print (word_guess)
    print ("")
    print ("Guess the word")
    print ("")
    print ("hint: ", hint1)
    term = False
    while not term:
        guess = str(input("Enter your guess or ask for a hint (Type: hint): "))
        if guess == 'hint':
            if hint_count > 0:
                print ("")
                event = str(input(str(hint_count) + " hint(s) left. It will effect your score (reduced to half). Press ENTER to continue: "))
                if event == "":
                    print ("")
                    if hint_count == 2:
                        print ("Your hint is: ", hint2)
                    else:
                        print ("Your hint is: ", hint3)
                    print ("")
                    hint_count -= 1
                    score *= 0.5
            else:
                print ("No More hints left")
        else:
            while len(guess) != 1 or guess not in alphabets:
                guess = str(input("WRONG ENTRY! Enter your guess again: "))
        if guess in word:
            for j in word:
                if j == guess:
                    word_guess[word.index(guess.lower())] = guess
                    word = replace_string(word, guess, "_")
            alphabets.pop(alphabets.index(guess.lower()))
        elif guess != 'hint':
            mistakes += 1
            score -= 5
        word_omitted.append(guess.lower())
        if guess != 'hint':
            clear()
            display(mistakes)
            print (word_guess, "                                   words used: ", word_omitted)
            print ("")
            if len(alphabets) == 0:
                print ("Your Score: ", score)
                print ("U Lost! No more alphabets left")
                term = True
            elif word == "_"*len(word):
                print ("Your Score: ", score)
                print ("Congrats! U won")
                term = True
            elif mistakes == 4:
                print ("Your Score: ", score)
                print ("U lost! 4 mistakes were mad. NOOB!")
                term = True
    print ("GAME OVER!")
Game()