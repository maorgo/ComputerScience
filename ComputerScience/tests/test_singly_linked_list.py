"""
    Created by Maor Goaz @ 28/10/2017
    Visit my github page @ https://github.com/maorgo

    This file is intended to test the DS implemented in the DataStructures module.
"""

from ComputerScience.DataStructures.List.LinkedList import SinglyLinkedList


# This is the linked list testing part
def test_singly_linked_list():
    # Singly linked list
    print('Testing SinglyLinkedList class:')
    singly_linked_list = SinglyLinkedList(10)
    print('\tStarting with first value as 10: {}'.format(singly_linked_list.data))
    sl1 = SinglyLinkedList(4)
    sl2 = SinglyLinkedList(1)
    sl3 = SinglyLinkedList(2)
    singly_linked_list.insert_last(sl1)
    print('\tAdding new node with data 4: {}'.format(singly_linked_list.nextNode.data))
    singly_linked_list.insert_last(sl2)
    print('\tAdding new node with data 1: {}'.format(singly_linked_list.nextNode.nextNode.data))
    singly_linked_list.insert_last(sl3)
    print('\tAdding new node with data 2: {}'.format(singly_linked_list.nextNode.nextNode.nextNode.data))
    print('\tSinglyLinkedList.print_list: ', end='')
    singly_linked_list.print_list()
    print('')


if __name__ == '__main__':
    test_singly_linked_list()
