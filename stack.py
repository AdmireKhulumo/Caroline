# a manual implementation of a stack using a list
# specifically used for strings
from typing import List


class Stack:
    # initialise list to hold items
    def __init__(self):
        # initialise stack variable
        self.stack: List[str] = []

    # define a property for the stack -- works as a getter
    @property
    def stack(self) -> List[str]:
        return self._stack

    # define a setter for the property
    @stack.setter
    def stack(self, new_stack: List[str]) -> None:
        # ensure proper format
        if isinstance(new_stack, List):
            # assign private stack wit new value
            self._stack = new_stack
        else:
            # improper input, deny and raise an error
            raise ValueError("Must be a list of strings, i.e List[str]")

    # push method adds to top of stack
    def push(self, item: str) -> None:
        if type(item) == str:
            self.stack.append(item)
        else:
            raise ValueError("Must supply a string")

    # pop method removes from top of stack
    def pop(self) -> str:
        # get top item
        item: str = self.stack[-1]
        # delete top item
        del self.stack[-1]
        # return top item
        return item

    # peek method retrieves the item at the top of the stack without removing it
    def peek(self) -> str:
        return self.stack[-1]

    # size returns the number of elements in the stack
    def size(self) -> int:
        return len(self.stack)

    # check if the stack is empty
    def is_empty(self) -> bool:
        return len(self.stack) == 0

    # reverse method
    def reverse(self) -> None:
        # create a new stack
        new_stack: Stack = Stack()
        # iterate through current stack and push to new stack
        while not self.is_empty():
            new_stack.push(self.stack.pop())
        # assign new_stack to old_stack
        self.stack = new_stack.stack

    # dunder methods -- kinda unnecessary here to be honest
    # len works the same as size() above
    def __len__(self) -> int:
        return len(self.stack)

    # repr returns a string representation of the stack
    def __repr__(self) -> str:
        string: str = ''
        for item in self.stack:
            str += item
        return string
