class Solution:
    def hammingWeight(self, n: int) -> int:
      #sol.#1
      # return str(bin(n)).count('1')
      
      #sol.#2
      b = str(bin(n))
      return len([i for i in b if i == '1'])
