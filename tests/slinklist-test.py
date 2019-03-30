#!/usr/local/bin/python3

import unittest

from context import linkedlist

class TestCreateSingleLinkedList(unittest.TestCase):
    def setUp(self):
        self.values = ("value 1", "value 2", "value 3")
        self.linkedList = linkedlist.SingleLinkedList()

    def test_empty(self):
        self.assertEqual(self.linkedList.headNode, None, "Head node for new list should be None")
        self.assertEqual(self.linkedList.lastNode, None, "Last node for new list should be None")
        self.assertEqual(self.linkedList.length, 0, "Length should be zero")

    def test_single_append(self):
        self.linkedList.append(self.values[0])

        self.assertNotEqual(self.linkedList.headNode, None, "Head node for new list should be created")
        self.assertEqual(self.linkedList.lastNode, self.linkedList.headNode, "Last node for new list should be same as head")
        self.assertEqual(self.linkedList.length, 1, "Length should be 1")
        self.assertEqual(self.linkedList.headNode.value, self.values[0], "value should be the same as the used in constructor")

    def test_double_append(self):
        self.linkedList.append(self.values[0])
        self.assertNotEqual(self.linkedList.headNode, None, "Head node for new list should be created")
        self.assertEqual(self.linkedList.lastNode, self.linkedList.headNode, "Last node for new list should be same as head")
        self.assertEqual(self.linkedList.length, 1, "Length should be 1")
        self.assertEqual(self.linkedList.headNode.value, self.values[0], "value should be the same as the used in constructor")

        self.linkedList.append(self.values[1])
        self.assertNotEqual(self.linkedList.headNode, None, "Head node for new list should be created")
        self.assertEqual(self.linkedList.headNode.nextNode, self.linkedList.lastNode, "Last node for new list should be same be after head")
        self.assertEqual(self.linkedList.headNode.value, self.values[0], "HeadNode value should not be changed")
        self.assertEqual(self.linkedList.headNode.nextNode.value, self.values[1], "Second node value should be the same as the used in constructor")
        self.assertEqual(self.linkedList.length, 2, "Length should be 2")

    def test_triple_append(self):
        self.linkedList.append(self.values[0])
        self.assertNotEqual(self.linkedList.headNode, None, "Head node for new list should be created")
        self.assertEqual(self.linkedList.lastNode, self.linkedList.headNode, "Last node for new list should be same as head")
        self.assertEqual(self.linkedList.length, 1, "Length should be 1")
        self.assertEqual(self.linkedList.headNode.value, self.values[0], "value should be the same as the used in constructor")

        self.linkedList.append(self.values[1])
        self.assertNotEqual(self.linkedList.headNode, None, "Head node for new list should be created")
        self.assertEqual(self.linkedList.headNode.nextNode, self.linkedList.lastNode, "Last node for new list should be same be after head")
        self.assertEqual(self.linkedList.headNode.value, self.values[0], "HeadNode value should not be changed")
        self.assertEqual(self.linkedList.headNode.nextNode.value, self.values[1], "Second node value should be the same as the used in constructor")
        self.assertEqual(self.linkedList.length, 2, "Length should be 2")

        self.linkedList.append(self.values[2])
        self.assertNotEqual(self.linkedList.headNode, None, "Head node for new list should be created")
        self.assertEqual(self.linkedList.headNode.nextNode.nextNode, self.linkedList.lastNode, "Last node for new list should be same as second node's nextNode")
        self.assertEqual(self.linkedList.headNode.value, self.values[0], "HeadNode value should not be changed")
        self.assertEqual(self.linkedList.headNode.nextNode.value, self.values[1], "Second node's value should not be changed")
        self.assertEqual(self.linkedList.headNode.nextNode.nextNode.value, self.values[2], "Third node value should be the same as the used in constructor")
        self.assertEqual(self.linkedList.length, 3, "Length should be 3")

    def test_equal(self):
        linkedList2 = linkedlist.SingleLinkedList()

        for value in self.values:
            self.linkedList.append(value)
            linkedList2.append(value)
        self.assertEqual(self.linkedList, linkedList2, "Values should be the same")

    def test_equal_same_object(self):
        for value in self.values:
            self.linkedList.append(value)
        anotherListReference = self.linkedList
        self.assertEqual(self.linkedList, anotherListReference, "Should be refering to the same object")

    def test_unequal_type(self):
        myString = "test string"
        for value in self.values:
            self.linkedList.append(value)
        self.assertNotEqual(self.linkedList, myString, "Linked list should not be equal to a string")

    def test_unequal_size(self):
        linkedList2 = linkedlist.SingleLinkedList()

        for value in self.values:
            self.linkedList.append(value)
            linkedList2.append(value)
        linkedList2.append("value 4")
        self.assertNotEqual(self.linkedList, linkedList2, "Link lists are not equal")

    def test_unequal_composition(self):
        linkedList2 = linkedlist.SingleLinkedList()

        for value in self.values:
            self.linkedList.append(value)
            
        linkedList2.append(self.values[0])
        linkedList2.append(self.values[1])
        linkedList2.append("different value")
        self.assertNotEqual(self.linkedList, linkedList2, "Link list content are different")

class TestGetSetDeleteItem(unittest.TestCase):
    def setUp(self):
        self.values = ("value 1", "value 2", "value 3")
        
        self.linkedList = linkedlist.SingleLinkedList()
        for value in self.values:
            self.linkedList.append(value)

        self.head_node = self.linkedList.headNode
        self.last_node = self.linkedList.lastNode
        self.second_node = self.linkedList.headNode.nextNode
        self.third_node = self.linkedList.headNode.nextNode.nextNode

    def test_getitem_first_node(self):
        self.assertEqual(self.linkedList[0], self.head_node, "Node with 0 index item should be the same as the head node")

    def test_getitem_second_node(self):
        self.assertEqual(self.linkedList[1], self.second_node, "Node with 1 index should be the same value as second node")

    def test_getitem_third_node(self):
        self.assertEqual(self.linkedList[2], self.third_node, "Node with 2 index should be the same value as third node")
        self.assertEqual(self.linkedList[2], self.last_node, "Node with 2 index should be the same node as lastNode node")

    def test_getitem_negative_first_node(self):
        self.assertEqual(self.linkedList[-1], self.third_node, "Node with negative -1 index should be the same value as third node")
        self.assertEqual(self.linkedList[-1], self.last_node, "Node with negative -1 index should be the same node as last node")

    def test_getitem_negative_second_node(self):
        self.assertEqual(self.linkedList[-2], self.second_node, "Node with negative -2 index should be the same as second node")
    
    def test_getitem_negative_third_node(self):
        self.assertEqual(self.linkedList[-3], self.head_node, "Node with negative -3 index should be the same as headNode")

    def test_getitem_out_of_range_positive_node(self):
        with self.assertRaises(IndexError):
            self.linkedList[3]

    def test_getitem_out_of_range_negative_node(self):
        with self.assertRaises(IndexError):
            self.linkedList[-4]

    def test_setitem(self):
        self.linkedList[0] = "new value"
        self.assertEqual(self.linkedList.headNode.value, "new value", "Head nodes's value should be updated to the new value")

    def test_delitem_first_node(self):
        del self.linkedList[0]

        self.assertEqual(self.linkedList.length, len(self.values) - 1, "List length after delete should be 2")
        self.assertEqual(self.linkedList.headNode, self.second_node, "Head node should be the old second node")
        self.assertEqual(self.linkedList.headNode.nextNode, self.third_node, "Second node should be the old third node")
        self.assertEqual(self.linkedList.headNode.nextNode.nextNode, None, "There should be no third node")
        self.assertEqual(self.linkedList.lastNode, self.last_node, "Last node should be the same")        

    def test_delitem_second_node(self):
        del self.linkedList[1]

        self.assertEqual(self.linkedList.length, len(self.values) - 1, "List length after delete should be 2")
        self.assertEqual(self.linkedList.headNode, self.head_node, "Head node should be unchanged")
        self.assertEqual(self.linkedList.headNode.nextNode, self.third_node, "Second node should be the old third node")
        self.assertEqual(self.linkedList.headNode.nextNode.nextNode, None, "There should be no third node")
        self.assertEqual(self.linkedList.lastNode, self.last_node, "Last node should be the same")   

    def test_delitem_third_node(self):
        del self.linkedList[2]

        self.assertEqual(self.linkedList.length, len(self.values) - 1, "List length after delete should be 2")
        self.assertEqual(self.linkedList.headNode, self.head_node, "Head node should be unchanged")
        self.assertEqual(self.linkedList.headNode.nextNode, self.second_node, "Second node should be unchanged")
        self.assertEqual(self.linkedList.headNode.nextNode.nextNode, None, "There should be no third node")
        self.assertEqual(self.linkedList.lastNode, self.second_node, "Last node should be the second node")

    def test_delitem_negative_first_node(self):
        del self.linkedList[-1]

        self.assertEqual(self.linkedList.length, len(self.values) - 1, "List length after delete should be 2")
        self.assertEqual(self.linkedList.headNode, self.head_node, "Head node should be unchanged")
        self.assertEqual(self.linkedList.headNode.nextNode, self.second_node, "Second node should be unchanged")
        self.assertEqual(self.linkedList.headNode.nextNode.nextNode, None, "There should be no third node")
        self.assertEqual(self.linkedList.lastNode, self.second_node, "Last node should be the second node")

    def test_delitem_out_of_range_positive_index(self):
        with self.assertRaises(IndexError):
            del self.linkedList[4]

        self.assertEqual(self.linkedList.length, len(self.values), "List length should not change")
        self.assertEqual(self.linkedList.headNode, self.head_node, "Head node should not have changed")
        self.assertEqual(self.linkedList.headNode.nextNode, self.second_node, "Second node should not have changed")
        self.assertEqual(self.linkedList.headNode.nextNode.nextNode, self.third_node, "Third node should not have changed")
        self.assertEqual(self.linkedList.lastNode, self.third_node, "Last node should not have changed")

    def test_delitem_out_of_range_negative_index(self):
        with self.assertRaises(IndexError):
            del self.linkedList[-4]

        self.assertEqual(self.linkedList.length, len(self.values), "List length should not change")
        self.assertEqual(self.linkedList.headNode, self.head_node, "Head node should not have changed")
        self.assertEqual(self.linkedList.headNode.nextNode, self.second_node, "Second node should not have changed")
        self.assertEqual(self.linkedList.headNode.nextNode.nextNode, self.third_node, "Third node should not have changed")
        self.assertEqual(self.linkedList.lastNode, self.third_node, "Last node should not have changed")


class TestSearchIndexOfDelete(unittest.TestCase):
    def setUp(self):
        self.values = ("value 1", "value 2", "value 3")
        
        self.linkedList = linkedlist.SingleLinkedList()
        for value in self.values:
            self.linkedList.append(value)
        
        self.head_node = self.linkedList.headNode
        self.last_node = self.linkedList.lastNode
        self.second_node = self.linkedList.headNode.nextNode
        self.third_node = self.linkedList.headNode.nextNode.nextNode

    def test_search_exists_first(self):
        result = self.linkedList.search(self.values[0])
        self.assertEqual(result, self.head_node, "First node should be returned")

    def test_search_exists_second(self):
        result = self.linkedList.search(self.values[1])
        self.assertEqual(result, self.second_node, "Second node should be returned")

    def test_search_exists_third(self):
        result = self.linkedList.search(self.values[2])
        self.assertEqual(result, self.third_node, "Third node should be returned")
    
    def test_search_does_not_exist(self):
        result = self.linkedList.search("unknown value")
        self.assertEqual(result, None, "None should be returned for unknown value")

    def test_indexOf_exists_first(self):
        index = 0
        result = self.linkedList.indexOf(self.values[index])
        self.assertEqual(result, index, "Index 0 should be returned")

    def test_indexOf_exists_second(self):
        index = 1
        result = self.linkedList.indexOf(self.values[index])
        self.assertEqual(result, index, "Index 1 should be returned")

    def test_indexOf_exists_third(self):
        index = 2
        result = self.linkedList.indexOf(self.values[index])
        self.assertEqual(result, index, "Index 2 should be returned")
    
    def test_indexOf_does_not_exist(self):
        result = self.linkedList.indexOf("unknown value")
        self.assertEqual(result, None, "None should be returned for unknown value")

    def test_delete_exists_first(self):
        index = 0
        result = self.linkedList.delete(self.values[index])
        self.assertEqual(result, self.head_node, "Deleted previous head node should be returned")
        self.assertEqual(self.linkedList.length, len(self.values) - 1, "List length after delete should be 2")
        self.assertEqual(self.linkedList.headNode, self.second_node, "Head node should be the old second node")
        self.assertEqual(self.linkedList.headNode.nextNode, self.third_node, "Second node should be the old third node")
        self.assertEqual(self.linkedList.headNode.nextNode.nextNode, None, "There should be no third node")
        self.assertEqual(self.linkedList.lastNode, self.last_node, "Last node should be the same")        

    def test_delete_exists_second(self):
        index = 1
        result = self.linkedList.delete(self.values[index])
        self.assertEqual(result, self.second_node, "Deleted previous second node should be returned")
        self.assertEqual(self.linkedList.length, len(self.values) - 1, "List length after delete should be 2")
        self.assertEqual(self.linkedList.headNode, self.head_node, "Head node should be unchanged")
        self.assertEqual(self.linkedList.headNode.nextNode, self.third_node, "Second node should be the old third node")
        self.assertEqual(self.linkedList.headNode.nextNode.nextNode, None, "There should be no third node")
        self.assertEqual(self.linkedList.lastNode, self.last_node, "Last node should be the same")   

    def test_delete_exists_third(self):
        index = 2
        result = self.linkedList.delete(self.values[index])
        self.assertEqual(result, self.third_node, "Deleted previous third node should be returned")
        self.assertEqual(self.linkedList.length, len(self.values) - 1, "List length after delete should be 2")
        self.assertEqual(self.linkedList.headNode, self.head_node, "Head node should be unchanged")
        self.assertEqual(self.linkedList.headNode.nextNode, self.second_node, "Second node should be unchanged")
        self.assertEqual(self.linkedList.headNode.nextNode.nextNode, None, "There should be no third node")
        self.assertEqual(self.linkedList.lastNode, self.second_node, "Last node should be the second node")

    def test_delete_does_not_exist(self):
        result = self.linkedList.delete("unknown value")
        self.assertEqual(result, None, "None should be returned for unknown value")
        self.assertEqual(self.linkedList.length, len(self.values), "List length should not change")
        self.assertEqual(self.linkedList.headNode, self.head_node, "Head node should not have changed")
        self.assertEqual(self.linkedList.headNode.nextNode, self.second_node, "Second node should not have changed")
        self.assertEqual(self.linkedList.headNode.nextNode.nextNode, self.third_node, "Third node should not have changed")
        self.assertEqual(self.linkedList.lastNode, self.third_node, "Last node should not have changed")

if __name__ == '__main__':
    unittest.main()