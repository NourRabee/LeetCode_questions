class Solution:
    def countBits(self, n: int) -> List[int]:
        hashmap= {}
        nofOnes = []
        for i in range(n+1):
            binary = bin(i)
            binary = binary[2:]
            hashmap[binary] = binary.count('1')
        for i in hashmap:
            nofOnes.append(hashmap[i])
        return nofOnes

