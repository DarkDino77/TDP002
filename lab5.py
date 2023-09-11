#Uppgift 1a - Summera alla naturliga tal upp till och med 512 
#Uppgift 1b - Produkten av alla positiva heltal upp till och med 512
# En funktion två lambda utryck
#5a

def calculation(math):
    a = 1
    for i in range(2,513):
         a = math(i, a)
    return a



#5b
""" 
En databas över personer som arbetar på ett företag definieras som en lista med tabeller.
 Skriv en funktion som söker i databasen. 
 Första argumentet till funktionen är databasen som ska genomsökas,
 andra argumentet anger vilket fält matchningen ska ske emot och tredje argumentet anger vilket värde det fältet ska ha.
 Returvärdet ska vara en lista med de poster i databasen som matchar sökningen. """

def dbsearch(db, feildsearch, value):
    return [dictonary for dictonary in db if dictonary[feildsearch] == value]




#5c
"""
Skriv en funktion som tar reda på om en viss lista innehåller ett visst element. 
Du får inte använda dig av Pythons in-operator! """
"""
def contains(word_to_search_for, sentencs):
    contain = False
    for word in sentencs:
        if word == word_to_search_for:
            contain = True
    return contain
"""

def contains(word_to_search_for, sentencs):
    contain = False
    if [word for word in sentencs if word_to_search_for == word]:
        contain = True
    return contain



#5d
"""
Den här uppgiften går ut på att konstruera ett simpelt kommando-system
där användaren presenteras med en kommandoprompt och kan skriva in kommandon som sedan tolkas och anropar lämpliga funktioner. 
Systemet ska vara ganska likt en terminal, fast begränsat. 
Notera att även detta är en interpretator likt uppgift 4b och 
även om uppgifterna till en början förefaller helt olika varandra kommer ni snart märka att skillnaderna är väldigt små.
Observera att detta kan och skall utföras helt med hjälp av Pythons standardbibliotek,
inte med hjälp av anrop till terminalen.

Följande kommandon ska finnas tillgängliga:
pwd 	Skriv ut nuvarande arbestkatalog.
cd 	    Byt nuvarande arbetskatalog.
ls 	    Lista innehållet i nuvarande arbetskatalog
cat 	Skriv ut innehållet i en fil


https://docs.python.org/3/library/os.path.html
"""

import os

def lss():
    directery = os.listdir("./")
    for file in directery:
        print(file)

def pwd():
    print(os.getcwd())

def cat(command):
    command = command.split(" ")
    with open(command[-1], "r", encoding = "UTF-8") as file:
        for row in file:
            print(row,end="")
        print("")
    file.close()
   # with open(command)
def cds(command):
    command = command.split(" ")
    os.chdir(command[-1])

def commands():
    
    command = input("command> ")
    if command == "pwd":
        pwd()
        commands()
    elif command == "ls":
        lss()
        commands()
    elif "cat" in command:
        cat(command)
        commands()
    elif "cd" in command:
        cds(command)
        commands()
    else:
        print("Ogiltigt commando")
        commands()


#5e
"""
Skriv en listgenererande funktion, generate_list. 
Funktionen ska ta en funktion som första argument och ett heltal som andra argument. 
Funktionen som angetts som första argument ska ta ett siffervärde som enda argument 
och skall anropas så många gånger som heltalet anger, med ett ökande siffervärde varje gång. 
Resultatet av funktionen ska läggas i en lista som slutligen returneras från generate_list.
"""

def generate_list(func, length):
    temp_list = []
    for i in range(1, length + 1):
        temp_list.append(func(i))
    return temp_list

def mirror(x): return x

def stars(n): return '*' * n


#5f
"""
Skriv en funktion partial som tar en annan funktion och ett värde som indata.
Partial ska returnera en ny funktion som gör samma sak som den angivna funktionen men där
första argumentet till den angivna funktionen är bundet till det värde som angavs som andra argument till partial. 
"""
#detta käns fel
def partial(func, data):
    return lambda m: func(data, m)


def add(n, m): return n + m



#5g
"""
Skriv en funktion compose som tar två funktioner som argument, 
vi kallar dem F_a och F_b, och returnerar en funktion, F_res,
som innebär att utdata från den andra funktionen blir indata till den första, dvs F_res(x) = F_a(F_b(x)). 
"""

def compose(F_a, F_b):
    return lambda m: F_a(F_b(m))

def multiply_five(n):
   return n * 5

def add_ten(x):
    return x + 10



"""
Uppgift 5h - Filter the mapped result
Skriv en funktion make_filter_map som tar en filter-funktion och en map-funktion som argument. 
Funktionen ska returnera en funktion som tar en lista som argument och
applicerar map-funktionen på varje element i listan som filter-funktionen är sann för. 
make_filter_map ska använda funktionerna partial och 
compose från tidigare uppgifter för att sätta ihop funktionerna map och 
filter med indatafunktionerna till det önskade resultatet. 
"""
#def compose(F_a, F_b):
 #   return lambda n: F_a(F_b(n))
# def partial(func, data):
#    return lambda m: func(data, m)
def make_filter_map(uneven, square):
    #return lambda length: [map(i) for i in length if filter(i)]
    
    assigend_square_to_map = partial(map, square)
    assigend_uneven_to_filter = partial(filter, uneven)
    cheack_if_uneven_and_square_it = compose(assigend_uneven_to_filter, assigend_square_to_map)

    return lambda length: list(cheack_if_uneven_and_square_it(i for i in length ))
  # printed value [1, 9, 25, 49, 81]
#5d kvar

def main():
    #5a
    print("5a")
    math = lambda a, b : a + b 
    i = calculation(math)
    print(f"Summan av alla tal mellan 1 till 512 är: {i}")

    math = lambda a, b : a * b 
    i = calculation(math)
    print(f"Multiplikationen av alla tal mellan 1 till 512 är: {i}")
    #
    #5b
    print("")
    print("5b")
    db = [
            {'name': 'Jakob', 'position': 'assistant'},
            {'name': 'Åke', 'position': 'assistant'},
            {'name': 'Ola', 'position': 'examiner'},
            {'name': 'Henrik', 'position': 'assistant'}
            ]

    print(dbsearch(db, 'position', 'examiner'))
    #
    #5c
    print("")
    print("5c")
    haystack = 'Can you find the needle in this haystack?'.split()

    print(contains('find', haystack))

    print(contains('needle', haystack))

    print(contains('haystack', haystack))
    #
    #5e
    print("")
    print("5e")
    print(generate_list(mirror, 4))
    #[1, 2, 3, 4]
    print(generate_list(stars, 5))
    #['*', '**', '***', '****', '*****'][word for word in sentencs if word_to_search_for == word]
    #
    #5f
    #...
    print("")
    print("5f")
    add_five = partial(add, 5)
    print(add_five(3))
    #8
    print(add_five(16))
    #21
    #
    #5g
    print("")
    print("5g")
    composition = compose(multiply_five, add_ten)
    print(composition(3))
    #65
    another_composition = compose(add_ten, multiply_five)
    print(another_composition(3))
    #25
    #
    #5h
    print("")
    print("5h")
    process = make_filter_map(lambda x: x % 2 == 1, lambda x: x * x)
    print(process(range(10)))
    #[1, 9, 25, 49, 81]
    #
    #5d
    print("")
    print("5d")
    wait = input("Starta commando programet")
    os.system('clear')
    commands()
    #

main()