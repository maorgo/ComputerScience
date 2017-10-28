"""
    Created by Maor Goaz @ 28/10/2017
    Visit my github page @ https://github.com/maorgo
"""

""" A simple implementation of a queue. size limit is optional."""


class Queue:
    def __init__(self, size=None):
        self.size = size
        self.queue = []

    def enqueue(self, item):
        if self.size and self.size > len(self.queue):
            self.queue.append(item)
            return True
        elif self.size and self.size <= len(self.queue):
            return False
        else:
            self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            item = self.queue[0]
            del self.queue[0]
            return item
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        if self.size and self.size == len(self.queue):
            return True
        return False

    def empty_queue(self):
        if self.size:
            self.size = 0
        self.queue = []
