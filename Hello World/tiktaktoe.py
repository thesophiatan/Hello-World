#Hello world, this software doesn't like people named Bob and will not respond if your name is Bob.
#If your name is similar to Bob, like Rob, Boob, Robert, Robby, etc, the software will insist you are Bob wearing a poor disguise.
#Otherwise, it will entertain you by telling you how long your name is, how long it's been since your birthday.
#Then, it will offer to play TikTakToe with you.
#If you say no, it will cry and mock you until you say yes.
#TikTakToe rules. You will choose either X or O. X goes first. Computer chooses position randomly. 
#The first to get three blocks in a row wins.
from datetime import date, datetime


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

    
def invalid_name():
    """Provides error message
    """
    print("That doesn't sound right. Please enter a more believable human name that only has letters.")
    intro_user()


def validate_name(name):
    """Names can't be empty, have special characters, or numbers. 
    """
    if name == "" or name.isalpha() is False:
        return False
    return True

def birthday_ask():
    """Asks users birthday"""
    date_of_birth=input(("When is your B'day? (in MM/DD/YYYY) "))
    birthdate=datetime.strptime(date_of_birth,"%m/%d/%Y").date()  
    print("Your B'day is "+birthdate.strftime('%B %d, %Y'))  
    user_age(birthdate)

def user_age(bday):
    """Calculates age of user
    """
    today = date.today()
    birthday=datetime(today.year, bday.month, bday.day)
    age = int((today-bday).days / 365.25)
    calc_days_since_birthday(bday, age)


def calc_days_since_birthday(bday, age):
    """Number of days since 
    """
    today = date.today()
    days_since_birthday = (today-bday).days
    birthday_comment(days_since_birthday, age)

def bday_within_last_week(days_since_bday):
    """ Returns True if user's bday was in the last week """
    return 365<int(days_since_bday)<372

def bday_today(days_since_bday):
    return int(days_since_bday)==0

def bday_in_next_week(days_since_bday):
    return 358<int(days_since_bday)<365

def birthday_comment(days_since_bday, age):
    """Comments based on recency of birthday"""
    if bday_within_last_week(days_since_bday):    
        print(('You are')+  str((age))  + (' years old, and your birthday was within the last week! Happy belated birthday!'))
    elif bday_today(days_since_bday):
        print(('You are')+  str((age))  + (' years old, today is your birthday. Happy Birthday!'))
    elif bday_in_next_week(days_since_bday):
        print(('You are')+  str((age))  + (' years old, and your birthday is coming up within a week from now! Happy early birthday!'))
    else:
        print(('You are ')+  str((age))  + (' years old, and it has been ') + str(int(days_since_bday)) + (' days since your birthday.'))


def nice_to_meet(name):
    """Lets user know how nice it is to meet them.
    Tells them how long their name is.
    """
    print(f'It\'s nice to meet you {name.capitalize()}! Your name is {len(name)} letters long.')
    birthday_ask()


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


def greet_user():
    """Greets user
    """
    print('Hello, what is your name?')
    intro_user()


###SOPHIA LOOK UP WHAT THIS IS
# if __name__ == "__main__":


greet_user()
