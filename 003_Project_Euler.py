#Python program to find the largest prime factor of the number 600851475143?
def largest_prime(num):
    for i in range(2,num//2 + 1):
        while num%i==0:
            num=num/i
            if num==1 or num==i:
                return i

print(f'The largest prime factor of the number 600851475143 is: {largest_prime(600851475143)}.')