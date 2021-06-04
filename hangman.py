# Problem Set 2, hangman.py
# Name: Max Spicer
# Time spent: 15:40-

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
    print("  ", len(wordlist), "words loaded.\n")
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
    for i in secret_word:
      if i in letters_guessed:
        guessing_status = True
      else:
        guessing_status = False
    return guessing_status

#print(is_word_guessed("bind", ["b","i","n","a"]))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
    for i in secret_word:
      if i in letters_guessed:
        guessed_word = guessed_word + i
      else:
        guessed_word = guessed_word + "_ "
    return guessed_word

#print(get_guessed_word("bin bag", ["x","b","i","g"]))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    available_letters = string.ascii_lowercase
    for i in letters_guessed:
      if i in available_letters:
        available_letters = available_letters.replace(i,"")
    return available_letters

#print(get_available_letters("xbig"))

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
    
    #setting up limits for number of guesses and strikes
    guesses_remaining = 6
    strikes_remaining = 3
    guessed_letters = []
    print(f"Welcome to Hangman, the game.\nI am thinking of a word that is {len(secret_word)} letters long.")
    #hash out the below line when playing the game
    #print(secret_word)
    #entering the loop, which lasts until the number of guesses or strikes has expired
    while guesses_remaining > 0 and strikes_remaining > 0:
      print(f"You have {guesses_remaining} guesses remaining.\n-------------\nAvailable letters: {get_available_letters(guessed_letters)}")
      guess = input("Please guess a letter: ").lower()
    #in my version of hangman, the user can input the full word at any point to end the game
      if secret_word == guess:
            print(f"Congratulations, you guessed the word!\n Your score is {guesses_remaining*len(set(secret_word))}")
            break
      else:
        if guess.isalpha() is False:
          strikes_remaining -= 1
          print(f"Oops, that's not a letter, please try again.\nYou have {strikes_remaining} strikes remaining")
        elif guess in guessed_letters:
          strikes_remaining -= 1
          print(f"Oops, you already guessed that letter, please try again.\nYou have {strikes_remaining} strikes remaining")
        elif len(guess) != 1:
          strikes_remaining -= 1
          print(f"Oops, that's not a letter, please try again.\nYou have {strikes_remaining} strikes remaining")
        else:
          guessed_letters.append(guess)
          if guess in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, guessed_letters)}")          
          else:
            print(f"Bad luck, that letter is not in my word: {get_guessed_word(secret_word, guessed_letters)}")
            if guess in ("a", "e", "i", "o", "u"):
              print(f"And that's a vowel so you lose two guesses :(")
              guesses_remaining -= 2
            else:
              guesses_remaining -= 1
      if secret_word == get_guessed_word(secret_word,guessed_letters):
        print(f"Congratulations, you guessed the word!\n Your score is {guesses_remaining*len(set(secret_word))}")
        break
      if strikes_remaining == 0:
        print(f"If you play with fire, you're gonna get burnt - Game Over. \nThe word was {secret_word}")
      elif guesses_remaining == 0:
        print(f"Sorry, you ran out of guesses - Game Over. \nThe word was {secret_word}")

    

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
    import string
    stripped_word = my_word.translate({ord(c): None for c in string.whitespace})
    match_result = True
    if len(stripped_word) != len(other_word):
      match_result = False
    else:
      character_position = 0
      for i in stripped_word:
        if i.isalpha() == True:
          if i != other_word[character_position]:
            match_result = False
          character_position +=1
        else:
          character_position +=1
    return match_result
         
print(match_with_gaps("t_ _ _ _ _ a","tapioca"))




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
    possible_matches = []
    for i in wordlist:
      if match_with_gaps(my_word,i) == True:
        possible_matches.append(i)
    print(possible_matches)
    return possible_matches

show_possible_matches("t_ _ _ _ _ a")


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
    #setting up limits for number of guesses and strikes
    guesses_remaining = 6
    strikes_remaining = 3
    guessed_letters = []
    print(f"Welcome to Hangman, the game.\nI am thinking of a word that is {len(secret_word)} letters long.")
    #hash out the below line when playing the game
    #print(secret_word)
    #entering the loop, which lasts until the number of guesses or strikes has expired
    while guesses_remaining > 0 and strikes_remaining > 0:
      print(f"You have {guesses_remaining} guesses remaining.\n-------------\nAvailable letters: {get_available_letters(guessed_letters)}")
      guess = input("Please guess a letter: ").lower()
    #in my version of hangman, the user can input the full word at any point to end the game
      if secret_word == guess:
            print(f"Congratulations, you guessed the word!\n Your score is {guesses_remaining*len(set(secret_word))}")
            break
      else:
        if guess == "*":
          show_possible_matches(get_guessed_word(secret_word, guessed_letters))
        elif guess.isalpha() == False:
          strikes_remaining -= 1
          print(f"Oops, that's not a letter, please try again.\nYou have {strikes_remaining} strikes remaining")
        elif guess in guessed_letters:
          strikes_remaining -= 1
          print(f"Oops, you already guessed that letter, please try again.\nYou have {strikes_remaining} strikes remaining")
        elif len(guess) != 1:
          strikes_remaining -= 1
          print(f"Oops, that's not a letter, please try again.\nYou have {strikes_remaining} strikes remaining")
        else:
          guessed_letters.append(guess)
          if guess in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, guessed_letters)}")          
          else:
            print(f"Bad luck, that letter is not in my word: {get_guessed_word(secret_word, guessed_letters)}")
            if guess in ("a", "e", "i", "o", "u"):
              print(f"And that's a vowel so you lose two guesses :(")
              guesses_remaining -= 2
            else:
              guesses_remaining -= 1
      if secret_word == get_guessed_word(secret_word,guessed_letters):
        print(f"Congratulations, you guessed the word!\n Your score is {guesses_remaining*len(set(secret_word))}")
        break
      if strikes_remaining == 0:
        print(f"If you play with fire, you're gonna get burnt - Game Over. \nThe word was {secret_word}")
      elif guesses_remaining == 0:
        print(f"Sorry, you ran out of guesses - Game Over. \nThe word was {secret_word}")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
