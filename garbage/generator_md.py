def get_new_md_content(old_content, new_content):
    pass

def read_data(filename):
    pass

def write_data(filename, data):
    pass

def get_new_md_solution(data):
    result = {}
    result['md_link'] = '+ [Two Sum](#two-sum)'
    result['md_solution'] = """## Two Sum
    
http://leetcode.com/problems/two-sum/

```python
class Solution(object):
    def twoSum(self, nums, target):
        previous_num = {}
        for index, num in enumerate(nums):
            diff = target - num
            if(diff in previous_nums):
                return index, previous_nums[diff]
            previous_nums[num] = index
            
```"""
    return result

def get_old_md_solutions(data):
    pass


# with open("leetcode.txt", "r") as file:
#     header = file.readline()
#     link = file.readline()
#     code = file.read()
#
#
# with open("result.txt", "w") as file:
#     print("##", header, sep="", end="\n", file = file)
#     print("```python", code, "```", sep="\n", file = file)