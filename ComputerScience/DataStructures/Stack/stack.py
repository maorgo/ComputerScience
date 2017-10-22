class Stack:
    def __init__(self, limit=None):
        self.stack = []
        self.limit = limit

    def __str__(self):
        return 'Stack implemented by python and a list.'

    def push(self, element):
        if len(self.stack) == self.limit:
            return False

        self.stack.append(element)
        return True

    def pop(self):
        if len(self.stack) == 0:
            return False
        element = self.stack[-1]
        del self.stack[-1]
        return element

    def top(self):
        if len(self.stack) == 0:
            return False
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
