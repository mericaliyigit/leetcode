class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_s = {}
        s_to_pattern = {}
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        for idx, letter in enumerate(pattern):
            if letter in pattern_to_s and pattern_to_s[letter] != s[idx]:
                return False
            else:
                pattern_to_s[letter] = s[idx]

            if s[idx] in s_to_pattern and s_to_pattern[s[idx]] != letter:
                return False
            else:
                s_to_pattern[s[idx]] = letter
        return True
