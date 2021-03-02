from typing import List

import speech_recognition as sr
import pywhatkit as pwk
import datetime as dt
import wikipedia as wiki
import pyjokes as jokes
from compliments import compliments
import random
import sys
from caroline_speech import talk
from conversation import track_conversation, recall_conversation

# initialise listener event
listener = sr.Recognizer()


# get a command from person
def get_command() -> str:
    try:
        # use microphone as audio source
        with sr.Microphone() as source:
            print('Caroline 👱🏾: Speak Now 🗣 ...')
            # listen to mic source
            voice = listener.listen(source, phrase_time_limit=4)
            # store recognised speech
            command: str = listener.recognize_google(voice)
            command = command.lower()
            # check if name is mentioned
            if 'caroline' in command:
                print("You 🤓: " + command)
                # track this conversation point
                track_conversation('user', command)
                # remove name from command
                command = command.replace('caroline', '')
                # return spoken command to caller
                return command
            else:
                print("You 🤓: " + command)
                return 'empty'
    except Exception as e:
        print(e)


# checks if any word in a list is in the command
def check_in(words: List[str], command: str) -> bool:
    return any(x in command for x in words)


def start_caroline():
    command: str = get_command()
    # check if not empty
    if type(command) == 'NoneType':
        print('No command.')
        start_caroline()
    # play a song
    elif 'play' in command:
        # remove keyword
        title: str = command.replace('play', '')
        talk('Now Playing: ' + title)
        pwk.playonyt(title)
    # tell the time
    elif 'the time' in command:
        time: str = dt.datetime.now().strftime('%H:%M %p')
        talk('Current Time Is: ' + time)
    # wikipedia search
    elif 'wiki' in command:
        query: str = command.replace('wiki', '')
        result = wiki.summary(query, 1)
        talk(result)
    elif 'joke' in command:
        talk(jokes.get_joke())
    elif 'compliment' in command or 'sweet' in command:
        talk(random.choice(compliments))
    # googling feature
    elif 'search' in command:
        query: str = command.replace('search', '')
        talk('Searching for ' + query)
        pwk.search(query)
    elif 'why' in command and 'lonely' in command:
        talk('You code too much, you have no life. Live a little! '
             'Woza weekend should not be spent at the lab! Improve!')
    # recount last conversation
    elif check_in(['recount', 'recall', 'repeat'], command) and check_in(['talk', 'conversation'], command):
        talk("Okay, let me do that.")
        recall_conversation()
    # stop execution
    elif 'bye' in command:
        talk("Awesome, catch you later!")
        sys.exit()
    # in all other cases
    else:
        talk('You are very sweet, but that is not a valid command.')


if __name__ == '__main__':
    # startup caroline in an infinite loop
    while True:
        start_caroline()
