import random
import bisect
from collections import Counter

class RandomGenerator:
    def __init__(self, from_number: int, to_number: int):
        if from_number > to_number:
            raise ValueError('from_number must be less than to_number')
        if from_number < 0 or to_number < 0:
            raise ValueError('from_number and to_number must be positive')
        
        self.from_number = from_number
        self.to_number = to_number

    def generate(self, n: int):
        return [random.randint(self.from_number, self.to_number+1) for _ in range(n)]
    
    @staticmethod
    def get_report(random_numbers: list):
        return Counter(random_numbers)
    
class AdvancedRandomGenerator(RandomGenerator):
    # 
    def generate(self, n):
        my_nums = {i: i for i in range(self.from_number, self.to_number+1)}
        print(my_nums)
        sum = 0
        for w in my_nums.values():
            sum += w
        print(sum)
        for i in range(n):
            r = random.randint(1, sum)
            for j, weight in my_nums.items():
                r -= weight
                if r <= 0:
                    yield j
                    break




result = list(AdvancedRandomGenerator(0, 2).generate(100))
print(result)
print(Counter(sorted(result)))