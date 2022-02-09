class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        temp = ""
        for i in ransomNote:

            if magazine.count(i) >= ransomNote.count(i):
                temp += i
        if temp == ransomNote:
            return True
        else:
            return False
