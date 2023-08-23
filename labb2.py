#Första uppgiften online
'''
#bild 1
def main():
    number = [1,2,3]
    number_reference=number
    
main()

#bild 2
def main():
    number = [1,2,3]
    number_reference=number.copy()

#bild 3     
def add_element(l, e):
    l.append(e)
    return l
def main():
    numbers = [1,2,3]
    add_element(numbers, 4)
    return numbers

main()

#bild 4
def add_element(l, e):
    l=l.copy()
    l.append(e)
    return l
def main():
    numbers = [1,2,3]
    add_element(numbers, 4)
    return numbers

main()

'''

#Uppgift 2a triangle
def triangle(heigth):
    for i in range (heigth):
        for n in range(i):
            print("**", end ="")

        print("*")

triangle(3)

#Uppgift 2a Flagga
#Flagga ska vara 21*9
'''
********** **********
********** **********
********** **********
********** **********

********** **********
********** **********
********** **********
********** **********

 
********** ********** 
********** ********** 
********** ********** 
********** **********

********** ********** 
********** ********** 
********** ********** 
********** ********** 


********************* ******************** 
********************* ******************** 
********************* ******************** 
********************* ******************** 
********************* ******************** 
********************* ******************** 
********************* ******************** 
********************* ********************

********************* ******************** 
********************* ******************** 
********************* ******************** 
********************* ******************** 
********************* ******************** 
********************* ******************** 
********************* ******************** 

'''
def flag(scale):
    for heigth in range (scale * 8+1):
        for width in range(scale * 20+1):
            if width == (scale * 20+1) // 2 :
                print(" ", end="")
            else:
                print("*", end="")
               # print(width)
        if heigth == (scale * 8) // 2 - 1:
            print("\n")
        else:
            print(" ")
           # print(heigth)
    

flag(1)

