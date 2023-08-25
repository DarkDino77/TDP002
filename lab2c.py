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
