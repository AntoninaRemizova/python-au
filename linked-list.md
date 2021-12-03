# Linked List

+ [234. Palindrome Linked List](#palindrome-linked-list)

## 234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
<details><summary>Test cases</summary><blockquote>

```python
import unittest
import palindrome_linked_list as rll


class TestPalindromeLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = rll.Solution()

    def test_true_even_palindrome(self):
        expected = True
        actual = self.solution.isPalindrome(self.build_linked_list([1, 2, 2, 1]))
        self.assertEqual(expected, actual)

    def test_true_odd_palindrome(self):
        expected = True
        actual = self.solution.isPalindrome(self.build_linked_list([1, 2, 3, 2, 1]))
        self.assertEqual(expected, actual)

    def test_false_palindrome(self):
        expected = False
        actual = self.solution.isPalindrome(self.build_linked_list([1, 2]))
        self.assertEqual(expected, actual)

    def test_palindrome_empty(self):
        expected = None
        actual = self.solution.isPalindrome(None)
        self.assertEqual(expected, actual)

    def build_linked_list(self, source):
        prev_link = None
        for i in source[::-1]:
            elem = rll.ListNode(i, prev_link)
            prev_link = elem
        return elem


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
    def isPalindrome(self, head):
        if not head:
            return None
        elems_val = []
        while head:
            elems_val.append(head.val)
            head = head.next
        if elems_val == elems_val[::-1]:
            return True
        else:
            return False
```