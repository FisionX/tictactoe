import random
import time

def print_grid(values):
    print("     |     |     ")
    print("  {}  |  {}  |  {} ".format(values[0], values[1], values[2],))
    print("_____|_____|_____")
    print("     |     |     ")
    print("  {}  |  {}  |  {} ".format(values[3], values[4], values[5],))
    print("_____|_____|_____")
    print("     |     |     ")
    print("  {}  |  {}  |  {} ".format(values[6], values[7], values[8],))
    print("     |     |     ")

def check_win(values):
    if values[0] == values[1] and values[0] == values[2]:
        return True
    elif values[3] == values[4] and values[3] == values[5]:
        return True
    elif values[6] == values[7] and values[6] == values[8]:
        return True
    elif values[0] == values[3] and values[0] == values[6]:
        return True
    elif values[1] == values[4] and values[1] == values[7]:
        return True
    elif values[2] == values[5] and values[2] == values[8]:
        return True
    elif values[0] == values[4] and values[0] == values[8]:
        return True
    elif values[6] == values[4] and values[6] == values[2]:
        return True
    else: return False

def cont(clean_values, values): # Check if the game continues
    empty_spaces = []
    for x in clean_values:
        if x == ' ':
            empty_spaces.append(x)
    empty_spaces = len(empty_spaces)

    if empty_spaces == 0 or check_win(values) == True:
        return False #The game ends
    else:
        return True #The game continues

def game():
    p1, p2 = "X", "O"
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    clean_values = [' ' for x in range(9)]
    turn = random.choice([p1, p2]) #Choses who will be the first turn
    con = cont(clean_values, values) # Will be tha game control variable
    place = 0

    print("Tic Tac Toe Game")
    time.sleep(1)
    print("It's {} player turn".format(turn))
    print_grid(values)

    while(con):
        place = int(input("Chose a number for {} ".format(turn))) - 1
        while(place < 0 or place > 9): # makes shure if the user imput is correct like a try exept but in a loop
            print("Value out of range. Try again :]")
            place = int(input("Chose a number for {} ".format(turn)))
        values[place], clean_values[place] = turn, turn

        print_grid(values)
        con = cont(clean_values, values)
        if con == False:
            print("Player {} wins!!".format(turn))

        if turn == p1:
            turn = p2
        else: turn = p1

game()
