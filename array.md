# Array

+ [977. Squares of a Sorted Array](#squares-of-a-sorted-array)

## 977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
<details><summary>Test cases</summary><blockquote>

```python
import unittest
import squares_of_a_sorted_array as rll

class TestSquaresOfASortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = rll.Solution()

    def test_get_first_nonnegtive(self):
        self.assertEqual(2, self.solution.get_first_nonnegtive([-3, -1, 0, 3, 4, 10]))
        self.assertEqual(3, self.solution.get_first_nonnegtive([-4, -3, -1]))
        self.assertEqual(0, self.solution.get_first_nonnegtive([]))

    def test_squares(self):
        expected = [0, 1, 9, 9, 16, 100]
        actual = self.solution.sortedSquares([-3, -1, 0, 3, 4, 10])
        self.assertEqual(expected, actual)

    def test_squares_only_negative(self):
        expected = [1, 9, 16]
        actual = self.solution.sortedSquares([-4, -3, -1])
        self.assertEqual(expected, actual)

    def test_squares_empty(self):
        expected = []
        actual = self.solution.sortedSquares([])
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

```
</blockquote></details>

```python
class Solution:
    def get_first_nonnegtive(self, nums):
        for indx, elem in enumerate(nums):
            if elem >= 0:
                return indx
        return len(nums)

    def merge_lists(self, nums, left, right):
        result = []
        while left >= 0 and right < len(nums):
            if nums[left] ** 2 < nums[right] ** 2:
                result.append(nums[left] ** 2)
                left -= 1
            else:
                result.append(nums[right] ** 2)
                right += 1

        while left >= 0:
            result.append(nums[left] ** 2)
            left -= 1

        while right < len(nums):
            result.append(nums[right] ** 2)
            right += 1

        return result

    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = self.get_first_nonnegtive(nums)
        return self.merge_lists(nums, start - 1, start)

```