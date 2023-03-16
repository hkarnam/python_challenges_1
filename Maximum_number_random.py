import random

def gen_n():
    gen_num = random.randint(1,1000)
    print(f"{gen_num}")
    return gen_num

initial_num = 210
print(f"initial number is {initial_num}")
change = 0
i = 1
change = 0
while i < 100:
    a = gen_n()
    i += 1
    if  a > initial_num:
        initial_num = a
        change += 1
        print(f"{initial_num} is new max")
print(f"Maximum was changed {change} times")