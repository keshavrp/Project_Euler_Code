#Python program to the value of the first triangle number to have over five hundred divisors?
sum=0
my_list=list()
my_list_1=list()
for i in range(1,10**5):
    sum+=i
    my_list.append(sum)
for j in range(1,10**5):
    for k in my_list:
        while k%j==0:
            my_list_1.append(j)
            if len(my_list_1)==500:
                print(j)
            else:
                my_list_1.clear()