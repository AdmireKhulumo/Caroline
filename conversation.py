from stack import Stack

# keeps a record of what I say
user_stack: Stack = Stack()

# keeps a record of what Caroline says
c_stack: Stack = Stack()


# function to track a conversation by recording on the stack
def track_conversation(name: str, phrase: str) -> None:
    # check who said it, then add what they said
    if name == 'caroline':
        c_stack.push(phrase)
    else:
        user_stack.push(phrase)


# function to recall a conversation
def recall_conversation() -> None:
    # ensure that stacks arent empty -- if so, return
    if user_stack.is_empty() or c_stack.is_empty():
        print('We haven\'t had a conversation yet.')
        return
    # reverse both stacks first
    user_stack.reverse()
    c_stack.reverse()
    # string to hold conversation
    convo: str = ''
    # recount, starting with user -- i.e user spoke first, and Caroline last
    while not c_stack.is_empty():
        # get what user said, then what C said, add to output string
        convo += f'You said "{user_stack.pop()}". Then I replied "{c_stack.pop()}". '
    # make C say it out -- import inline to prevent circular import
    from caroline_speech import talk
    talk(convo)

