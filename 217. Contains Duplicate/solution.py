from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False


nums = [1, 2, 3, 1]
nums = [1, 2, 3, 4]
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print(Solution().containsDuplicate(nums))
