class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
            return not self == other
    
class SingleList:

    def __init__(self):
        self.length = 0  
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def count(self):   
        return self.length

    def insert_head(self, node):
        if self.head:   
            node.next = self.head
            self.head = node
        else:   
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   
        if self.head:   
            self.tail.next = node
            self.tail = node
        else:   
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  
        self.length -= 1
        return node   
    
    def remove_tail(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        
        temp = self.head
        node = self.tail
        if self.head == self.tail:   
            self.head = self.tail = None
        else: 
            while not temp.next is self.tail:
                temp = temp.next
        del self.tail
        temp.next=None
        self.tail = temp
        self.length -= 1
        return node
    
    def join(self, other):
        if other.is_empty():
            return
        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
        else:
            self.tail.next = other.head
            self.tail = other.tail
        self.length += other.length
        other.clear()

    def clear(self):   #prymitywnie, bardzo dużo "śmieci" powstaje ale operacja ta ma złożoność O(1)"
        self.head = None
        self.tail = None
        self.length = 0
    
    def trueClear(self):   #nie zostawia śmieci ale ma złożoność O(n) a prosił pan o join o złozoności O(1), a użycie w join funkcji trueClear zwiększyło by ja do O(n)
        current = self.head
        while current:
            next_node = current.next
            del current
            current = next_node
        self.head = self.tail = None
        self.length = 0

    def display(self):  
        if self.is_empty():
            print("empty list")
            return
        node = self.head
        while node:
            print(str(node), end=" -> ")
            node = node.next
        print("None")
    
'''
A = SingleList()

B = SingleList()

print(str(Node(1)))

A.insert_head(Node(12))
A.insert_head(Node(10))
A.insert_head(Node(9))
A.display()

B.insert_head(Node(15))
B.insert_head(Node(14))
B.insert_head(Node(13))
B.display()

A.join(B)

A.display()
B.display()

B.insert_head(Node(18))
B.display()
B.insert_tail(Node(19))
B.display() '''

import unittest

class TestSingleList(unittest.TestCase):

    def setUp(self):
        self.list1 = SingleList()
        self.list2 = SingleList()

    def test_remove_tail(self):
        with self.assertRaises(ValueError):
            self.list1.remove_tail()
        
        self.list1.insert_tail(Node(1))
        tail = self.list1.remove_tail()
        self.assertEqual(tail.data, 1)
        self.assertTrue(self.list1.is_empty())
        
        self.list1.insert_tail(Node(1))
        self.list1.insert_tail(Node(2))
        self.list1.insert_tail(Node(3))
        tail = self.list1.remove_tail()
        self.assertEqual(tail.data, 3)
        self.assertEqual(self.list1.tail.data, 2)
        self.assertEqual(self.list1.count(), 2)

    def test_join(self):
        self.list1.join(self.list2)
        self.assertTrue(self.list1.is_empty())
        self.assertTrue(self.list2.is_empty())

        self.list1.insert_tail(Node(1))
        self.list1.insert_tail(Node(2))
        self.list2.join(self.list1)
        self.assertEqual(self.list2.count(), 2)
        self.assertEqual(self.list2.head.data, 1)
        self.assertEqual(self.list2.tail.data, 2)
        self.assertTrue(self.list1.is_empty())

        self.list1.insert_tail(Node(3))
        self.list1.insert_tail(Node(4))
        self.list2.join(self.list1)
        self.assertEqual(self.list2.count(), 4)
        self.assertEqual(self.list2.tail.data, 4)
        self.assertTrue(self.list1.is_empty())

    def test_clear(self):
        self.list1.clear()
        self.assertTrue(self.list1.is_empty())

        self.list1.insert_tail(Node(1))
        self.list1.insert_tail(Node(2))
        self.list1.insert_tail(Node(3))
        self.list1.clear()
        self.assertTrue(self.list1.is_empty())
        self.assertEqual(self.list1.count(), 0)

    def test_trueClear(self):
        self.list1.trueClear()
        self.assertTrue(self.list1.is_empty())

        self.list1.insert_tail(Node(1))
        self.list1.insert_tail(Node(2))
        self.list1.insert_tail(Node(3))
        self.list1.trueClear()
        self.assertTrue(self.list1.is_empty())
        self.assertEqual(self.list1.count(), 0)

if __name__ == "__main__":
    unittest.main()