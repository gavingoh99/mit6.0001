# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = word_list
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        copy_valid_words = self.valid_words[:]
        return copy_valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        permutation_list = list(vowels_permutation)
        permutation_list_upper = list(vowels_permutation.upper())
        transpose_dict = {}
        all_letters = string.ascii_letters
        for letter in all_letters:
            if letter not in VOWELS_LOWER and letter not in VOWELS_UPPER:
                transpose_dict[letter] = letter
        
        for position, vowel in enumerate(VOWELS_LOWER):
            transpose_dict[vowel] = permutation_list[position] 
        for position, vowel in enumerate(VOWELS_UPPER):
            transpose_dict[vowel] = permutation_list_upper[position]
        return transpose_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        new_message = []
        message_in_list_form = list(self.message_text)
        for letter in message_in_list_form:
            for key in transpose_dict.keys():
                if letter == key:
                    letter = transpose_dict[key]
                    break
            new_message.append(letter)
        return ''.join(new_message)            
        
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        # we want a list of all possible permutations of the 5 vowels
        # given in this form [] using the get_permutation function defined in 4a
        # from there we can iterate through each permutation, passing the permutation
        # through the build_transpose_dict function and applying transpose to get a resultant text
        # we are returned a string which we can turn into a list split by ' ' and
        # iterate through checking with is_word and adding to a total count
        permutations_list = get_permutations(VOWELS_LOWER)
        print(permutations_list)
        total_wordcount = None
        best_permutation = None
        i = 0
        for permutation in permutations_list:
            current_transpose_dict = self.build_transpose_dict(permutation)
            decrypted_message = self.apply_transpose(current_transpose_dict)
            decrypted_in_list = decrypted_message.split()
            valid_wordcount = 0
            for word in decrypted_in_list:
                if is_word(word_list, word):
                    valid_wordcount += 1
            if not total_wordcount or valid_wordcount > total_wordcount:
                best_permutation = permutation
                total_wordcount = valid_wordcount 
        best_transpose_dict = self.build_transpose_dict(best_permutation)
        return self.apply_transpose(best_transpose_dict)

if __name__ == '__main__':
    word_list = load_words(WORDLIST_FILENAME)
    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    #TODO: WRITE YOUR TEST CASES HERE
    # message = SubMessage('Hairy Chest')
    # permutation = 'iauoe'
    # enc_dict = message.build_transpose_dict(permutation)
    # print("Original message:", message.get_message_text(), "Permutation:", permutation)
    # print("Expected encryption:", "Hiury Chast!")
    # print("Actual encryption:", message.apply_transpose(enc_dict))
    # enc_message = EncryptedSubMessage(message.apply_transpose((enc_dict)))
    # print('Decrypted message:', enc_message.decrypt_message())
    # program returns Hoary Chest instead since hoary is also a word in word_list