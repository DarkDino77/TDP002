#Uppgift 1a
sum = 0
for i in range(1, 513):
    sum += i
print(sum)

#Uppgift 1b
product = 1
for i in range(1, 513):
    product *= i
print(product)

#Uppgift 1c
number_found = False
iterator = 1
while number_found != True:
    all_nums_equal = True
    iter_iterator = 1
    while all_nums_equal:
        if iterator % iter_iterator != 0:
            all_nums_equal = False
            break
        if iter_iterator >= 13:
            break
        iter_iterator += 1
    if all_nums_equal == True:
        print("Found integer:", iterator)
        number_found = True
        break
    iterator += 1
    

#Uppgift 1d
sumprim = 0
for i in range(2,1001):
    prim = True
    for n in range(2,i):
        if(i % n) == 0 :
            prim = False
    if prim == True:
        sumprim += i
print(sumprim)


