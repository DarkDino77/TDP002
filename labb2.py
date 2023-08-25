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


******************** ******************** 
******************** ******************** 
******************** ******************** 
******************** ******************** 
******************** ******************** 
******************** ******************** 
******************** ******************** 
******************** ********************

******************** ******************** 
******************** ******************** 
******************** ******************** 
******************** ******************** 
******************** ******************** 
******************** ******************** 
******************** ******************** 
******************** ******************** 


'''
def flag(scale):
    for heigth in range (scale * 8):
        for width in range((scale * 20)+1):
            if width == ((scale * 20)+1) // 2 :
                #a
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

#2b Inköpslistan
#Skapa listan
def create_shopping_list():
    return ["Kurslitteratur", "Anteckningsblock","Penna"]

#Visa vad som är i listan
def shopping_list(lista):
    for i in range(len(lista)):
        print(f"{i+1}.", lista[i])
#Lägger till i listan
def shopping_add(lista):
     lista.append(input("Vad ska läggas till i listan? "))
#Tar bort utan retur från listan
def shopping_remove(lista):
     del lista[int(input("Vilken sak vill du ta bort ur listan? "))-1]
#Låter användaren byta ut ett element i lista mot ett annat
def shopping_edit(lista):
    position = int(input("Vilken sak vill du ändra på? "))-1
    removed = lista.pop(position)
    lista.insert(position, input(f'Vad ska det stå istället för "{removed}"? '))

#2c
#Skapa lista 
lista = create_shopping_list()
#Välkomst medelande 
print("Välkommen till shoppinglistan, välj ett alternativ:")
#Håller programet i gång tills användaren säger nej 
while True:
    #Visar alternativen till användaren
    print("1. Skriv ut en existerande lista")
    print("2. Lägg till ett föremål i listan")
    print("3. Ta bort ett föremål ur listan")
    print("4. Ändra ett föremål i listan")
    print("5. Avsluta")
    #Tar in val från användaren
    operation = int(input())
    print("")
    #Utför valet som användaren har valt
    #Kollar om användaren vill avsluta
    if(operation == 5):
        break
    elif(operation == 4):
        shopping_edit(lista)
    elif(operation == 3):
        shopping_remove(lista)
    elif(operation == 2):
        shopping_add(lista)
    elif(operation == 1):
        shopping_list(lista)
    else:
        #om det inte är ett siffra mellan 1-5 
        print("Fel gör om")
    print("")

#Programet har avslutats
print("Hej då!")
        

