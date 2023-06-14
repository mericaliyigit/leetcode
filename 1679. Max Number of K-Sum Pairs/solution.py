from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = [n for n in nums if n < k]
        nums.sort()
        # print(nums)
        count = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
                l += 1
                r -= 1
            if nums[l] + nums[r] > k:
                r -= 1
            if nums[l] + nums[r] < k:
                l += 1
        return count


print(Solution().maxOperations(nums=[3, 1, 3, 4, 3], k=6))
print(Solution().maxOperations(nums=[1, 2, 3, 4], k=5))
