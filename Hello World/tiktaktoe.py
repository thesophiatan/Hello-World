#Hello world, this software doesn't like people named Bob and will not respond if your name is Bob.
#If your name is similar to Bob, like Rob, Boob, Robert, Robby, etc, the software will insist you are Bob wearing a poor disguise.
#Otherwise, it will entertain you by telling you how long your name is, how long it's been since your birthday.
#Then, it will offer to play TikTakToe with you.
#If you say no, it will cry and mock you until you say yes.
#TikTakToe rules. You will choose either X or O. X goes first. Computer chooses position randomly. 
#The first to get three blocks in a row wins.
def greet_user():
    print('Hello, what is your name?')
    intro_user()

def dislikes_name(name):
    """ Checks if the user's name is disliked by the AI. Disliked names include those that
    resemble the name 'Bob'.
    """
    if 'bob' in name.lower() or 'rob' in name.lower():
        return True
    return False

def respond_to_disliked_name():
    """ Negatively respond 
    """
    print("My mom told me not to talk with mythical monsters. Be gone with you, foul demon!")

def intro_user():
    user_name = str(input())
    if validate_name(user_name)==False:
        invalid_name()
    if dislikes_name(user_name):
        respond_to_disliked_name()
        quit
    
def invalid_name():
    print("That doesn't sound right. Please enter a more believable human name that only has letters.")
    intro_user()

def validate_name(name):
    """Names can't be empty, have special characters, or numbers. 
    """
    if name == "" or name.isalpha()==False:
        return False
        

###SOPHIA LOOK UP WHAT THIS IS
# if __name__ == "__main__":
greet_user()
        
"""


def nicetomeet():
print ('It's nice to meet you,) + user_name.capitalize() + ("!")



def birthday():
print('When is your birthday?')
age = (CurrentYYYY - BirthYear)
print('You are')+ AGE + ('years old, and it has been') + LENGTH OF TIME + (' since your birthday.')
print('You are')+ AGE + ('years old, today is your birthday. Happy Birthday!')
print('You are')+ AGE + ('years old, and your birthday is coming up within 7 days! Happy early birthday!')

"""