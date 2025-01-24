"""HANGMAN!"""

import random

#difficulties

a_hundred_attemtps_attempts = 100
easy_attempts = 20
normal_attempts = 15
expert_attempts = 10
super_expert_attempts = 5

difficulties = ["100_attempts", "easy", "normal", "expert", "super_expert"]

max_attempt = a_hundred_attemtps_attempts

#scores

win = False

attempt = 1
wrong_letters = []

#words
list_of_underscores = []

def choose_random_word():
    """This function chooses a random word from 'words.txt'.
    Due to it's scrambledness, we need to separate the text document line by line
    into lines, then choose a random line, then a word in the line using str.split()"""

    lines = []
    
    with open('words.txt', 'r') as words:
        for line in words:
            lines.append(line)
            
        random_line = random.choice(lines)
        _word = random.choice(random_line.split())

        for c in range(len(_word)):
            list_of_underscores.append("_")

        return _word

word = choose_random_word()

split_word = list(word)

#cool font
def intro():
    """'Cool' intro with text 'HANGMAN!' to give a weird 'font'
    All credit to JoonaFinland in YouTube.

    intro()

    |
    v

    prints

    |
    v

    |  |  /\  |\ |  /\ |\/|  /\  |\ | |
    |--| |--| | \| | ┐ |  | |--| | \| |
    |  | |  | |  |  \/ |  | |  | |  | *
    Made possible by: JoonaFinland
    """
    
    print("|  |  /\  |\ |  /\ |\/|  /\  |\ | |")
    print("|--| |--| | \| | ┐ |  | |--| | \| |")
    print("|  | |  | |  |  \/ |  | |  | |  | *")
    print("Made possible by: JoonaFinland \n")

#difficulty setup
def difficulty_setup():
    """Chooses the difficulty for the game, depending on the player's answer in the console.
    It asks the player to select a difficulty, and if the input 'ans' is
    not a difficulty, the game starts 100 attempts."""

    global attempt
    global max_attempt
    
    
    ans = input("Choose a difficulty: [100_attempts, easy, normal, expert or super_expert]")
    if str(ans) in difficulties and ans.lower() == "easy":
        max_attempt = easy_attempts
    elif str(ans) in difficulties and ans.lower() == "normal":
        max_attempt = normal_attempts
    elif str(ans) in difficulties and ans.lower() == "expert":
        max_attempt = expert_attempts
    elif str(ans) in difficulties and ans.lower() == "super_expert":
        max_attempt = super_expert_attempts
    elif str(ans) in difficulties and ans.lower() == "100_attempts":
        max_attempt = a_hundred_attemtps_attempts
    else:
        print("Sorry, that is not a difficulty... Starting on 100_attempts mode...")

#main game
def main():
    """The main part of the game.

    It's a for loop that determines if the answer is a letter (one letter long) and correct,
    incorrect, if the answer is an incorrect word, or if the whole word has been guessed.
    Each time they guess, they'll see something like this:
    
    ___________________________________________________
    Attempt: 3/100
    length: 4
    WORD: W _ _ _
    WRONG LETTERS: e, f, w
    >>>

    """

    global split_word
    global list_of_underscores
    global max_attempt
    global attempt
    global win
    
    for times in range(max_attempt):
        print("___________________________________________________")
        print("Attempt: ", str(attempt) + "/" + str(max_attempt))
        print("length: " + str(len(word)))
        print("WORD: ", " ".join(list_of_underscores))
        print("WRONG LETTERS: ", ", ".join(wrong_letters))

        answer = input(">>>")

        if answer:       
            if len(answer) == 1 and answer.lower() in split_word: #if they guessed a correct letter
                print("CORRECT!")
                attempt = attempt + 1

                for i in range(len(word)): #Adds the letter to the 'list_of_underscores' list.
                    if word[i] == answer.lower():
                        list_of_underscores[i] = answer.upper()

                if "_" not in list_of_underscores: #if they guessed the last letter of the word
                    print("___________________________________________________")
                    print("YOU GUESSED THE WORD!!")
                    win = True
                    break

            elif len(answer) == 1 and answer.lower() not in split_word: #if they guessed a wrong letter
                print("INCORRECT!")
                if answer not in wrong_letters:
                    wrong_letters.append(answer.lower())
                attempt = attempt + 1
                
            elif answer.lower() == word: #if they guess the full word at once
                print("___________________________________________________")
                print("YOU GUESSED THE WORD!!")
                win = True
                break
            
            elif len(answer) != 1 and answer.lower() != word: #if they failed to guess the full word
                print("That's not the word!")
                attempt = attempt + 1
                
                for c in answer.lower():
                    if c not in wrong_letters and c not in split_word:
                        wrong_letters.append(c)
                        
            elif attempt == max_attempt and answer.lower() != word: #if they didn't clutch it out on the last attempt
                print("sorry, try again...")
                break
            
            else: #if... idek at this point...
                print("Sorry, try again...")
                attempt = attempt + 1

def check_for_win():
    """Checks for win or loss, and prints ending.
    The ending can look like this:

    ___________________________________________________

    YOU GUESSED THE WORD!!

    You won!
    The word was WORD!

    ___________________________________________________

    or like this:

    ___________________________________________________
    
    You did not guess the word...
    The word was WORD!

    ___________________________________________________"""
    
    if win:
        print("You won!")
    else:
        print("You did not guess the word...")

    print("The word was " + word.upper() + "!")

#game
intro()
difficulty_setup()
main()
check_for_win()
#game
