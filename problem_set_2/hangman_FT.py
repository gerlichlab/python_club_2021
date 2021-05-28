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
    inFile = open(WORDLIST_FILENAME, "r")
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
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """

    secret_word_guessed = ""
    for letter in secret_word:
        if letter not in letters_guessed:
            secret_word_guessed += "_"
        else:
            secret_word_guessed += letter

    return secret_word_guessed


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """

    available_letters = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters += letter

    return available_letters


def hangman(secret_word):
    """
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
    """

    guesses = 6
    warnings = 3
    letters_guessed = []
    vowels = "aeiou"

    print(
        f"Welcome to the game Hangman!\n"
        f"I am thinking of a word that is {(len(secret_word))} letters long \n"
        f"-------------"
    )

    while True:
        print(
            f"You have {guesses} guesses left\n"
            f"Available letters: {get_available_letters(letters_guessed)}\n"
        )

        letter_input = input(f"Please enter a letter: ").lower()

        if letter_input.isalpha():
            if letter_input not in letters_guessed:
                letters_guessed.append(letter_input)
                guessed_word = get_guessed_word(secret_word, letters_guessed)

                if letter_input in secret_word:
                    print(f"Good guess: {guessed_word}")
                else:
                    if letter_input in vowels:
                        guesses -= 2
                    else:
                        guesses -= 1
                    print(f"Oops! That letter is not in my word: {guessed_word}")
            else:
                if warnings > 0:
                    warnings -= 1
                    print(
                        f"Oops! You've already guessed that letter. You now have {warnings} warnings: {guessed_word}"
                    )
                else:
                    guesses -= 1
                    print(
                        f"Oops! You've already guessed that letter. You now have no warnings left so you lose one guess: {guessed_word}"
                    )

        else:
            if warnings > 0:
                warnings -= 1
                print(
                    f"Oops! That is not a valid letter. You have {warnings} warnings left: {guessed_word}"
                )
            else:
                guesses -= 1
                print(
                    f"Oops! You've already guessed that letter. You now have no warnings left so you lose one guess: {guessed_word}"
                )

        print("-------------")

        if is_word_guessed(secret_word, letters_guessed):
            unique_letters = []
            for letter in secret_word:
                if letter not in unique_letters:
                    unique_letters.append(letter)

            print(
                f"Congratulations, you won!\n"
                f"Your total score for this game is {guesses*len(unique_letters)}"
            )
            break

        if guesses <= 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}")
            break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    for letter in my_word:
        if letter.isalpha():
            letters_guessed.append(letter)
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        current_word_letter = my_word[i]
        other_word_letter = other_word[i]
        if current_word_letter.isalpha():
            same_letter = current_word_letter == other_word_letter
            if not same_letter:
                return False
        else:
            if current_word_letter == "_" and other_word_letter in letters_guessed:
                return False
    return True


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    match = False
    matched_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched_words.append(word)
            match = True
    matched_words = ", ".join(matched_words)
    if match:
        return {matched_words}
    else:
        print("No matches found")


def hangman_with_hints(secret_word):
    """
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
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 3
    letters_guessed = []
    vowels = "aeiou"

    print(
        f"Welcome to the game Hangman!\n"
        f"I am thinking of a word that is {(len(secret_word))} letters long \n"
        f"-------------"
    )

    while True:
        print(
            f"You have {guesses} guesses left\n"
            f"Available letters: {get_available_letters(letters_guessed)}\n"
            f"You can the character * to get a hint!\n"
        )

        letter_input = input(f"Please enter a letter: ").lower()
        guessed_word = get_guessed_word(secret_word, letters_guessed)

        if letter_input.isalpha():
            if letter_input not in letters_guessed:
                letters_guessed.append(letter_input)
                guessed_word = get_guessed_word(secret_word, letters_guessed)

                if letter_input in secret_word:
                    print(f"Good guess: {guessed_word}")
                else:
                    if letter_input in vowels:
                        guesses -= 2
                    else:
                        guesses -= 1
                    print(f"Oops! That letter is not in my word: {guessed_word}")
            else:
                if warnings > 0:
                    warnings -= 1
                    print(
                        f"Oops! You've already guessed that letter. You now have {warnings} warnings: {guessed_word}"
                    )
                else:
                    guesses -= 1
                    print(
                        f"Oops! You've already guessed that letter. You now have no warnings left so you lose one guess: {guessed_word}"
                    )
        elif letter_input == "*":
            print(f"Possible word matches are: {show_possible_matches(guessed_word)}")
        else:
            if warnings > 0:
                warnings -= 1
                print(
                    f"Oops! That is not a valid letter. You have {warnings} warnings left: {guessed_word}"
                )
            else:
                guesses -= 1
                print(
                    f"Oops! You've already guessed that letter. You now have no warnings left so you lose one guess: {guessed_word}"
                )

        print("-------------")

        if is_word_guessed(secret_word, letters_guessed):
            unique_letters = []
            for letter in secret_word:
                if letter not in unique_letters:
                    unique_letters.append(letter)

            print(
                f"Congratulations, you won!\n"
                f"Your total score for this game is {guesses*len(unique_letters)}"
            )
            break

        if guesses <= 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}")
            break


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
