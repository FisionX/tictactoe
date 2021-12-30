import random
import time

p1, p2 = "X", "O"
values = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]
turn = random.choice([p1, p2])

def sel_template():
    select_template = """
     |     |
  1  |  2  |  3
_____|_____|_____
     |     |
  4  |  5  |  6
_____|_____|_____
     |     |
  7  |  8  |  9
     |     |     """
    print(select_template)

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
    if values[0:3] == [p1, p1, p1]:
        print("Player {} wins!".format(p1))
    elif values[0:3] == [p2, p2, p2]:
        print("Player {} wins!".format(p2))
    elif values[3:6] == [p1, p1, p1]:
        print("Player {} wins!".format(p1))
    elif values[3:6] == [p2, p2, p2]:
        print("Player {} wins!".format(p2))
    elif values[6:9] == [p1, p1, p1]:
        print("Player {} wins!".format(p1))
    elif values[6:9] == [p2, p2, p2]:
        print("Player {} wins!".format(p2))

def game():
    print("Tic Tac Toe Game")
    time.sleep(.3)
    print("It's {} player turn".format(turn))
    print(values[6:9])

game()
