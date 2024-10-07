import random

#Generate random floats
print(random.random())

#Generate Random Integers
print(random.randint(1,100))
print(random.randint(1, 100))

#Generate Random Numbers
print(random.randrange(1, 10)) 
print(random.randrange(1, 10, 2))
print(random.randrange(0, 101, 10))

#Select Random Elements
print(random.choice('computer'))  
print(random.choice([12,23,45,67,65,43]))
print(random.choice((12,23,45,67,65,43)))

#Select Random Items from Data
aList = [20, 40, 80, 100, 120]
sampled_list = random.sample(aList, 3)
print(sampled_list)

#Generate the sampled list of random integers
num_list = random.sample(range(100), 5)
print(num_list)