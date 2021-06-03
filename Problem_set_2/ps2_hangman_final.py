# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
          if letter not in letters_guessed:
                return False
    return True

    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

def get_guessed_word(secret_word, letters_guessed):
    word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word = word + letter
        else:
            word = word + "_ "
    return word


'''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
import string
print (string.ascii_lowercase)

def get_available_letters(letters_guessed):
      available_letters = list(string.ascii_lowercase)
      for letter in letters_guessed:
            available_letters.remove(letter)
      remaining_letters = "".join(available_letters)
      
      return remaining_letters
           
      #return available_letters
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

def hangman(secret_word):
    
    number_guesses = 6
    number_warnings = 3
    letters_guessed = []
    vowels = ["a", "e", "i", "o", "u"]
    print (f"""
    Loading word list from file...
    {(len(wordlist))} words loaded.
    Welcome to the game Hangman!
    I am thinking of a word that is {(len(secret_word))} letters long.
    {get_guessed_word(secret_word, letters_guessed)}

    --------------------------------
    You have {number_warnings} warnings remaining
    You have {number_guesses} guesses remaining
    Available letters: {get_available_letters(letters_guessed)}
    """)
    
    while True:
        letter_input = input("Please guess a letter: ").lower()
        if letter_input.isalpha():
            if (len(letter_input) != 1):
                print (f"""Only a single letter is allowed as an input""")
            if letter_input not in letters_guessed:
                letters_guessed.append(letter_input)
                print(f"""---------------------------------------
                """)
                if letter_input in secret_word:
                    print (f"""Good guess: {get_guessed_word(secret_word, letters_guessed)}
                    ----------------------------------------""")
                    if number_guesses == 1:
                        print(f"""You have {number_guesses} guess remaining
                        Available letters: {get_available_letters(letters_guessed)}
                        ----------------------------------------""")
                    else:
                        print(f"""You have {number_guesses} guesses remaining
                        Available letters: {get_available_letters(letters_guessed)}
                        ----------------------------------------""")
                elif letter_input in vowels:
                    number_guesses -=2
                    print(f"""Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}
                    ---------------------------------------""")
                    if number_guesses == 1:
                        print(f"""You have {number_guesses} guess remaining
                        Available letters: {get_available_letters(letters_guessed)}
                        ----------------------------------------""")
                    elif number_guesses <=0:
                        print(f"""
                        """)
                    else:
                        print(f"""You have {number_guesses} guesses remaining
                        Available letters: {get_available_letters(letters_guessed)}
                        ----------------------------------------""")
                else:
                    number_guesses -=1
                    print(f"""Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}
                    ---------------------------------------""")
                    if number_guesses == 1:
                        print(f"""You have {number_guesses} guess remaining
                        Available letters: {get_available_letters(letters_guessed)}
                        ----------------------------------------""")
                    elif number_guesses <=0:
                        print(f"""
                        """)
                    else:
                        print(f"""You have {number_guesses} guesses remaining
                        Available letters: {get_available_letters(letters_guessed)}
                        ----------------------------------------""")
            elif number_warnings > 2:
                number_warnings -=1
                print(f"""You have already guessed that letter. You lose one warning. You now have {number_warnings} warnings left.
                """)
            elif number_warnings ==2:
                number_warnings -=1
                print(f"""You have already guessed that letter. You lose one warning. You now have {number_warnings} warning left.
                """)
            elif number_warnings == 1:
                number_warnings -=1
                print(f"""You have already guessed that letter. You lose one warning. You now have {number_warnings} warnings left.
                """)
            elif number_guesses <=0:
                number_guesses -= 1
                print(f"""You have already guessed that letter and have used up all your warnings. You lose one guess.
                """)
        elif number_warnings > 2:
            number_warnings -=1
            print(f"""Oops! That is not a valid letter. You have {number_warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}
            """)
        elif number_warnings == 2:
            number_warnings -=1
            print (f"""Oops! That is not a valid letter. You have {number_warnings} warning left: {get_guessed_word(secret_word, letters_guessed)}.
                """)
        elif number_warnings == 1:
            number_warnings -=1
            print (f"""Oops! That is not a valid letter. You have {number_warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}.
            """)
        elif number_warnings <=0:
            number_guesses -=1
            print (f"""You have run out of warnings and have made an invalid input. You lose one guess.""")
        
        if is_word_guessed(secret_word, letters_guessed) and number_guesses >0:
            unique_letters = []
            for letter in secret_word:
                if letter not in unique_letters:
                    unique_letters.append(letter)
            print(f"""Congratulations. You have won.
            Your score for this game is {(number_guesses*len(unique_letters))}""")
            break
        if number_guesses <=0:
            print(f"""You have run out of guesses. The word was {secret_word}""")
            break

#secret_word = choose_word(wordlist)
#hangman(secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def match_with_gaps(my_word, other_word):
    guessed_letters = []
    for letter in my_word:
        if letter.isalpha():
            guessed_letters.append(letter)
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        my_word_letter = my_word[i]
        other_word_letter = other_word[i]
        if my_word_letter.isalpha() and my_word_letter != other_word_letter:
            return False
        else:
            if my_word_letter == "_" and other_word_letter in guessed_letters:
                return False
    return True

    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

wordlist = load_words()


def show_possible_matches(my_word):
    match = False
    matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches.append(word)
            match = True
    #if len(matches) == 0:
        #print ("No matches found")
    matches = " ".join(matches)
    if match:
        return matches
    else:
        print("No matches found")

def show_possible_matches(my_word):
    matches = ""
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            matches + word + " "
    return matches
    #if len(matches) == 0:
        #print ("No matches found")
    #if len(matches) > 0:
        #total_matches = " ".join(matches)
        #print(f"""Available matches are:
        #{total_matches}""")
    #if len(matches) == 0:
        #print("No matches found")

    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

def hangman_with_hints(secret_word):
    
    #secret_word = choose_word(wordlist)
    number_guesses = 6
    number_warnings = 3
    letters_guessed = []
    vowels = ["a", "e", "i", "o", "u"]
    print (f"""
    Loading word list from file...
    {(len(wordlist))} words loaded.
    Welcome to the game Hangman!
    I am thinking of a word that is {(len(secret_word))} letters long.
    {get_guessed_word(secret_word, letters_guessed)}

    --------------------------------
    You have {number_warnings} warnings remaining
    You have {number_guesses} guesses remaining
    Available letters: {get_available_letters(letters_guessed)}
    """)
    
    while True:
        letter_input = input("Please guess a letter: ").lower()
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if letter_input.isalpha():
            if (len(letter_input) != 1):
                print (f"""Only a single letter is allowed as an input""")
            if letter_input not in letters_guessed:
                letters_guessed.append(letter_input)
                print(f"""---------------------------------------
                """)
                if letter_input in secret_word:
                    print (f"""Good guess: {get_guessed_word(secret_word, letters_guessed)}
                    ----------------------------------------""")
                    if number_guesses == 1:
                        print(f"""You have {number_guesses} guess remaining
                        Available letters: {get_available_letters(letters_guessed)}
                        ----------------------------------------""")
                    else:
                        print(f"""You have {number_guesses} guesses remaining
                        Available letters: {get_available_letters(letters_guessed)}
                        ----------------------------------------""")
                elif letter_input in vowels:
                    number_guesses -=2
                    print(f"""Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}
                    ---------------------------------------""")
                    if number_guesses == 1:
                        print(f"""You have {number_guesses} guess remaining
                        Available letters: {get_available_letters(letters_guessed)}
                        ----------------------------------------""")
                    elif number_guesses <=0:
                        print(f"""
                        """)
                    else:
                        print(f"""You have {number_guesses} guesses remaining
                        Available letters: {get_available_letters(letters_guessed)}
                        ----------------------------------------""")
                else:
                    number_guesses -=1
                    print(f"""Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}
                    ---------------------------------------""")
                    if number_guesses == 1:
                        print(f"""You have {number_guesses} guess remaining
                        Available letters: {get_available_letters(letters_guessed)}
                        ----------------------------------------""")
                    elif number_guesses <=0:
                        print(f"""
                        """)
                    else:
                        print(f"""You have {number_guesses} guesses remaining
                        Available letters: {get_available_letters(letters_guessed)}
                        ----------------------------------------""")
            elif number_warnings > 2:
                number_warnings -=1
                print(f"""You have already guessed that letter. You lose one warning. You now have {number_warnings} warnings left.
                """)
            elif number_warnings ==2:
                number_warnings -=1
                print(f"""You have already guessed that letter. You lose one warning. You now have {number_warnings} warning left.
                """)
            elif number_warnings == 1:
                number_warnings -=1
                print(f"""You have already guessed that letter. You lose one warning. You now have {number_warnings} warnings left.
                """)
            elif number_guesses <=0:
                number_guesses -= 1
                print(f"""You have already guessed that letter and have used up all your warnings. You lose one guess.
                """)
        elif letter_input == "*":
            my_word = get_guessed_word(secret_word, letters_guessed)
            print(f"Possible word matches are: {show_possible_matches(my_word)}")
            #print(f"""{show_possible_matches(my_word)}""")
            #result = show_possible_matches(my_word)
            #print(f"""Possible matches are: {result}""")
            #print(f"""{get_guessed_word(secret_word, letters_guessed)}""")       
        elif number_warnings > 2:
            number_warnings -=1
            print(f"""Oops! That is not a valid letter. You have {number_warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}
            """)
        elif number_warnings == 2:
            number_warnings -=1
            print (f"""Oops! That is not a valid letter. You have {number_warnings} warning left: {get_guessed_word(secret_word, letters_guessed)}.
                """)
        elif number_warnings == 1:
            number_warnings -=1
            print (f"""Oops! That is not a valid letter. You have {number_warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}.
            """)
        elif number_warnings <=0:
            number_guesses -=1
            print (f"""You have run out of warnings and have made an invalid input. You lose one guess.""")
        
        if is_word_guessed(secret_word, letters_guessed) and number_guesses >0:
            unique_letters = []
            for letter in secret_word:
                if letter not in unique_letters:
                    unique_letters.append(letter)
            print(f"""Congratulations. You have won.
            Your score for this game is {(number_guesses*len(unique_letters))}""")
            break
        if number_guesses <=0:
            print(f"""You have run out of guesses. The word was {secret_word}""")
            break

secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)

    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#secret_word = choose_word(wordlist)
#hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
