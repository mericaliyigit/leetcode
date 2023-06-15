from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        l = 0
        credit = 1
        for r, num in enumerate(nums):
            if num == 0:
                credit -= 1
            if credit < 0:
                if nums[l] == 0:
                    credit += 1
                l += 1
            else:
                longest = max(longest, r - l)
        return longest


print(Solution().longestSubarray(nums=[1, 1, 0, 1]))

print(Solution().longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))

print(Solution().longestSubarray(nums=[1, 1, 1]))
