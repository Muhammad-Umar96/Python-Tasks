import random


numbers = []

while len(numbers) < 100:
    rand = (random.randint(1,1000))
    if rand % 13 == 0 and rand % 29 ==0:
        numbers.append(rand)

for i in range (len(numbers)):
    print(numbers[i])
