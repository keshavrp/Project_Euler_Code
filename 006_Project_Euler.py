#Python program to Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def squares_sum(num):
    sum_of_squares=0
    for i in range(1,num+1):
        for j in range(1,num+1):
            if i==j :
                sum_of_squares+=i*j
    return sum_of_squares

def square_of_sum(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    square_of_sums=sum * sum
    return square_of_sums

print('The desired reslt is:',square_of_sum(100)-squares_sum(100))
