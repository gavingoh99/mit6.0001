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
    for char in secret_word:
        if char in letters_guessed:
          continue
        else:
          return False
          break
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    current_guess = []
    for char in secret_word:
      if char in letters_guessed:
        current_guess.append(char)
      else:
        current_guess.append('_ ')
    guessed_word = ''.join(current_guess)
    return guessed_word




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    remaining_letters = string.ascii_lowercase
    for char in letters_guessed:
        all_letters = remaining_letters[:]
        if char in all_letters:
            remaining_letters = remaining_letters.replace(char, "")
    return remaining_letters

    
    

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
    print('Welcome to the game Hangman!')
    x = secret_word
    tmp = []
    guess_remaining = 6
    warnings_remaining = 3
    print('I am thinking of a word that is', str(len(x)), 'letters long.')
    print('You have', warnings_remaining, 'warnings left.')
    word_in_list = list(x)
    sum_unique_letters = 0 
    for letter in word_in_list:
        if letter not in tmp:
            tmp.append(letter)
            sum_unique_letters += 1
        else:
            continue

    list_of_guessed_letters = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    while not is_word_guessed(x, list_of_guessed_letters):
        print('-' * 13)
        if guess_remaining == 0:
            print('Sorry, you ran out of guesses. The word was', x)
            break
        print('You have', guess_remaining, 'guesses left.')
        print('Available letters: ', get_available_letters(list_of_guessed_letters))
        raw_guess = str(input('Please guess a letter: '))
        if raw_guess.isalpha():
            current_letter_guess = raw_guess.lower()
            if current_letter_guess in list_of_guessed_letters:
                if warnings_remaining >= 1:
                    warnings_remaining -= 1
                    print('''Oops! You've already guessed that letter. You now have''', warnings_remaining, 'warnings left:', get_guessed_word(x, list_of_guessed_letters))
                else:
                    print('''Oops! You've already guessed that letter. You have no warnings left so you lose one guess:''', get_guessed_word(x, list_of_guessed_letters))
                    guess_remaining -= 1
            else:
                list_of_guessed_letters.append(current_letter_guess)
                if current_letter_guess in x:
                    print('Good guess:', get_guessed_word(x, list_of_guessed_letters))
                else:
                    print('Oops! That letter is not in my word:', get_guessed_word(x, list_of_guessed_letters))
                    if current_letter_guess in vowels:
                        guess_remaining -= 2
                    else:
                        guess_remaining -= 1
        elif not raw_guess.isalpha():
            if warnings_remaining >= 1:
                warnings_remaining -= 1
                print('Oops! That is not a valid letter. You have', warnings_remaining, 'warnings left:', get_guessed_word(x, list_of_guessed_letters))
                continue
            else:
                print('''Oops! You've already guessed that letter. You have no warnings left so you lose one guess:''', get_guessed_word(x, list_of_guessed_letters))
                guess_remaining -= 1
                continue
        
    if is_word_guessed(x, list_of_guessed_letters):
        print('-' * 13)
        print('Congratulations, you won!')
        score = guess_remaining * sum_unique_letters
        print('Your total score for this game is:', score)



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
    my_word = my_word.replace('_ ', "_", len(my_word))
    if len(my_word) != len(other_word):
        return False
    else:
        i = 0
        for char in my_word:
            if char == '_':
                i += 1
                continue
            elif char != other_word[i]:
                return False
            else:
                i += 1
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
    tmp = []
    for each_word in wordlist:
        if match_with_gaps(my_word, each_word):
            tmp.append(each_word)
        else:
            continue
    if tmp == []:
        x = 'No matches found'
        return x
    else:    
        possible_matches = ' '.join(tmp)
        return possible_matches



def hangman_with_hints(secret_word):
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
    print('Welcome to the game Hangman!')
    x = secret_word
    tmp = []
    guess_remaining = 6
    warnings_remaining = 3
    print('I am thinking of a word that is', str(len(x)), 'letters long.')
    print('You have', warnings_remaining, 'warnings left.')
    word_in_list = list(x)
    sum_unique_letters = 0 
    for letter in word_in_list:
        if letter not in tmp:
            tmp.append(letter)
            sum_unique_letters += 1
        else:
            continue

    list_of_guessed_letters = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    while not is_word_guessed(x, list_of_guessed_letters):
        print('-' * 13)
        if guess_remaining == 0:
            print('Sorry, you ran out of guesses. The word was', x)
            break
        print('You have', guess_remaining, 'guesses left.')
        print('Available letters: ', get_available_letters(list_of_guessed_letters))
        raw_guess = str(input('Please guess a letter: '))
        if raw_guess.isalpha():
            current_letter_guess = raw_guess.lower()
            if current_letter_guess in list_of_guessed_letters:
                if warnings_remaining >= 1:
                    warnings_remaining -= 1
                    print('''Oops! You've already guessed that letter. You now have''', warnings_remaining, 'warnings left:', get_guessed_word(x, list_of_guessed_letters))
                else:
                    print('''Oops! You've already guessed that letter. You have no warnings left so you lose one guess:''', get_guessed_word(x, list_of_guessed_letters))
                    guess_remaining -= 1
            else:
                list_of_guessed_letters.append(current_letter_guess)
                if current_letter_guess in x:
                    print('Good guess:', get_guessed_word(x, list_of_guessed_letters))
                else:
                    print('Oops! That letter is not in my word:', get_guessed_word(x, list_of_guessed_letters))
                    if current_letter_guess in vowels:
                        guess_remaining -= 2
                    else:
                        guess_remaining -= 1
        elif raw_guess == '*':
            results = show_possible_matches(get_guessed_word(x, list_of_guessed_letters))
            print('Possible word matches are:', results)
        elif not raw_guess.isalpha():
            if warnings_remaining >= 1:
                warnings_remaining -= 1
                print('Oops! That is not a valid letter. You have', warnings_remaining, 'warnings left:', get_guessed_word(x, list_of_guessed_letters))
                continue
            else:
                print('''Oops! You've already guessed that letter. You have no warnings left so you lose one guess:''', get_guessed_word(x, list_of_guessed_letters))
                guess_remaining -= 1
                continue
        
    if is_word_guessed(x, list_of_guessed_letters):
        print('-' * 13)
        print('Congratulations, you won!')
        score = guess_remaining * sum_unique_letters
        print('Your total score for this game is:', score)



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
