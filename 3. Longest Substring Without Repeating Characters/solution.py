class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        longest = 0
        # keep left stable move right
        for r in range(len(s)):
            # we havent encountered this char yet
            current_char = s[r]
            if current_char not in seen:
                longest = max(longest, r-l+1)
            else:
                # we have seen this char before but its behind our current window so not important
                if seen[current_char] < l:
                    longest = max(longest, r-l+1)
                # char is seen and inside our sliding window
                else:
                    l = seen[current_char] + 1
            # update the seen dictionary to show the most recent encounter of the current char
            seen[current_char] = r

        return longest


s = ''
s = ' '
s = 'xyzedf'
s = "abcabcbb"

print(Solution().lengthOfLongestSubstring(s))
