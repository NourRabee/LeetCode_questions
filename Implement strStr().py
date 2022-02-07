class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        output = 0

        if needle in haystack and needle and haystack:
            output = haystack.find(needle)
        elif not needle:
            output = 0

        elif needle not in haystack:
            output = -1
            
        return output
