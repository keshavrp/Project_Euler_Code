'''By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.'''
def sum_of_even_terms(num):
    num_1=1
    num_2=2
    sum=0
    while num_1 <= num :
        if num_1 % 2 == 0:
            sum=sum + num_1
        num_2=num_1 + num_2
        num_1=num_2 - num_1
    return sum

print(f'The sum of the even-valued terms: {sum_of_even_terms(4000000)}.')