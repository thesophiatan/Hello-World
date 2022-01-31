#Hello world, this software doesn't like people named Bob and will not respond if your name is Bob.
#If your name is has 'bob' or 'rob' in it, the software will refuse to talk to you.
#Otherwise, it will entertain you by telling you how long your name is, how long it's been since your birthday.
#Then, it will offer to play TicTacToe with you.
#If you say no, it will leave you alone.
#TicTacToe rules. You will choose either X or O. X goes first. Computer chooses position randomly. 
#The first to get three blocks in a row wins.
from datetime import date, datetime
from os import name
import random


def dislikes_name(name):
    """ Checks if the user's name is disliked by the AI. Disliked names include those that
    resemble the name 'Bob'.
    """
    if 'bob' in name.lower() or 'rob' in name.lower():
        return True
    return False

def respond_to_disliked_name():
    """ Negatively respond to disliked names
    """
    print("My mom told me not to talk to small town mythical monsters. Be gone with you, foul demon!")

    



def validate_name(name):
    """Names can't be empty, have special characters, or numbers. 
    """
    if name == "" or name.isalpha() is False:
        return False
    return True

def birthday_ask(name):
    """Asks users birthday"""
    date_of_birth=input(("When is your B'day? (in MM/DD/YYYY) "))
    birthdate=datetime.strptime(date_of_birth,"%m/%d/%Y").date()  
    print("Your birthday is "+birthdate.strftime('%B %d, %Y')+("."))  
    user_age(birthdate, name)


def user_age(bday, name):
    """Calculates age of user
    """
    today = date.today()
    birthday=date(today.year, bday.month, bday.day)
    age =int((today-bday).days/365.25)
    calc_days_since_birthday(today, birthday, age, name)

def calc_days_since_birthday(today, birthday, age, name):
    """Number of days since 
    """
    days_since_birthday = (today-birthday).days
    birthday_comment(days_since_birthday, age, name)
    
def bday_within_last_week(days_since_birthday):
    """ Returns True if user's bday was in the last week """
    return 1<int(days_since_birthday)<8

def bday_today(days_since_birthday):
    return int(days_since_birthday)==0

def bday_in_next_week(days_since_birthday):
    return -8<int(days_since_birthday)<-1

def bday_in_week_plus(days_since_birthday):
    return int(days_since_birthday)< -8

def bday_in_week_minus(days_since_birthday):
    return int(days_since_birthday)> 8

def birthday_comment(days_since_birthday, age, name):
    """Comments based on recency of birthday"""
    if bday_within_last_week(days_since_birthday):    
        print(('You are ')+  str((age))  + (' years old, and your birthday was within the last week! Happy belated birthday!'))
    elif bday_today(days_since_birthday):
        print(('You are ')+  str((age))  + (' years old, today is your birthday. Happy Birthday!'))
    elif bday_in_next_week(days_since_birthday):
        print(('You are ')+  str((age))  + (' years old, and your birthday is coming up within a week from now! Happy early birthday!'))
    elif bday_in_week_plus(days_since_birthday):
        print(('You are ')+  str((age))  + (' years old, and your birthday is more than a week from now! Specifically, ') + str(int(days_since_birthday*-1)) + (' days.'))
    elif bday_in_week_minus(days_since_birthday):
        print(('You are ')+  str((age))  + (' years old, and it has been over a week since your birthday! Specifically, ') + str(int(days_since_birthday)) + (' days since your birthday.'))
    game_invite (name)

def game_invite(name):
    invite_reply=str(input(name+(', would you like to play Tic Tac Toe with me? [Y/N]:'))).lower().strip()
    while not(invite_reply =="y" or invite_reply =="n"):
        invite_reply=str(input(name+(', please be clear with me! I need a yes or no. Would you like to play Tic Tac Toe with me? [Y/N]:'))).lower().strip()
    if invite_reply[:1] == 'y':
         game_rules(name)
    if invite_reply[:1] == 'n':
        print("You don't want to play? Okay, maybe next time. See you later! :)")
        quit

def game_rules(name):
    rules_reply=str(input('Sweet! Before we get started, do you know how to play? [Y/N]:')).lower().strip()
    while not(rules_reply =="y" or rules_reply =="n"):
        rules_reply=str(input(name+(', give it to me straight. Do you know how to play? If not, I can teach you! [Y/N]:'))).lower().strip()
    if rules_reply[:1] == 'y':
        game_setup(name)
    if rules_reply[:1] == 'n':
        print("It's pretty simple.\n1. The game is played on a grid that's 3 squares by 3 squares. \n2. One of us plays as X, and the other plays as O. X goes first. Players take turns putting their marks in empty squares.\n3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n5. Choose your move by typing in your x-axis move (top, mid, or low) with your y-axis move (L, M, R). For example, top-L will be the top left square." )
        game_setup(name)
def game_setup(name):
    player_piece=str(input(name+(', would you like to play as X or O? Remember, X goes first. [X/O]:'))).lower().strip()
    while not(player_piece =="x" or player_piece =="o"):
        player_piece=str(input(name+(', we can only play as X or O. Which would you like? [X/O]:'))).lower().strip()
    if player_piece[:1] == 'x':
        print("Okay, you're playing as X, so that means you go first!")
        game_play(player_piece)
    if player_piece[:1] == 'o':
        print("Okay, I'm playing as X, so that means I'm going first!")
        game_play(player_piece)

def game_play(player_piece):
    player_XO=str(player_piece.upper())
    turn = 'X'
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
        'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
        'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    possibleMoves = ['top-L','top-M', 'top-R', 'mid-L', 'mid-M', 'mid-R', 'low-L', 'low-M', 'low-R']

    def printBoard(board):
        print('     ')
        print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
        print('-+-+-')
        print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
        print('-+-+-')
        print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
        print('     ')


    def testForAWin(board):
        won = False
    #Horizontal Wins
        if((board['top-L'] == board['top-M'] == board['top-R']) and board['top-L'] != ' '):
            won = True
        elif(board['mid-L'] == board['mid-M'] == board['mid-R'] and board['mid-L'] != ' '):
            won = True
        elif(board['low-L'] == board['low-M'] == board['low-R'] and board['low-L'] != ' '):
            won = True
    #Vertical Wins
        elif(board['low-L'] == board['mid-L'] == board['top-L'] and board['low-L'] != ' '):
          won = True
        elif(board['low-M'] == board['mid-M'] == board['top-M'] and board['low-M'] != ' '):
          won = True
        elif(board['low-R'] == board['mid-R'] == board['top-R'] and board['low-R'] != ' '):
            won = True
    #Diagonal Wins
        elif(board['low-L'] == board['mid-M'] == board['top-R'] and board['low-L'] != ' '):
           won = True
        elif(board['low-R'] == board['mid-M'] == board['top-L'] and board['low-R'] != ' '):
           won = True
        return won

    for i in range(9):
        printBoard(theBoard)
        if str(player_XO) == turn:
            print("It's " + turn + "'s turn. Choose a space: ")
            move = input()
            while move not in (possibleMoves):
                move =input("That's not an option on the board! Go ahead and try again.")
        else:
            print("It's " + turn + "'s turn. Choose a space: ")
            move = random.choice(possibleMoves)
            while move not in (possibleMoves):
                move =input("That's not an option on the board! Go ahead and try again.")
    
        while not theBoard[move]== ' ':
            print('Do not try to steal a place! ')
            if str(player_XO) == turn:
                move = input()
            else:
                move = random.choice(possibleMoves)
    
        theBoard[move] = turn
        won = testForAWin(theBoard)
        if won:
            print(turn + ' wins the game!')
            break
        elif turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    printBoard(theBoard)

def nice_to_meet(name):
    """Lets user know how nice it is to meet them.
    Tells them how long their name is.
    """
    print(f'It\'s nice to meet you {name.capitalize()}! Your name is {len(name)} letters long.')
    birthday_ask(name)


def intro_user():
    """Checks to validity and dislike of name, if valid and liked then proceeds
    """
    user_name = str(input())
    if validate_name(user_name)==False:
        invalid_name()
    if dislikes_name(user_name):
        respond_to_disliked_name()
        quit
    if validate_name(user_name):
        nice_to_meet(user_name)

def invalid_name():
    """Provides error message
    """
    print("That doesn't sound right. Please enter a more believable human name that only has letters.")
    intro_user()

def greet_user():
    """Greets user
    """
    print('Hello, what is your name?')
    intro_user()
greet_user()
