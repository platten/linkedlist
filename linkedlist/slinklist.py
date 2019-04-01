#!/usr/local/bin/python3

import collections.abc


class SingleLinkedList(collections.abc.Sequence):
    class Node(collections.abc.Container):
        def __init__(self, value=None):
            self.value = value
            self.nextNode = None

        def __str__(self):
            return str(self.value)

        def __repr__(self):
            return self.__str__()

        def __contains__(self, value):
            if self.value == value:
                return True
            return False

    class LinkedListIterator(collections.abc.Iterator):
        def __init__(self, head):
            self.current = head

        def __iter__(self):
            return self

        def __next__(self):
            if self.current is None:
                raise StopIteration
            else:
                current = self.current
                self.current = self.current.nextNode
                return current

    def __init__(self):
        self.headNode = None
        self.lastNode = None
        self.length = 0

    def __len__(self):
        return self.length

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            if self.length != other.length:
                return False

            theSame = True
            selfIter = iter(self)
            otherIter = iter(other)
            for _ in range(0, self.length):
                if next(selfIter).value != next(otherIter).value:
                    theSame = False
                    break
            return theSame

    def __contains__(self, value):
        for element in iter(self):
            if element.value == value:
                return True
        return False

    def __add__(self, other):
        for element in other:
            self.append(element.value)

    def __iter__(self):
        return self.LinkedListIterator(self.headNode)

    def __str__(self):
        iterator = self.__iter__()
        return str(list(map(str, iterator)))

    def __getitem__(self, index):
        current = self.headNode
        if index >= 0:
            for _ in range(0, index):
                current = current.nextNode
                if not current:
                    raise IndexError("Index out of range")
            return current
        elif index == -1:
            return self.lastNode
        else:
            if -1 * index > self.length:
                raise IndexError("Index out of range")
            return self.__getitem__(index + self.length)

    def __setitem__(self, index, value):
        self.__getitem__(index).value = value

    def __delitem__(self, index):
        current = self.headNode
        previous = None

        if not current:
            raise IndexError("Index out of range")

        if index >= 0:
            for _ in range(0, index):
                if not current:
                    raise IndexError("Index out of range")
                previous = current
                current = current.nextNode
            if not previous:
                # Head node
                self.headNode = current.nextNode
            elif not current.nextNode:
                # Last node
                previous.nextNode = None
                self.lastNode = previous
            else:
                # Any other node in the middle
                previous.nextNode = current.nextNode
            del current
            self.length -= 1
        else:
            if -1 * index > self.length:
                raise IndexError("Index out of range")
            return self.__delitem__(index + self.length)

    def extend(self, other):
        self.__add__(other)

    def index(self, value, start=0, stop=None):
        # Returns first value of index. Will raise ValueError if not found.
        iterator = iter(self)
        index = 0
        for _ in range(0, start):
            next(iterator)
            index += 1
        while True:
            try:
                current = next(iterator)
            except StopIteration:
                raise ValueError

            if current.value == value:
                return index
            if stop is not None and index == stop:
                raise ValueError
            index += 1

    def count(self, value):
        counter = 0
        for element in self.__iter__():
            if element.value == value:
                counter += 1
        return counter

    def delete(self, value):
        """
        Deletes a node from the list with the provided payload value.
        Returns the node object or None if not found.
        """
        current = self.headNode
        previous = None
        found = False

        while current and not found:
            if current and current.value == value:
                found = True
                break
            previous = current
            current = current.nextNode

        if not current and not found:
            return None

        if not previous:
            # Head node
            self.headNode = current.nextNode
        elif not current.nextNode:
            # Last node
            previous.nextNode = None
            self.lastNode = previous
        else:
            # Any other node in the middle
            previous.nextNode = current.nextNode
        self.length -= 1
        return current

    def append(self, value):
        """
        Appends a node with the provided payload value.
        """
        node = self.Node(value)
        if not self.headNode:
            self.headNode = node
            self.lastNode = node
        else:
            self.lastNode.nextNode = node
            self.lastNode = self.lastNode.nextNode
        self.length += 1


def main():  # pragma: no cover
    linkedList = SingleLinkedList()

    alphabetList = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
    for letter in alphabetList:
        linkedList.append(letter)
    print(linkedList)


if __name__ == "__main__":  # pragma: no cover
    main()
