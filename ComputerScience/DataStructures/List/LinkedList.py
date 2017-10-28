class SinglyLinkedList:
    def __init__(self, data, node_next=None):
        self.data = data
        self.nextNode = node_next

    def set_next(self, linked_list):
        self.nextNode = linked_list
        linked_list.prevNode = self

    def set_data(self, data):
        self.data = data

    def __str__(self):
        return 'LinkedList node object Data: {0}, next: {1}'.format(self.data, self.nextNode)

    def print_list(self):
        cur = self
        while cur is not None:
            print('{0} -> '.format(cur.data), end='')
            cur = cur.nextNode
        print('None')

    def insert_last(self, lst):
        cur = self
        while cur.nextNode:
            cur = cur.nextNode
        cur.nextNode = lst


class DoublyLinkedList(SinglyLinkedList):
    def __init__(self, data, node_next=None, node_prev=None):
        SinglyLinkedList.__init__(self, data, node_next)
        self.prevNode = node_prev

    def set_prev(self, linked_list):
        self.prevNode = linked_list
        linked_list.nextNode = self

    def __str__(self):
        return 'DoublyLinkedList node object Data: {0}, next: {1}'.format(self.data, self.nextNode)

    def print_reverse(self):
        cur = self
        while cur.prevNode:
            print('{0} <-> '.format(cur.data), end='')
            cur = cur.prevNode
        print('{} -> None'.format(cur.data), end='')

    def print_list(self):
        cur = self
        print('None <- ', end='')
        while cur is not None:
            if cur.nextNode is None:
                print('{0} -> None'.format(cur.data), end='')
            else:
                print('{0} <-> '.format(cur.data), end='')
            cur = cur.nextNode
        print('')

    def insert_last(self, lst):
        cur = self
        while cur.nextNode:
            cur = cur.nextNode
        cur.nextNode = lst
        lst.prevNode = cur
