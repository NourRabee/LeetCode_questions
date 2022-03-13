class Solution:
    def average(self, salary: List[int]) -> float:
        x= max(salary)
        y=min(salary)
        salary.remove(x)
        salary.remove(y)
        counter = 0
        sum = 0
        for i in salary:
            sum +=i
            counter+=1
        return sum/counter
