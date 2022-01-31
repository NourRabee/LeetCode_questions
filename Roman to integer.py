class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
                   'XC': 90, 'CD': 400, 'CM': 900}
        sum = 0
        i = 0
        while i <= len(s)-1:

            j = i + 1
            ch = s[i]

            if s[i] == 'I' and j < len(s) and (s[j] == 'V' or s[j] == 'X'):

                ch = s[i]+s[j]
                sum += hashMap[ch]
                i += 2
            elif s[i] == 'X' and j < len(s) and (s[j] == 'L' or s[j] == 'C'):

                ch = s[i] + s[j]
                sum += hashMap[ch]
                i += 2

            elif s[i] == 'C' and j < len(s) and (s[j] == 'D' or s[j] == 'M'):

                ch = s[i] + s[j]
                sum += hashMap[ch]
                i += 2

            else:
                sum += hashMap[ch]
                i += 1

        return sum
