# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

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


# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())
    

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, time):
        format = "%d %b %Y %H:%M:%S"
        time = datetime.strptime(time, format)
        time = time.replace(tzinfo=pytz.timezone("EST"))
        self.time = time
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)
    def evaluate(self, story):
        return self.time > story.get_pubdate().replace(tzinfo=pytz.timezone('EST'))

class AfterTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)
    def evaluate(self, story):
        return self.time < story.get_pubdate().replace(tzinfo=pytz.timezone('EST'))

# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
    def evaluate(self, story):
        return not self.trigger.evaluate(story)


# Problem 8
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    result_stories = []
    for newsstory in stories:
        for trigger in triggerlist:
            if trigger.evaluate(newsstory):
                result_stories.append(newsstory)
                break
    return result_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    # trigger_file = open(filename, 'r')
    # list_of_triggers_to_add = []
    # resultant_list = []
    # list_of_triggers_added = []
    # trigger_type_dict = {}
    # not_and_or_dict = {}
    # phrase_or_time_dict = {}
    # for line in trigger_file:
    #     line = line.rstrip()
    #     if not (len(line) == 0 or line.startswith('//')):
    #         words_of_line = line.split(',')
    #         if words_of_line[0] == 'ADD':
    #             for i in range(1, len(words_of_line)):
    #                 list_of_triggers_to_add.append(words_of_line[i])
    #         else:
    #             if words_of_line[1] == 'TITLE':
    #                 trigger_type_dict[words_of_line[0]] = 'PHRASE'
    #                 phrase_or_time_dict[words_of_line[0]] = words_of_line[2]
    #             elif words_of_line[1] == 'DESCRIPTION':
    #                 trigger_type_dict[words_of_line[0]] = 'DESCRIPTION'
    #                 phrase_or_time_dict[words_of_line[0]] = words_of_line[2]
    #             elif words_of_line[1] == 'BEFORE':
    #                 trigger_type_dict[words_of_line[0]] = 'BEFORE'
    #                 phrase_or_time_dict[words_of_line[0]] = words_of_line[2]
    #             elif words_of_line[1] == 'AFTER':
    #                 trigger_type_dict[words_of_line[0]] = 'AFTER'
    #                 phrase_or_time_dict[words_of_line[0]] = words_of_line[2]
    #             elif words_of_line[1] == 'NOT':
    #                 trigger_type_dict[words_of_line[0]] = 'NOT'
    #                 not_and_or_dict[words_of_line[0]] = words_of_line[2]
    #             elif words_of_line[1] == 'AND':
    #                 trigger_type_dict[words_of_line[0]] = 'AND'
    #                 not_and_or_dict[words_of_line[0]] = (words_of_line[2], words_of_line[3])
    #             elif words_of_line[1] == 'OR':
    #                 trigger_type_dict[words_of_line[0]] = 'OR'
    #                 not_and_or_dict[words_of_line[0]] = (words_of_line[2], words_of_line[3])
    # for trigger in list_of_triggers_to_add:
    #     for key in trigger_type_dict.keys():
    #         if trigger == key:
    #             type_of_trigger = trigger_type_dict[key]
    #             if type_of_trigger == 'TITLE':
    #                 key = TitleTrigger(phrase_or_time_dict[key])
    #             elif type_of_trigger == 'DESCRIPTION':
    #                 key = DescriptionTrigger(phrase_or_time_dict[key])
    #             elif type_of_trigger == 'BEFORE':
    #                 key = BeforeTrigger(phrase_or_time_dict[key])
    #             elif type_of_trigger == 'AFTER':
    #                 key = AfterTrigger(phrase_or_time_dict[key])
    #             else: 
    #                 break
    #             resultant_list.append(key)
    #             list_of_triggers_added.append(trigger)
    #             break
    # for trigger in list_of_triggers_to_add:
    #     if trigger not in list_of_triggers_added:
    #         for key in trigger_type_dict.keys():
    #             if trigger == key:
    #                 type_of_trigger = trigger_type_dict[key]
    #                 if type_of_trigger == 'NOT':
    #                     key = NotTrigger(resultant_list[not_and_or_dict[key]])
    #                 elif type_of_trigger == 'AND':
    #                     key = AndTrigger(resultant_list[not_and_or_dict[key]])
    #                 elif type_of_trigger == 'OR':
    #                     key = OrTrigger(resultant_list[not_and_or_dict[key]])
    #                 resultant_list.append(key)
    #                 break
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    trig_dict = {}
    trig_list = []
    for i in range(len(lines)):
        trig = lines[i].split(',')
        if trig[1] == 'TITLE':
            trig_dict[trig[1]] = TitleTrigger(trig[2])
        elif trig[1] == 'DESCRIPTION':
            trig_dict[trig[1]] = DescriptionTrigger(trig[2])
        elif trig[1] == 'BEFORE':
            trig_dict[trig[1]] = BeforeTrigger(trig[2])
        elif trig[1] == 'AFTER':
            trig_dict[trig[1]] = AfterTrigger(trig[2])
    for i in range(len(lines)):
        trig = lines[i].split(',')    
        if trig[1] == 'NOT':
            trig_dict[trig[1]] = NotTrigger(trig_dict[trig[2]])
        elif trig[1] == 'AND':
            trig_dict[trig[1]] = AndTrigger(trig_dict[trig[2]], trig_dict[trig[3]])
        elif trig[1] == 'OR':
            trig_dict[trig[1]] = OrTrigger(trig_dict[trig[2]], trig_dict[trig[3]])
        elif trig[0] == 'ADD':
            for i in range(1, len(trig)):
                trig_list.append(trig_dict[trig[i]])
    return trig_list

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers




SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

