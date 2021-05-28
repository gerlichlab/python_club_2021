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
    for i in secret_word:
        if i not in letters_guessed:
            return(False)
    return(True)

    
    


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guess=[]
    for i in secret_word:
        if i in letters_guessed:
            guess.append(i)
        else:
            guess.append("_ ")           
    return(''.join(guess))




available_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    for i in letters_guessed:
      if i in available_letters:
        available_letters.remove(i)
    return(''.join(available_letters))

      
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
    #set initial variables for all rounds of guessing
    vowels = ['a', 'e', 'i', 'o', 'u']
    letters_guessed = []
    P = len(secret_word)
    number_of_guesses = 6
    number_of_warnings = 3
    total_score = 0
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {P} letters long')

    while True:

      #print things for user before the first guess
      print(f'You have {number_of_guesses} guesses left')
      print(f'You have {number_of_warnings} warnings left')
      print('The available letters are ' + get_available_letters(letters_guessed))


      #now get the user to provide a letter that hasn't been used before
      letters_guessed.append(str.lower(input('Please provide a letter:')))

      while True:                                                                             #this while loop should eliminate the possibility of entering something that's not a letter
        if letters_guessed[-1] not in available_letters:
          print('I said a letter!')
          letters_guessed.pop()
          number_of_warnings = number_of_warnings - 1
          print(f'You have  {number_of_warnings} warnings left')
          if number_of_warnings <= 0:
            number_of_guesses = number_of_guesses - 1
            print(f'You have lost one guess. Now you have {number_of_guesses}')
            number_of_warnings = 3
          if number_of_guesses <= 0:
            print('You have not managed to guess the word :(. Game over.')
            print('The secret word was' + secret_word)
            break
          letters_guessed.append(str.lower(input('Try again:')))
        else:
          break

      while True:                                                                            #this while loop should eliminate the possibilty of entering the same letter twice
        if letters_guessed[-1] not in available_letters:
          print('You are trying a letter you already used!')
          letters_guessed.pop()
          number_of_warnings = number_of_warnings - 1
          print(f'You have {number_of_warnings} warnings left')
          if number_of_warnings <= 0:
            number_of_guesses = number_of_guesses - 1
            print(f'You have lost one guess. Now you have {number_of_guesses}')
            number_of_warnings = 3
          if number_of_guesses <= 0:
            print('You have not managed to guess the word :(. Game over.')
            print('The secret word was' + secret_word)
            break
          letters_guessed.append(str.lower(input('Try again:')))
        else:
          break

      #here is where you give the output of a round to the user
      if letters_guessed[-1] in secret_word:                                                #scenario: you guessed the letter
        print('Good guess!' + get_guessed_word(secret_word, letters_guessed))  

      elif letters_guessed[-1] in vowels:                                                   #you didn't guess the letter and you put in a vowel  
        print('Wrong guess!' + get_guessed_word(secret_word, letters_guessed))
        number_of_guesses = number_of_guesses - 2
      
      else:
        print('Wrong guess!' + get_guessed_word(secret_word, letters_guessed))              #you didn't guess the letter and you put in a consonant
        number_of_guesses = number_of_guesses - 1

      if number_of_guesses <=0:                                                             #check that there is still enough guesses to continue to the next round
        print('You have not managed to guess the word :(. Game over.')
        print('The secret word was ' + secret_word)
        break  
                  
      if is_word_guessed(secret_word,letters_guessed) == True:                              #check before entering a new round that the word is not yet guessed
        print('Great job, you guessed the word')
        total_score = number_of_guesses * len(secret_word)
        print(f"Your total score is {total_score}")  
        break    

      #end of the guessing round
      print('------------------------------------------------------------------------------')

  
      



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
    my_word = 'te_t'
    other_word = 'tact'
   
    
    if len(my_word) != len(other_word):                       
      return(False)
    
    for i in range(len(my_word)):
      current_letter = my_word(i)
      other_letter = other_word(i)
      if current_letter == other_letter:
        check = True
      elif (current_letter == "_") and (other_letter not in my_word):
        check = True
      else:
        check = False
        return(False)
    return(True)
    
  print(match_with_gaps(my_word, other_word))







      if my_word(i) == other_word(i):
        check == True
      elif (my_word(i) == '_') and (other_word(i) not in my_word):
        check == True
      else:
        check == False

    if check == False
      return(False)
    else:
      return(True)
      




    
        


         
   
    

  
     



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
    pass



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
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
