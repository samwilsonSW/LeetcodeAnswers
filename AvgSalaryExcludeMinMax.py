class Solution:
    def average(self, salary: List[int]) -> float:
        sum = 0
        for i in salary:
            sum += i
            
        salary.sort()
        min = salary[0]
        max = salary[len(salary)-1]
        
        sum = sum - max - min
        print(sum)
        avg = sum / (len(salary) - 2)
        
        return avg
