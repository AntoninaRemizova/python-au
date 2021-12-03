# Linked List

+ [21. Merge Two Sorted Lists](#merge-two-sorted-lists)

## 21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
<details><summary>Test cases</summary><blockquote>

```python
import unittest
import merge_two_sorted_lists as rll


class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        self.solution = rll.Solution()

    def test_merge_two_lists_same_size(self):
        expected = self.get_linked_list_values(self.build_linked_list([1, 1, 2, 3, 4, 4]))
        list1 = self.build_linked_list([1, 2, 4])
        list2 = self.build_linked_list([1, 3, 4])
        actual = self.get_linked_list_values(self.solution.mergeTwoLists(list1, list2))
        self.assertEqual(expected, actual)

    def test_merge_two_lists_different_sizes(self):
        expected = self.get_linked_list_values(self.build_linked_list([1, 1, 2, 3, 4, 4, 5, 6, 7]))
        list1 = self.build_linked_list([1, 2, 4, 5, 6, 7])
        list2 = self.build_linked_list([1, 3, 4])
        actual = self.get_linked_list_values(self.solution.mergeTwoLists(list1, list2))
        self.assertEqual(expected, actual)

    def test_merge_two_lists_one_empty(self):
        expected = self.get_linked_list_values(self.build_linked_list([1, 2, 4]))
        list1 = self.build_linked_list([1, 2, 4])
        list2 = []
        actual = self.get_linked_list_values(self.solution.mergeTwoLists(list1, list2))
        self.assertEqual(expected, actual)

    def test_merge_two_lists_both_empty(self):
        expected = []
        list1 = []
        list2 = []
        actual = self.get_linked_list_values(self.solution.mergeTwoLists(list1, list2))
        self.assertEqual(expected, actual)

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
    def mergeTwoLists(self, list1, list2):
        new_list = ListNode()
        elems = new_list
        while list1 and list2:
            if list1.val < list2.val:
                elems.next = list1
                list1 = list1.next
            else:
                elems.next = list2
                list2 = list2.next
            print(elems)
            elems = elems.next
        if list1:
            elems.next = list1
        if list2:
            elems.next = list2
        return new_list.next

```