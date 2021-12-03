# Linked List

+ [160. Intersection of Two Linked Lists](#intersection-of-two-linked-lists)

## 160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
<details><summary>Test cases</summary><blockquote>

```python
import unittest
import intersection_of_two_linked_lists as rll


class TestIntersectionOfTwoLinkedLists(unittest.TestCase):
    def setUp(self):
        self.solution = rll.Solution()


    def test_intersection(self):
        common = self.build_linked_list([8, 4, 5])
        list1, list1.next = self.build_linked_list([4, 1]), common
        list2, list2.next = self.build_linked_list([5, 6, 1]), common
        actual = self.solution.getIntersectionNode(list1, list2)
        expected = common
        self.assertEqual(expected, actual)

    def test_no_intersection(self):
        common = []
        list1, list1.next = self.build_linked_list([2, 6, 4]), common
        list2, list2.next = self.build_linked_list([1, 5]), common
        actual = self.solution.getIntersectionNode(list1, list2)
        expected = common
        self.assertEqual(expected, actual)

    def test_empty_lists(self):
        common = []
        list1 = []
        list2 = []
        actual = self.solution.getIntersectionNode(list1, list2)
        expected = common
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
    def getIntersectionNode(self, headA, headB):
        nodeA, nodeB = headA, headB
        while nodeA != nodeB:
            if nodeA:
                nodeA = nodeA.next
            else:
                nodeA = headB
            if nodeB:
                nodeB = nodeB.next
            else:
                nodeB = headA
        return nodeA

```