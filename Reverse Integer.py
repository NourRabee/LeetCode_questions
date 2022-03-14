class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)

        if 0 > x > pow(-2, 31):

            i = y[:0:-1]
            n = i.lstrip('0')
            l = list(n)
            l.insert(0, '-')
            j = ''.join(l)
            if pow(-2, 31) < int(j) < pow(2, 31):
                return j
            else:
                return 0

        elif 0 < x < pow(2, 31) - 1:
            i = y[::-1]
            n = i.lstrip('0')
            if pow(-2, 31) < int(n) < pow(2, 31):
                return n
            else:
                return 0

        else:
            return 0
