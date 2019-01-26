'''Linked List Python3 Implementation
'''

from typing import Any, List


class LinkedListNode(object):
    def __init__(self, value: Any):
        self.value = value
        self.next = None

    def __repr__(self)->str:
        if self.next:
            return f'{self.value}->{self.next}'
        else:
            return f'{self.value}->None'


class LinkedList(object):
    def __init__(self, values: List[Any]):
        """
        Generate LinkedList from dynamic array list
        """
        if len(values) < 1:
            self.head = None
        else:
            self.head = LinkedListNode(values[0])
            current = self.head
            for value in values[1:]:
                next_node = LinkedListNode(value)
                current.next = next_node
                current = next_node

    def __len__(self)->int:
        length = 0
        current = self.head
        while current != None:
            current = current.next
            length += 1
        return length
