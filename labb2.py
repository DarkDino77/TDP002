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
main()
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
#Uppgift 2a Frame
def frame(string):
     for i in range(3):
            for n in range(len(string) + 3):
                if i == 1:
                    if n == 0 or n == len(string) + 2:
                         print("*", end = " ")
                    elif n == len(string) + 1:
                         print(" ", end="")
                    else:
                         print(string[n - 1], end = "")
                else:
                     print("*", end = "")   
            if i == 1 :
                 print("")
            else:
                print("*")             
string=input("Skriv in Sträng som ska matas in: ")
frame(string)
print('\n')

#Uppgift 2a triangle
def triangle(heigth):
    for i in range (heigth):
        for n in range(i):
            print("**", end ="")
        print("*")
triangle_size = int(input("Skriv in höjd på triangel: "))
triangle(triangle_size)
print('\n')

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
	for heigth in range(scale * 9):
		if heigth != (scale * 4):
			for width in range(scale * 21):
				if width == (scale * 10):
					print(" ", end = "")
				elif width != (scale * 21):
					print("*", end = "")
				else:
					print('\n', end = "")
		print('\n', end = "")
flag_size = int(input("Skriv in flagg storlek: "))
flag(1)
print("\n")
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
def run_code(lista):
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

        operation = input()
        print("")
        #Utför valet som användaren har valt
        #Kollar om användaren vill avsluta
        if(operation == "5"):
            break
        elif(operation == "4"):
            shopping_edit(lista)
        elif(operation == "3"):
            shopping_remove(lista)
        elif(operation == "2"):
            shopping_add(lista)
        elif(operation == "1"):
            shopping_list(lista)
        else:
            #om det inte är ett siffra mellan 1-5 
            print("Fel gör om")
        print("")

    #Programet har avslutats
    print("Hej då!")
lista = create_shopping_list()
run_code(lista)


