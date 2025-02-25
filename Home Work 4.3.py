import random
random_lst = [random.randint(1, 100) for _ in range(random.randint(3, 10))]
new_lst = [random_lst[0], random_lst[2], random_lst[-2]]
print(random_lst)
print(new_lst)