#!/usr/local/bin/python3


class SingleLinkedList:
    class Node:
        def __init__(self, value=None):
            self.value = value
            self.nextNode = None
        
        def __str__(self):
            return str(self.value)
        
        def __repr__(self):
            return self.__str__()

    class LinkedListIterator:
        def __init__(self, head):
            self.current = head

        def __iter__(self):
            return self
    
        def __next__(self):
            if self.current == None:
                raise StopIteration
            else:
                current = self.current
                self.current = self.current.nextNode
                return current
        
        def next(self):
            return self.__next__()    
        
    def __init__(self):
        self.headNode = None
        self.lastNode = None
        self.length = 0

    def __len__(self):
        return self.length

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

    def __search(self, value):
        current = self.headNode
        found = False
        index = 0

        while current and not found:
            if current.value == value:
                found = True
            else:
                current = current.nextNode
                index += 1
        if not current:
            return None
        return current, index

    def search(self, value):
        """
        Searches the list for a node with payload value. Returns the node object or None if not found.
        """
        response = self.__search(value)
        if not response:
            return None
        return response[0]

    def indexOf(self, value):
        """
        Searches the list for a node with payload value. Returns the index of the object or None if not found.
        """
        response = self.__search(value)
        if not response:
            return None
        return response[1]

    def delete(self, value):
        """
        Deletes a node from the list with the provided payload value. Returns the node object or None if not found.
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


def main():
    linkedList = SingleLinkedList()

    alphabetList = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
    for letter in alphabetList:
        linkedList.append(letter)
    print(linkedList)
    # linkedList[-1] = "abc"
    # print(linkedList)

    # import copy 
    # linkedList2 = copy.deepcopy(linkedList)
    # del linkedList2[0]
    # print(linkedList2)

    # linkedList2 = copy.deepcopy(linkedList)
    # del linkedList2[-1]
    # print(linkedList2)

    # linkedList2 = copy.deepcopy(linkedList)
    # del linkedList2[25]
    # print(linkedList2)
    
    # linkedList2 = copy.deepcopy(linkedList)
    # del linkedList2[1]
    # print(linkedList2)
    print(linkedList.delete("a"))
    del linkedList[0]
    print(linkedList)

if __name__ == "__main__":
    main()