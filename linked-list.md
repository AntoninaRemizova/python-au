# Linked List

+ [206. Reverse Linked List](#reverse-linked-list)

## 206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
<details><summary>Test cases</summary><blockquote>

```python
import unittest
import reverse_linked_list as rll


class TestReversedLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = rll.Solution()

    def test_reverse(self):
        expected = self.get_linked_list_values(self.build_linked_list([5, 4, 3, 2, 1]))
        actual = self.get_linked_list_values(self.solution.reverseList(self.create_linked_list(5)))
        self.assertEqual(expected, actual)  # add assertion here

    def test_reverse_empty(self):
        expected = None
        actual = self.solution.reverseList(None)
        self.assertEqual(expected, actual)  # add assertion here

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
    def reverseList(self, head):
        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
```
