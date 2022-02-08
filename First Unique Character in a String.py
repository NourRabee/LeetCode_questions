class Solution:
    def firstUniqChar(self, s: str) -> int:
            firstUniqChar = 0
            for i in s:
                if s.count(i) == 1:
                    firstUniqChar = s.index(i)
                    break
                else:
                    firstUniqChar = -1
            return firstUniqChar
