import string
class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
    def is_phrase_in(self, text):
        text = text.lower()
        for char in string.punctuation:
            text = text.replace(char, ' ')
        word_list = text.split(' ')
        while '' in word_list:
            word_list.remove('')
        phrase_split = self.phrase.split()
        test = []
        for phrase in phrase_split:
            for count, word in enumerate(word_list):
                if phrase == word:
                    test.append(count)
        found = False
        if len(test) < len(phrase_split):
            found = False
        for i in range(len(test) - 1):
            #checks for the phrase appearing separate from one another i.e 
            #purple people love cows, if phrase is purple cow
            #test[i] = 0, test[i + 1] = 3
            if test[i + 1] - test[i] == 1:
                if word_list[test[i]] == phrase_split[0] and word_list[test[i + 1]] == phrase_split[1]:
                    found = True
        return found

x = PhraseTrigger('purple cow')
print(x.is_phrase_in('purplecowpurplecow'))