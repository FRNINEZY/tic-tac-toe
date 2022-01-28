import os 
import sys
import time
import random
import pyttsx3
from colorama import Fore 
from colorama import init

speak = pyttsx3.init()


init()

os.system("cls")

#the game board 
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#Player Symbol is
x = "X"

#shows settings
def rules():
    speak.say("Okay Here")
    speak.runAndWait()
    print("""
Controls

1 -> top left 
2 -> top center 
3 -> top right
-----------------------
4 -> center left  
5 -> center 
6 -> center right 
-----------------------
7 -> down left
8 -> down center 
9 -> down right 
""")

#running game 
Win = None
run = True 

#Board 
def playboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8]) 

#Input
def player(board):
    awnser = int(input("Eneter a number(1-9): "))
    if awnser >= 1 and awnser <= 9 and board[awnser-1] == "-":
        board[awnser-1] = x
    else:
        print("")
        print(Fore.RED)
        print("Wrong awnser plz choose another option!")
        print("")

#Win cheak
def cheking(board):
    global Win
    if board[0] == board[1] == board[2] and board[1] != "-":
        Win = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        Win = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        Win = board[6]
        return True

#chaking rows for win 
def rowwin(board):
    global Win
    if board[0] == board[3] == board[6] and board[0] != "-":
        Win = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        Win = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        Win = board[2]
        return True

#Cheaking Diag for win
def diagwin(board):
    global Win
    if board[0] == board[4] == board[8] and board[0] != "-":
        Win = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        Win = board[2]
        return True

#Cheaking For tie 
def Tiecheak(board):
    global run
    if '-' not in board:
        playboard(board)
        print("Yo its Tie")
        run = False

#Cheking for Win!!
def wincheak():
    if rowwin(board) or cheking(board) or diagwin(board):
        speak.say("The winner is " + Win)
        speak.runAndWait()
        print(Fore.GREEN + "Wins " + Win)
        sys.exit()

#Player switch 
def switch():
    global x 
    if x == "X":
        x = "O"
    else:
        x = "X"

#pc
def pc(board):
    while x == "O":
        poss = random.randint(0,8)
        if board[poss] == "-":
            board[poss] = "O"
            switch()

#Game is running 
def gameison():
    while run:
        print(Fore.WHITE)
        playboard(board)
        player(board)
        wincheak()
        Tiecheak(board)
        switch()
        pc(board)

#running all 
print(Fore.GREEN)
speak.say("Hello. Wellcome! ")
speak.runAndWait()
yourn = input("Hello do you whant to see how to play(y/n): ")
if yourn == "y":
    os.system("cls")
    rules()
    time.sleep(5)
    os.system("cls")
    print(Fore.YELLOW)
    print("Now starting")
    speak.say("Starting the game!")
    speak.runAndWait()
    time.sleep(2)
    os.system("cls")
    gameison()
elif yourn == "n":
    os.system("cls")
    print(Fore.YELLOW)
    print("Now starting")
    speak.say("Starting the game!")
    speak.runAndWait()
    os.system("cls")
    gameison()
    

