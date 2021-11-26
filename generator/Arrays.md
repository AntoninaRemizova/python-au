# Arrays

+ [Two Sum](#wo-sum)
+ [String Compression](#string-compression)

## Two Sum

```python
class Solution(object):
    def twoSum(self, nums, target):
        previous_num = {}
        for index, num in enumerate(nums):
            diff = target - num
            if(diff in previous_nums):
                return index, previous_nums[diff]
            previous_nums[num] = index
```

## String Compression

```python
def compress(chars):
    length = len(chars)
    if length == 1:
        return 1
    sample = chars[0]
    chars.append(" ")
    count = 0
    for i in range(length + 1):
        char = chars[0]
        chars.pop(0)
        if char == sample:
            count += 1
        else:
            if count == 1:
                chars.append(sample)
            else:
                chars.append(sample)
                chars += list(str(count))
            sample = char
            count = 1
    return len(chars)
```
