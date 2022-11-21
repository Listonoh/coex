from collections import Counter
import random
from django.db import models

# Create your models here.

class RandomGenerator(models.Model):
    class GeneratorChoices(models.TextChoices):
        NORMAL = 'normal'
        ADVANCED = 'advanced'

    timestamp = models.DateTimeField(auto_now_add=True)
    from_number = models.IntegerField()
    to_number = models.IntegerField()
    result_list = models.JSONField()
    count = models.IntegerField()
    generator_type = models.CharField(max_length=50, choices=GeneratorChoices.choices, default=GeneratorChoices.NORMAL)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)

    def generate(self, n: int):
        return [random.randint(self.from_number, self.to_number) for _ in range(n)]

    def __str__(self):
        return f'{self.from_number} - {self.to_number} ({self.count})'

    @property
    def distribution(self):
        dist = Counter(self.result_list)
        return {i: round(dist[i]/self.count * 100, 2) for i in range(self.from_number, self.to_number+1)}


class AdvanceRandomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(generator_type=RandomGenerator.GeneratorChoices.ADVANCED)

class AdvanceRandomGenerator(RandomGenerator):
    advance_objects = AdvanceRandomManager()
    class Meta:
        proxy = True
    def __str__(self):
        return super().__str__() + ' (advanced)'
    
    def __repr__(self) -> str:
        return 'super().__repr__()'

    def generate(self, n):
        """
        Generate random numbers with weights
        """
        my_nums = list(range(self.from_number, self.to_number+1))

        sum_of_values = sum(my_nums)
        for i in range(n):
            r = random.randint(1, sum_of_values)
            for weight in my_nums:
                r -= weight
                if r <= 0:
                    yield weight
                    break
    