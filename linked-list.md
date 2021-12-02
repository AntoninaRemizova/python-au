# Linked List

+ [876. Middle of the Linked List](#middle-of-the-linked-list)

## 876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
<details><summary>Test cases</summary><blockquote>

```python
import unittest
import middle_of_the_linked_list as rll


class TestMiddleOfTheLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = rll.Solution()

    def test_one_middleNode(self):
        expected = self.get_linked_list_values(self.build_linked_list([3, 4, 5]))
        actual = self.get_linked_list_values(self.solution.middleNode(self.create_linked_list(5)))
        self.assertEqual(expected, actual)

    def test_two_middleNode(self):
        expected = self.get_linked_list_values(self.build_linked_list([4, 5, 6]))
        actual = self.get_linked_list_values(self.solution.middleNode(self.create_linked_list(6)))
        self.assertEqual(expected, actual)

    def test_empty_middleNode(self):
        expected = []
        actual = self.solution.middleNode(None)
        self.assertEqual(expected, actual)

    def create_linked_list(self, n=10):
        prev_link = None
        for i in range(n, 0, -1):
            elem = rll.ListNode(i, prev_link)
            prev_link = elem
        return elem

    def build_linked_list(self, source):
        prev_link = None
        for i in source[::-1]:
            elem = rll.ListNode(i, prev_link)
            prev_link = elem
        return elem

    def get_linked_list_values(self, head):
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result


if __name__ == '__main__':
    unittest.main()

```
</blockquote></details>

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        elem, i = head, 1
        if elem == None:
            return []
        while elem.next:
            i += 1
            elem = elem.next
        elem = head
        for j in range(i // 2):
            elem = elem.next
        return elem
```