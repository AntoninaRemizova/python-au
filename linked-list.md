# Linked List

+ [148. Sort List](#sort-list)

## 148. Sort List
https://leetcode.com/problems/sort-list/
<details><summary>Test cases</summary><blockquote>

```python
import unittest
import sort_list as rll


class TestSortList(unittest.TestCase):
    def setUp(self):
        self.solution = rll.Solution()

    def test_merge(self):
        expected = self.get_linked_list_values(self.build_linked_list([1, 2, 3, 4]))
        list1 = self.build_linked_list([2, 4])
        list2 = self.build_linked_list([1, 3])
        actual = self.get_linked_list_values(self.solution.merge(list1, list2))
        self.assertEqual(expected, actual)

    def test_sort(self):
        expected = self.get_linked_list_values(self.build_linked_list([1, 2, 3, 4]))
        actual = self.get_linked_list_values(self.solution.sortList(self.build_linked_list([4, 2, 1, 3])))
        self.assertEqual(expected, actual)

    def test_sort_empty(self):
        expected = []
        actual = self.get_linked_list_values(self.solution.sortList(None))
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

    def sortList(self, head):
        if not head or not head.next:
            return head
        prev = slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        first_head = Solution.sortList(self, head)
        second_head = Solution.sortList(self, slow)
        return Solution.merge(self, first_head, second_head)

    def merge(self, list1, list2):
        new_list = ListNode()
        elems = new_list
        while list1 and list2:
            if list1.val < list2.val:
                elems.next = list1
                list1 = list1.next
            else:
                elems.next = list2
                list2 = list2.next
            elems = elems.next
        if list1:
            elems.next = list1
        if list2:
            elems.next = list2
        return new_list.next

        return sortList(head)




```