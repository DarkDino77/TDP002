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

#Uppgift 2a 
def triangle(heigth):
    for i in range (heigth):
        for n in range(i):
            print("**", end ="")

        print("*")

triangle(3)
