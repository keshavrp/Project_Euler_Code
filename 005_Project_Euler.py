#Python program to find the smallest positive number that is evenly divisible by all of numbers from 1 to 20.
import math
def divisible_by_all(num):
    my_list=list(range(1,num+1))
    lcm=my_list[0]
    for i in range(1,num):
        lcm=lcm*my_list[i]//math.gcd(lcm, my_list[i])
    return lcm

print(f'The smallest positive number that is evenly divisible by all of numbers from 1 to 20 is:', divisible_by_all(20))