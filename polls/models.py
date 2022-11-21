from collections import Counter
import random
from django.db import models

# Create your models here.
class RandomGenerator(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    from_number = models.IntegerField()
    to_number = models.IntegerField()
    result_list = models.JSONField()
    count = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.PROTECT)

    def generate(self, n: int):
        return [random.randint(self.from_number, self.to_number) for _ in range(n)]

    def __str__(self):
        return f'{self.from_number} - {self.to_number} ({self.count})'

    @property
    def distribution(self):
        dist = Counter(self.result_list)
        return {i: round(dist[i]/self.count * 100, 2) for i in range(self.from_number, self.to_number+1)}

class AdvanceRandomGenerator(RandomGenerator):
    def __str__(self):
        return  '(Advanced)'
    
    def __repr__(self) -> str:
        return 'super().__repr__()'

    def generate(self, n):
        my_nums = {i: i for i in range(self.from_number, self.to_number+1)}
        sum = 0
        for w in my_nums.values():
            sum += w
        for i in range(n):
            r = random.randint(1, sum)
            for j, weight in my_nums.items():
                r -= weight
                if r <= 0:
                    yield j
                    break