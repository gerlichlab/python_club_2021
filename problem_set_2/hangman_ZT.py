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
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    l1 = list(secret_word)
    if all(i in letters_guessed for i in l1):
        return True
    False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_letters = []
    for i in secret_word:
        if i in letters_guessed:
          guessed_letters.append(i)
        else:
          guessed_letters.append("_")
    get_guessed = "".join(guessed_letters)
    return get_guessed


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters = string.ascii_lowercase
    available_letters = []
    for i in all_letters:
      if i not in letters_guessed:
        available_letters.append(i)
    return ''.join(available_letters)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    number_of_guesses = 6
    number_of_warnings = 3
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    print("Welcome to the game Hangman")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
   
   
    
    while True:
      print(f"You have {number_of_guesses} guesses left")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      print("--------------")
      guessed_letter = input("Please guess a letter: ").lower()
      
      if str.isalpha(guessed_letter):
        if guessed_letter in letters_guessed:
          number_of_warnings -= 1
          print(f"The letter has already been guessed. You have {number_of_warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
        
        else:
          letters_guessed.append(guessed_letter)
          
          if guessed_letter in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
          else:
            if guessed_letter in vowels:
              number_of_guesses -= 2
            else:
              number_of_guesses -= 1
            print(f"That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
      else:
        number_of_warnings -= 1
        print(f"""That is not a valid letter./n You have {number_of_warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}""")

      
      if is_word_guessed(secret_word, letters_guessed):
        unique_letters = []
        for i in secret_word:
          if i not in unique_letters:
            unique_letters.append(i)
        print(f"""Congratulations, you won!\n
        Your total score for this game is: {number_of_guesses*len(unique_letters)}""")
        break
    # 
      if number_of_guesses <= 0:
        print(f"""Sorry, you have run out of guesses and lost the game.
        The secret word was: {secret_word}""")
        break



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # create a list of words from worldlist which have the same length as my_word, and have the same characters at the same pos
    guessed_letters = []
    
    for letter in my_word:
      if letter.isalpha():
        guessed_letters.append(letter)
    
    if len(other_word) != len(my_word):
      return False
    
    for i in range(len(my_word)):
      my_letter = my_word[i]
      other_letter = other_word[i]
      if my_letter.isalpha() and my_letter != other_letter:
        return False
      else:
        if my_letter == "_" and other_letter in guessed_letters:
          return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches = []
    
    for match in wordlist:
      if match_with_gaps(my_word, match):
        matches.append(match)
    
    if len(matches) == 0:
      print("No matches found")
    
    if len(matches) > 0:
      return matches


def hangman_with_hints(secret_word):
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
    number_of_guesses = 6
    number_of_warnings = 3
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    print("Welcome to the game Hangman")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
   
    while True:
      print(f"You have {number_of_guesses} guesses left")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      print("--------------")
      guessed_letter = input("Please guess a letter: ").lower()
      
      if str.isalpha(guessed_letter):
        if guessed_letter in letters_guessed:
          number_of_warnings -= 1
          print(f"The letter has already been guessed. You have {number_of_warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
        
        else:
          letters_guessed.append(guessed_letter)
          
          if guessed_letter in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
          else:
            if guessed_letter in vowels:
              number_of_guesses -= 2
            else:
              number_of_guesses -= 1
            print(f"That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
      if guessed_letter == "*":
        if len(letters_guessed) > 0:
          my_word = get_guessed_word(secret_word, letters_guessed)
          matches = show_possible_matches(my_word)
          print("Possible matches are:")
          print(matches)
        if len(letters_guessed) == 0:
          print("You need to guess a letter first")
      else:
        number_of_warnings -= 1
        print(f"""That is not a valid letter.
        You have {number_of_warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}""")

      
      if is_word_guessed(secret_word, letters_guessed):
        unique_letters = []
        for i in secret_word:
          if i not in unique_letters:
            unique_letters.append(i)
        print(f"""Congratulations, you won!\n
        Your total score for this game is: {number_of_guesses*len(unique_letters)}""")
        break
    # 
      if number_of_guesses <= 0:
        print(f"""Sorry, you have run out of guesses and lost the game.
        The secret word was: {secret_word}""")
        break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    #secret_word = "star"
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
