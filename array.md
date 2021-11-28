# Array

+ [977. Squares of a Sorted Array](#squares-of-a-sorted-array)

## 977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
<details><summary>Test cases</summary><blockquote>

```python

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