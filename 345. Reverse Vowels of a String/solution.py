class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = set(['a', 'e', 'i', 'o', 'u',
                   'A', 'E', 'I', 'O', 'U'])
        extracted_vows = []
        for letter in s:
            if letter in vow:
                extracted_vows.append(letter)

        extracted_vows.reverse()
        ix = 0
        result = ''
        for letter in s:
            if letter not in vow:
                result += letter
            else:
                result += extracted_vows[ix]
                ix += 1

        return result
