import msvcrt
import time
import random
from os import system, name
    
def clear():
    if name == 'nt':
        _ = system('cls')

def food():
    return random.randint(0, 162), random.randint(0,31)

def dublicate():
    for i in range(len(snake)):
        index = i + 1
        while index < len(snake):
            if snake[i] == snake[index]:
                return True
            index += 1
    return False

def dec_grid():
    
    grid = '''                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 '''
    return grid


snake = [[0,0]]
previous_entry = "a"
score = 0
y_pos = 0
x_inc = 1
y_inc = 0
x_pos = 0
eaten = True
grid = dec_grid()
while x_pos < 162 and x_pos > -1 and y_pos < 29 and y_pos > -1 and not dublicate():
    if eaten:
        x_food, y_food = food()
        eaten = False
    if snake[0] == [x_food, y_food]:
        snake.append([snake[0][0] + x_inc, snake[0][1] + y_inc])
        score += 1
        eaten = True
    for i in range(len(snake)):
          grid = grid[:snake[i][0] + (snake[i][1]*162)] + "*" + grid[snake[i][0] + (snake[i][1]*162) + 1:]
                

    grid = grid[:x_food + (y_food*162)] + "o" + grid[x_food + (y_food*162) + 1:]
    print (grid)
    grid = dec_grid()
    if previous_entry == "a" or previous_entry == "d":
        time.sleep(1/60)
    else:
        time.sleep(0.075)
    if msvcrt.kbhit():
        x = "{}".format(msvcrt.getch())
        x = x[2]
        if x == "w":
             if previous_entry == "s" and len(snake) != 1:
                 clear()
                 break
             x_inc = 0
             y_inc = -1
        elif x == "a":
             if previous_entry == "d" and len(snake) != 1:
                 clear()
                 break
             y_inc = 0
             x_inc = -1
        elif x == "s":
             if previous_entry == "w" and len(snake) != 1:
                 clear()
                 break
             x_inc = 0
             y_inc = 1
        elif x == "d":
             if previous_entry == "a" and len(snake) != 1:
                 clear()
                 break
             y_inc = 0
             x_inc = 1
        previous_entry = x
    else:
        pass
    x_pos += x_inc
    y_pos += y_inc
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1]
    snake[0] = [x_pos, y_pos]
    clear()

print (score, " Score achieved")
print ("Game Over!")