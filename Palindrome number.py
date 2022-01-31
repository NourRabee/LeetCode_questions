class Solution:
    def isPalindrome(self, x: int) -> bool:

                    x_s = str(x)
                    x_inv = x_s[::-1] 
          #So, when you do a[::-1], it starts from the end towards the first taking each element. So it reverses a. This is applicable for lists/tuples as well.
                    return x_s == x_inv
