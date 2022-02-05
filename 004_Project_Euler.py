#Python program to find the largest palindrome made from the product of two n-digit numbers.
def lar_palindrome(n):
    my_list=list()
    for i in range((10**(n-1)),(10**n)):
        for j in range((10**(n-1)),(10**n)):
            mul=str(i*j)
            if mul[ : :-1]==mul[:]:
                my_list.append(int(mul))
                my_list.sort()
    return my_list[-1]

print(lar_palindrome(3))