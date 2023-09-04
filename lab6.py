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
def linear_search(list_to_search, value, search_function = None):
    searched = []
    for record in list_to_search:
        if search_function == None and value in record:
            print(record)
            searched.append(record)
        elif search_function in record and record[search_function] == value:
            print(record)
            searched.append(record)
    return searched

imdb = [
    {'title': 'The Rock', 'actress': 'Nicholas Cage', 'score': 11},          
    {'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10},    
    {'title': 'Black Hawk Down', 'actress': 'Eric Bana', 'score': 12},
]

print(linear_search(imdb, 10, lambda e: e['score']))
#{'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10}
  