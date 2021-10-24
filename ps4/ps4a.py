# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # permutations = []
    # if len(sequence) == 1:
    #         permutations.append(sequence)
    #         return permutations
    # else:
    #     front_letter = sequence[0]
    #     sequence = sequence[1:] #abc = bc #bc = c which would return base case ['c']
    #     list_of_permutations_of_base_case = get_permutations(sequence)
    #     permutations_of_previous_case = []
    #     if len(list_of_permutations_of_base_case[0]) > 1:
    #         for i in range(len(list_of_permutations_of_base_case)):
    #             tmp1 = front_letter + list_of_permutations_of_base_case[i]
    #             tmp2 = list_of_permutations_of_base_case[i] + front_letter
    #             permutations_of_previous_case.append(tmp1)
    #             permutations_of_previous_case.append(tmp2)
    #             for j in range(1, len(list_of_permutations_of_base_case[0])):
    #                 tmp3 = list_of_permutations_of_base_case[i][:j] + front_letter + list_of_permutations_of_base_case[i][j:]
    #                 permutations_of_previous_case.append(tmp3)
    #         return permutations_of_previous_case
    #     else:
    #         tmp1 = front_letter + list_of_permutations_of_base_case[0]
    #         tmp2 = list_of_permutations_of_base_case[0] + front_letter
    #         permutations_of_previous_case.append(tmp1)
    #         permutations_of_previous_case.append(tmp2)
    #         return permutations_of_previous_case
    if len(sequence) == 1:
        return [sequence]
    result = []
    #enumerate over 'abc'
    #first counter = 0, letter = 'a'
    #call get_permutation on sequence after slicing [:counter] + [counter+1:] 
    #means resultant string excludes the current letter so sequence argument
    #in get_permutation is now 'bc'
    #enumerate over 'bc'
    #first counter = 0, letter = 'b'
    #call get_perm on 'c' due to same string slicing
    #'c' lies in base case so this call of get_perm returns ['c']
    #now character = 'c' and recall in this call that letter = 'b'
    #so appends the concatenation 'b' + 'c' or 'bc' into results
    #enumerate continues so counter = 1, letter = 'c'
    #slicing to create 'b' passed as new sequence
    #returns ['b']
    #so character is now 'b' and letter is now 'c'
    #appends 'c' + 'b'
    #so now results contains ['bc', 'cb']
    #enumerate terminates and the result list is returned to the first internal call of get_perm
    #recall that firs counter = 0 and letter = 'a'
    #now iterates over the list of results returned 'bc' and 'cb'
    #concatenates 'a' and the two elements respectively and appends to new result list
    #enumerate moves to next counter = 1, letter = 'b'
    #repeats for the rest of letters 'b' and 'c' as for 'a'
    for counter, letter in enumerate(sequence):
        for character in get_permutations(sequence[:counter] + sequence[counter + 1:]):
            result = result + [letter + character]
    return result

        
        
    

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

