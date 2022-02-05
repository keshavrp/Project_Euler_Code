#Python program to find the sum of all the multiples of 3 or 5 below 1000.
def multiples(num): 
    sum=0
    for i in range(1,num):
        if i%3==0 or i%5==0 :
            sum=sum+i
    return sum

print(f'The sum of the multiples of 3 or 5 below 1000: {multiples(1000)}.')