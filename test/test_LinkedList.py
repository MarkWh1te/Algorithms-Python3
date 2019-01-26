from datastructures.LinkedList import LinkedList

from random import randint


# utilities part TODO: move all utilities function to one place
log = print

# constant  for upper bound and lower bound
UPPER = 177
LOWER = 7


def get_random_int()->int:
    return randint(LOWER, UPPER)


#  test part
def test_random_linked_list():
    """
    test for generate random linked list
    """
    numbers = get_random_int()
    random_array = [get_random_int() for _ in range(numbers)]
    ll = LinkedList(random_array)
    assert len(ll) == len(random_array)
    log(ll.head)
    current = ll.head
    i = 0
    while i < len(random_array):
        assert current.value == random_array[i]
        current = current.next
        i += 1


def test_empty_list():
    """
    test for empty list
    """
    ll = LinkedList([])
    assert len(ll) == 0
    assert ll.head == None


def test_linked_list():
    for _ in range(97):
        test_random_linked_list()
    test_empty_list()
