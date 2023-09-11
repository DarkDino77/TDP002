"""
 Uppgift 6a - Linjärsökning

Linjärsökning är den simplaste formen av sökning ni kan tänka er. 
Det går helt enkelt ut på att ni börjar söka från början av listan och
slutar när ni hittar elementet ni letar efter eller kommer till slutet av listan.
Linjärsökning har fördelen att den även fungerar för osorterad data.
Skriv en funktion linear_search som söker igenom en lista (haystack) efter ett specifikt värde (needle). 
Funktionen ska dessutom ha möjlighet
att ta ett tredje argument med en funktion för att specificera hur jämförelsen ska gå till.  
"""
import re

def linear_search(list_to_search, value, search_function = ""):
    searched = ""
    for record in list_to_search:
        if search_function == "":
            if value in record.values():
                    searched = record
        elif search_function != "":
            if search_function(record) == value:
                searched = record

    return searched
    
def binary_search_no_func(people, value, left = 0 , right = 0):
    if right == 0:
        right = len(people) - 1
    if left <= right:
          middle = (left + right) // 2
          for element in people[middle]:
               finding = people[middle][element]
               if type(finding) == type(value):
                    if value == finding:
                        return people[middle]
                    if value < finding:
                        return binary_search_no_func(people[middle + 1:], value, left , right = len(people[middle + 1 :]))
                    elif value > finding:
                        return binary_search_no_func(people[:middle], value, left , right = len(people[:middle]))
    return None
                    

def binary_search_func(people, value, func= "", left = 0 , right = 0):
    if right == 0:
        right = len(people) - 1
    if left <= right:
          middle = (left + right) // 2
          if value == func(people[middle]):
               return people[middle]
          if value > func(people[middle]):
               return binary_search_func(people[middle + 1:], value, func, left , right = len(people[middle + 1 :]))
          elif value < func(people[middle]):
               return binary_search_func(people[:middle], value, func, left , right = len(people[:middle]))
    return None

def binary_search(people, value, func = "", left = 0 , right = 0):
    right = len(people) - 1 
    if func == "":         
         return binary_search_no_func(people, value, left, right)
    if func != "":
         return binary_search_func(people, value, func, left, right)
    

def insertion_sort(db, func = ""):
    dba = db.copy()
    if func == "":
        for i in range(len(dba)):
            j = i
            while j > 0 and dba[j - 1] > dba[j]:
                dba[j], dba[j-1] = dba[j-1], dba[j]
                j -= 1
    if func != "":            
        for i in range(len(dba)):
            j = i
            while j > 0 and (func(dba[j - 1]) > func(dba[j]) or (func(dba[j - 1]) == func(dba[j]) and dba[j - 1] > dba[j] )):
                dba[j], dba[j-1] = dba[j-1], dba[j]
                j -= 1
    return dba

def partion(db, low , high, func):
    pivot = func(db[high]) 
    j = low - 1
    for i in range(low, high):    
        if func(db[i]) <= pivot:
            j += 1
            db[i], db[j] = db[j], db[i]
    db[j + 1], db[high] = db[high], db[j + 1]
    return j + 1

def quicksort(db, func, low = 0, high = None):
    if high == None:
        high = len(db) - 1
    if low < high:
        pivot = partion(db, low, high, func)
        quicksort(db, func, low, pivot-1)
        quicksort(db, func, pivot + 1, high)

    
def main():
    #5a
    """
    print("5a")
    imdb = [
            {'title': 'The Rock', 'actress': 'Nicholas Cage', 'score': 11},          
            {'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10},    
            {'title': 'Black Hawk Down', 'actress': 'Eric Bana', 'score': 12},
            ]

    print(linear_search(imdb, 10, lambda e: e['score']))
    print(linear_search(imdb, 'Black Hawk Down', lambda e: e['title']))
    print(linear_search(imdb, 'Nicholas Cage', lambda e: e['actress']))
    print(linear_search(imdb, 11))
    print(linear_search(imdb, "The Rock"))
    print(linear_search(imdb, "Eric Bana"))
    """
    #5b
    """
    print("")
    print("5b")
    people = [{'name': 'Pontus', 'age': 30},
              {'name': 'Sara', 'age': 20},
              {'name': 'Xavier', 'age': 19}]
    # listan people är här sorterad på personernas namn      
    print(binary_search(people, 'Pontus', lambda e: e['name']))
    print(binary_search(people, 'Sara', lambda e: e['name']))
    print(binary_search(people, 'Xavier', lambda e: e['name']))
    print(binary_search(people, 20))
    print(binary_search(people, 30))
    print(binary_search(people, 19))
    #{'name': 'Pontus', 'age': 30}
    """
    #5c
    """
    print("")
    print("5c")
    db = [
        ('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
        ('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
        ] 
    dba = insertion_sort(db,lambda e: e[0])
    print(dba)
    dbc = insertion_sort(db)
    print(dbc)
    dbb = insertion_sort(db,lambda e: e[1])
    print(dbb)
    """
    #5d
    
    print("")
    print("5d")
    db = [
        ('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
        ('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
        ] 
    #dba = quicksort(db,lambda e: e[0])
    #print(dba)
    #dbc = quicksort(db)
    dba = db.copy()
    quicksort(db,lambda e: e[0])
    quicksort(dba,lambda e: e[1])
    print(db)
    #quicksort(db,lambda e: e[1])
    print(dba)

main()