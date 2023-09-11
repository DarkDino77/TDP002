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
    
def main():
    """
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
    


main()