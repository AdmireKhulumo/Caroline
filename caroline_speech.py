# for things that Caroline must say
import pyttsx3 as tts

# initialise text to speech engine
engine = tts.init()
# set speed to 75%
engine.setProperty('rate', 75)
# set voice to female
engine.setProperty('voice', "com.apple.speech.synthesis.voice.samantha")


# Caroline's text response
def text_reply(text: str) -> None:
    print('Caroline 👱🏾: ' + text)


# Caroline's audio response
def talk(text: str) -> None:
    # write out what she's saying
    text_reply(text)
    # track what she's saying for recall_conversation
    # import inline to prevent circular import
    from conversation import track_conversation
    track_conversation('caroline', text)
    # actually say something in audio
    engine.say(text)
    engine.runAndWait()
