import random

numbers = range(1,46)
print(list(numbers))
lotto = random.sample(numbers,6)
print(sorted(lotto))