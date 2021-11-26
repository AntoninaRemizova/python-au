import unittest
from garbage import generator_md as gnr

class TestGenerator(unittest.TestCase):
    def test_get_new_md_solution(self):
        file_content = 'Two Sum\n' \
                       'http://leetcode.com/problems/two-sum/\n'  \
                       'class Solution(object):\n' \
                       '    def twoSum(self, nums, target):\n' \
                       '        previous_num = {}\n' \
                       '        for index, num in enumerate(nums):\n' \
                       '            diff = target - num\n' \
                       '            if(diff in previous_nums):\n' \
                       '                return index, previous_nums[diff]\n' \
                       '            previous_nums[num] = index'
        expected = {'md_link': '+ [Two Sum](#two-sum)',
                    'md_solution': '## Two Sum\n'
                    '    \n'
                    'http://leetcode.com/problems/two-sum/\n'
                    '\n'
                    '```python\n'
                    'class Solution(object):\n'
                    '    def twoSum(self, nums, target):\n'
                    '        previous_num = {}\n'
                    '        for index, num in enumerate(nums):\n'
                    '            diff = target - num\n'
                    '            if(diff in previous_nums):\n'
                    '                return index, previous_nums[diff]\n'
                    '            previous_nums[num] = index\n'
                    '            \n'
                    '```'}
        self.assertEqual(expected, gnr.get_new_md_solution(file_content))  # add assertion here


if __name__ == '__main__':
    unittest.main()
