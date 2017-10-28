"""
    Created by Maor Goaz @ 29/10/2017
    Visit my github page @ https://github.com/maorgo
"""

from ComputerScience.DataStructures.Queue.queue import Queue


def test_queue():
    q = Queue(3)
    print('Queue should be empty: {0}'.format(q.is_empty()))
    q.enqueue(6)
    print('Pushing element 6: {0}'.format(q.dequeue()))
    q.enqueue(2)
    q.enqueue(1)
    q.enqueue(9)
    print('Queue shouldn\'t be empty: {0}'.format(q.is_empty()))
    print('Queue should be full: {0}'.format(q.is_full()))
    while not q.is_empty():
        print(q.dequeue())
    q.empty_queue()
    print('Queue should be empty: {0}'.format(q.is_empty()))

if __name__ == '__main__':
    test_queue()
