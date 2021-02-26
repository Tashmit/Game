import random
import math
# Taking Inputs
def numguess():
    lower = int(input("Enter Lower bound:- "))

    # Taking Inputs
    upper = int(input("Enter Upper bound:- "))

    # generating random number between the lower and upper
    x = random.randint(lower, upper)
    print("\n\tYou've only ", round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")

    # Initializing the number of guesses.
    count = 0

    # for calculation of minimum number of guesses depends upon range
    while count < math.log(upper - lower + 1, 2):
        count += 1

        # taking guessing number as input
        guess = int(input("Guess a number:- "))

        # Condition testing
        if x == guess:
            print("Congratulations you did it in ", count, " try")
            # Once guessed, loop will break
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")

# If Guessing is more than required guesses, shows this output.
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is",x)
        print("\tBetter Luck Next time!")

# Print multiline instruction perform string concatenation of string
def RPS():
    print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")

    while True:
        print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")

    # take the input from user
        choice = int(input("User turn: "))

    # OR is the short-circuit operator if any one of the condition is true then it return True value

    # looping until user enter invalid input
        while choice > 3 or choice < 1:
            choice = int(input("enter valid input: "))


    # initialize value of choice_name variable corresponding to the choice value
        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'paper'
        else:
            choice_name = 'scissor'

    # print user choice
        print("user choice is: " + choice_name)
        print("\nNow its computer turn.......")

    # Computer chooses randomly any number among 1 , 2 and 3. Using randint method of random module
        comp_choice = random.randint(1, 3)

    # looping until comp_choice value is equal to the choice value
        while comp_choice == choice:
            comp_choice = random.randint(1, 3)

    # initialize value of comp_choice_name variable corresponding to the choice value
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'paper'
        else:
            comp_choice_name = 'scissor'

        print("Computer choice is: " + comp_choice_name)

        print(choice_name + " V/s " + comp_choice_name)

    # condition for winning
        if((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice ==1 )):
            print("paper wins => ", end = "")
            result = "paper"

        elif((choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
            print("Rock wins =>", end = "")
            result = "Rock"
        else:
            print("scissor wins =>", end = "")
            result = "scissor"

    # Printing either user or computer wins
        if result == choice_name:
            print("<== User wins ==>")
        else:
            print("<== Computer wins ==>")

        print("Do you want to play again? (Y/N)")
        ans = input()


    # if user input n or N then condition is True
        if ans == 'n' or ans == 'N':
            break

# after coming out of the while loop we print thanks for playing
    print("\nThanks for playing")

def wordguess(name):

# Here the user is asked to enter the name first

    print("Good Luck ! ", name)

    words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board']

# Function will choose one random word from this list of words
    word = random.choice(words)


    print("Guess the characters")

    guesses = ''

# any number of turns can be used here
    turns = 12


    while turns > 0:

    # counts the number of times a user fails
        failed = 0

    # all characters from the input word taking one at a time.
        for char in word:

        # comparing that character with the character in guesses
            if char in guesses:
                print(char)

            else:
                print("_")

            # for every failure 1 will be incremented in failure
                failed += 1


        if failed == 0:
        # user will win the game if failure is 0 and 'You Win' will be given as output
            print("You Win")
            break

        # this print the correct word
            #print("The word is: ", word)
            #break

    # if user has input the wrong alphabet then it will ask user to enter another alphabet
        guess = input("guess a character:")

    # every input character will be stored in guesses
        guesses += guess

    # check input with the character in word
        if guess not in word:
            turns -= 1

        # if the character doesn’t match the word then “Wrong” will be given as output
            print("Wrong")

        # this will print the number of turns left for the user
            print("You have", + turns, 'more guesses')


            if turns == 0:
                print("You Loose")
    print("The word was: ", word)

#Main menu
print('------------------------------Welcome to GameHub------------------------------')
name=input('What is your name?')
print('Hello',name)
ans='Y'
while ans== 'Y' or 'y' :
    print('Menu')
    print('1. Number Guess')
    print('2. Rock Paper Scissor')
    print('3. Word Guess')
    print('Enter your choice',name)
    choice=input()
    ch=int(choice)
#Choice selection
    if ch==1:
        numguess()
    elif ch==2:
        RPS()
    elif ch==3:
        wordguess(name)
    else:
        print('Wrong input....terminating')
        quit()
    print('Do you want to continue', name, '?(Y/N)')
    ans=input()
    if(ans == 'N' or 'n'):
        print('Thank You',name )
        quit()
#End of Code
