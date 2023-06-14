from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = max_cons = 0
        for r, num in enumerate(nums):
            print(l, r)
            # if k is equal to 1 we dont use credit
            if num == 0:
                k -= 1
            if k < 0:
                # element at the start of our window is 0 we gain a k
                if nums[l] == 0:
                    k += 1
                # our tail needs to follow
                l += 1
            else:
                max_cons = max(max_cons, r - l + 1)
        return max_cons


print(Solution().longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
