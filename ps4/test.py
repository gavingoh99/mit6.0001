import string
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'
def build_transpose_dict(vowels_permutation):
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

print(apply_transpose(build_transpose_dict('eoaui')))