"""
    Created by Maor Goaz @ 28/10/2017
    Visit my github page @ https://github.com/maorgo
"""
from ComputerScience.DataStructures.List.LinkedList import DoublyLinkedList


# Doubly linked list
def test_doubly_linked_list():
    print('Testing DoublyLinkedList class:')
    doubly_linked_list = DoublyLinkedList(12)
    print('\tStarting with first value as 10: {}'.format(doubly_linked_list.data))
    l1 = DoublyLinkedList(5)
    l2 = DoublyLinkedList(9)
    l3 = DoublyLinkedList(6)
    doubly_linked_list.insert_last(l1)
    print('\tAdding new node with data 4: {}'.format(doubly_linked_list.nextNode.data))
    doubly_linked_list.insert_last(l2)
    print('\tAdding new node with data 4: {}'.format(doubly_linked_list.nextNode.data))
    doubly_linked_list.insert_last(l3)
    print('\tAdding new node with data 4: {}'.format(doubly_linked_list.nextNode.data))
    print('\tDoublyLinkedList.print_list: ', end='')
    doubly_linked_list.print_list()
    print('\tDoublyLinkedList.print_reverse: ', end='')
    l3.print_reverse()
    print('\n\t{}'.format(doubly_linked_list.__str__()))

if __name__ == '__main__':
    test_doubly_linked_list()
