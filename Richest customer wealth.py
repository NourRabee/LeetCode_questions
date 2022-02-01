class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
            theWealthiest = []
            sum = 0
            for i in range(len(accounts)):
                if len(accounts[i]) != 0:
                    for x in range(len(accounts[i])):
                        sum += accounts[i][x]
                    theWealthiest.append(sum)
                    sum = 0
            return max(theWealthiest)
