"""
    Created by Maor Goaz @ 28/10/2017
    Visit my github page @ https://github.com/maorgo
"""
from ComputerScience.DataStructures.Stack import Stack


def test_stack():
    # This is the stack testing part
    s = Stack()
    s.push(5)
    s.push(8)
    print(s.top())
    print(s.stack_size())
    s.pop()
    print(s.stack_size())

if __name__ == '__main__':
    test_stack()
