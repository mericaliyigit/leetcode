class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(0, len(s)+1):
            for j in range(i, len(s)+1):
                word = s[i:j]
                lenw = len(word)
                setw = len(set(word))
                if lenw == setw:
                    longest = max(longest, lenw)
                else:
                    break

        return longest
