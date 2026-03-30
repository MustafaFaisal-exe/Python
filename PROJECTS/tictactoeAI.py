from os import system, name
import random

def clear():
    if name == 'nt':
        _ = system('cls')

def display():
    print ("                                                                        ")
    print ("                              " + "          |               |          ")
    print ("                              " + grid[0] + "     |   " + grid[1] + "       |" + grid[2])
    print ("                              " + "          |               |          ")
    print ("                              " + "  ---------------------------------- ")
    print ("                              " + "          |               |          ")
    print ("                              " + grid[3] + "     |   " + grid[4] + "       |" + grid[5])
    print ("                              " + "          |               |          ")
    print ("                              " + "  ---------------------------------- ")
    print ("                              " + "          |               |          ")
    print ("                              " + grid[6] + "     |   " + grid[7] + "       |" + grid[8])
    print ("                              " + "          |               |          ")
    print ("                                                                        ")

grid = ["    1","    2","    3","    4","    5","    6","    7","    8","    9"]
marking = ["    X","    O","    X","    O","    X","    O","    X","    O","    X"]
winner = [[1,2,3],[7,8,9],[1,4,7],[3,6,9],[1,5,9],[3,5,7],[4,5,6],[2,5,8]]
combinations = [[1,2,3],[7,8,9],[1,4,7],[3,6,9],[1,5,9],[3,5,7],[4,5,6],[2,5,8]]
tries = 9
corners = [1,3,7,9]
sides = [2,4,6,8]
def mark(tries):
    victory = False
    while tries > 0 and not victory:
        if (tries - turn + 1) % 2 == 1:
            index = int(input(f"Enter the location for{marking[tries - 1]}: "))
            while index > 9 or index < 0:
                index = int(input(f"Wrong entery, location out of bounds. Enter a new location: "))
            if index in corners:
                corners.pop(corners.index(index))
            while grid[index - 1] == "    X" or grid[index - 1] == "    O":
                index = int(input(f"Wrong entery, location already has {grid[index - 1]}. Enter a new and empty location for{marking[tries - 1]}: "))
        elif mode == 1:
            index = AI(tries)
        else:
            index = int(input(f"Enter the location for{marking[tries - 1]}: "))
            while index > 9 or index < 0:
                index = int(input(f"Wrong entery, location out of bounds. Enter a new location: "))
            if index in corners:
                corners.pop(corners.index(index))
            while grid[index - 1] == "    X" or grid[index - 1] == "    O":
                index = int(input(f"Wrong entery, location already has {grid[index - 1]}. Enter a new and empty location for{marking[tries - 1]}: "))
        grid[index - 1] = marking[tries - 1]
        tries -= 1
        clear()
        display()
        if tries <= 5:
            victory, counter_x, counter_o = check()
        
    if counter_o == 3:
        print ("O WINS THE GAME!!!")
    elif counter_x == 3:
        print ("X WINS THE GAME!!!")
    else:
        print ("DRAW!!!")

def AI(tries):
    if tries == 9:
        loc = random.choice(corners)
        corners.pop(corners.index(loc))
        return loc
    elif tries == 8:
        if grid[4] == "    5":
            return 5
        else:
            loc =  random.choice(corners)
            return loc
    if tries < 8:
        AI_win, index_AI = AI_check()
        player_win, index_player = player_check()
        if AI_win:
            return index_AI
        elif player_win:
                return index_player
        elif index_AI == -1:
            if len(corners) <= 2:
                loc = random.choice(sides)
                while grid[loc - 1] == "    X" or grid[loc - 1] == "    O":
                    loc = random.choice(sides)
                sides.pop(sides.index(loc))
            else:
                loc = random.choice(corners)
                while grid[loc - 1] == "    X" or grid[loc - 1] == "    O":
                    loc = random.choice(corners)
                corners.pop(corners.index(loc))
            return loc
            
def AI_check():
    possible_winner = False
    i = 0
    if turn == 1:
        address = tries - 2
    else:
        address = tries - 1
    while i < len(combinations) and not possible_winner:
        count = 0
        for index, location in enumerate(combinations[i]):
            if grid[location - 1] == marking[address]:
                count += 1
            else:
                empty = location
        if count == 2 and (grid[empty - 1] != "    X" and grid[empty - 1] != "    O"):
            combinations.pop(i)
            possible_winner = True
            return possible_winner, empty
        i += 1
    return possible_winner, -1

def player_check():
    player_winner = False
    if turn == 1:
        address = tries - 1
    else:
        address = tries - 2
    j = 0
    while j < len(winner) and not player_winner:
        count = 0
        count = 0
        for index, location in enumerate(winner[j]):
            if grid[location - 1] == marking[address]:
                count += 1
            else:
                empty = location
        if count == 2 and (grid[empty - 1] != "    X" and grid[empty - 1] != "    O"):
            player_winner = True
            return player_winner, empty
        j += 1
    return player_winner, -1

def check():
    winner_found = False
    i = 0
    while i < len(winner) and not winner_found:
        counter_x = 0
        counter_o = 0
        for location in range(len(winner[i])):
            if grid[winner[i][location] - 1] == "    X":
                counter_x += 1 
            if grid[winner[i][location] - 1] == "    O":
                counter_o += 1
        if counter_x == 3 or counter_o == 3:
            winner_found = True
            return winner_found, counter_x, counter_o
        i += 1
    return winner_found, counter_x, counter_o

print ("                            __________________      __________________      __________________")
print ("                                    |                       |                       |         ")
print ("                                    |                       |                       |         ")
print ("                                    |                       |                       |         ")
print ("                                    |                       |                       |         ")
print ("                                    | IC                    | AC                    | OE      ")
print ("                                                                                              ")
print ("                                                                                              ")
print ("                                                                                              ")
play = input("                                      Press 'ENTER' to play: ")
while play == "":
    print ("                                                                                              ")
    print ("                                                                                              ")
    mode = int(input("                           1. Single Player / 2. Multiplayer: "))
    print ("                                                                                              ")
    print ("                                                                                              ")
    turn = 1
    if mode == 1:
        turn = int(input("                              Enter your turn. 1st or 2nd: "))
    if play == "":
        clear()
        display()
        mark(tries)
    play = input("                              Press Enter to play again or Press any other button to finish: ")
    print ("                                                                                              ")
    print ("                                                                                              ")
print ("                                                     GAME OVER!!!!!!!")