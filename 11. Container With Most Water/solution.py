from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        r = len(height)-1
        l = 0
        while (l != r):
            h = min(height[l], height[r])
            distance = r - l
            area = h * distance
            if area > max_area:
                max_area = area
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

solution = Solution()
res = solution.maxArea(height)
print(res)
