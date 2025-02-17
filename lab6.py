#! /usr/bin/env python3
import re, os, sys

# Uppgift 6a - Linjärsökning
def linear_search(list_to_search, value, search_function = None):
    for record in list_to_search:
        if search_function != None:
            if search_function(record) == value:
                return record
        else:
            if value in record.values():
                return record
    return ""

# 6b    
def binary_search_no_func(people, value, left = 0, right = 0):
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

def binary_search_func_new(people, value, func = "", left = 0, right = 0):
    if right == 0:
        right = len(people) - 1
    if left <= right:
          middle = (left + right) // 2
          if value == func(people[middle]):
               return people[middle]
          if value > func(people[middle]):
               return binary_search_func(people[middle + 1:], value, func, left, right = len(people[middle + 1:]))
          elif value < func(people[middle]):
               return binary_search_func(people[:middle], value, func, left , right = len(people[:middle]))
    return None                    

def binary_search_func(people, value, func = "", left = 0, right = 0):
    if right == 0:
        right = len(people) - 1
    if left <= right:
          middle = (left + right) // 2
          if value == func(people[middle]):
               return people[middle]
          if value > func(people[middle]):
               return binary_search_func(people[middle + 1:], value, func, left, right = len(people[middle + 1:]))
          elif value < func(people[middle]):
               return binary_search_func(people[:middle], value, func, left , right = len(people[:middle]))
    return None

def binary_search(people, value, func = "", left = 0 , right = 0):
    right = len(people) - 1
    if func == "":
         return binary_search_no_func(people, value, left, right)
    if func != "":
         return binary_search_func(people, value, func, left, right)

# 6c
def insertion_sort(db, func = ""):
    dba = db.copy()
    if func == "":
        for i in range(len(dba)): # Loop through every element
            j = i # Make a copy to not mutate the loop iterator
            while j > 0 and dba[j - 1] > dba[j]: # Move dba[j] back until it is at zero or nothing behind it is greater than it
                dba[j], dba[j - 1] = dba[j - 1], dba[j] # Python multiple assignment operation
                j -= 1
    if func != "":            
        for i in range(len(dba)):
            j = i
            while j > 0 and (func(dba[j - 1]) > func(dba[j]) # Run until the function no longer returns a value greater than dba[j]
                or (func(dba[j - 1]) == func(dba[j]) and dba[j - 1] > dba[j])): # If they're the same value then fallback to sorting based on pure value
                dba[j], dba[j - 1] = dba[j - 1], dba[j] # Python multiple assignment operation
                j -= 1
    return dba

# 6d
def partition(db, low, high, func):
    pivot = func(db[high])
    j = low - 1
    for i in range(low, high):    
        if func(db[i]) < pivot or (func(db[i]) == pivot and db[i] <= db[high]):
            j += 1
            db[i], db[j] = db[j], db[i]
    db[j + 1], db[high] = db[high], db[j + 1]
    return j + 1

def quicksort(db, func, low = 0, high = None):
    if high == None:
        high = len(db) - 1
    if low < high:
        pivot = partition(db, low, high, func)
        quicksort(db, func, low, pivot - 1)
        quicksort(db, func, pivot + 1, high)

# 6e
def replace_copyright(copyright_message, path_to_file, types, new_types):
    regex = re.compile("(#\sBEGIN\sCOPYRIGHT)((.|\n)*)(#\sEND\sCOPYRIGHT)")
    
    with open(copyright_message, "r", encoding="UTF-8") as b:
        content = b.read()
        content = regex.search(content).group()

    if os.path.isdir(path_to_file):    

        dir_replacement = os.listdir(path_to_file)
        for files in dir_replacement:

            new_path_to_file = path_to_file + "/" + files
            with open(new_path_to_file, "r", encoding="UTF-8") as f:
                replacement = f.read()
            if regex.search(replacement) and re.search(types, new_path_to_file):
                new_path_to_file = re.sub(f"{types}$", new_types, new_path_to_file )
                with open(new_path_to_file , "w", encoding="UTF-8") as f:
                    f.write(regex.sub(content, replacement))

            
    else:
        with open(path_to_file, "r", encoding="UTF-8") as f:
            replacement = f.read()
        if regex.search(replacement) and re.search(types, path_to_file):
                new_path_to_file = re.sub(f"{types}$", new_types, path_to_file)
                with open(new_path_to_file , "w", encoding="UTF-8") as f:
                    f.write(regex.sub(content, replacement))

    
def main():
    
    #6a
    print("6a")
    imdb = [
        {'title': 'The Rock', 'actress': 'Nicholas Cage', 'score': 11},          
        {'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10},    
        {'title': 'Black Hawk Down', 'actress': 'Eric Bana', 'score': 12}
    ]

    print(linear_search(imdb, 10, lambda e: e['score']))
    print(linear_search(imdb, 'Black Hawk Down', lambda e: e['title']))
    print(linear_search(imdb, 'Nicholas Cage', lambda e: e['actress']))
    print(linear_search(imdb, 11))
    print(linear_search(imdb, "The Rock"))
    print(linear_search(imdb, "Eric Bana"))

    #6b
    print("")
    print("6b")
    
    """
    people = [
        {"name": "Alice", "age": 28},    
        {"name": "Bob", "age": 22},
        {"name": "Charlie", "age": 35},    
        {"name": "Diana", "age": 40},
        {"name": "Eve", "age": 20},    
        {"name": "Frank", "age": 50},    
        {"name": "Grace", "age": 32},    
        {"name": "Hannah", "age": 21},    
        {"name": "Ivy", "age": 28},
        {"name": "Jack", "age": 33},
        {"name": "John", "age": 30},
        {"name": "Kathy", "age": 39},
        {"name": "Leo", "age": 45},
        {"name": "Mandy", "age": 24},
        {"name": "Pontus", "age": 30},
        {"name": "Zara", "age": 25}
    ]"""


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
    
    #6c
    print("")
    print("6c")
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

    #6d
    print("")
    print("6d")
    db = [
        ('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
        ('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
        ] 
    dba = db.copy()
    quicksort(db,lambda e: e[0])
    quicksort(dba,lambda e: e[1])
    print(db)
    print(dba)
 
    #6e
    #Regex utrycket
    #(?<=BEGIN\sCOPYRIGHT)((.|\n)*)(?=(END\sCOPYRIGHT))
    replace_copyright("copyright.txt", "copyright.py", ".py", ".c.py")
    replace_copyright("copyright.txt", "./copyrigth_test", ".py", ".c.py")

def copyrights():
    from_user = sys.argv
    if len(from_user) == 7 and from_user[3] == "-c" and from_user[5] == "-u":
        replace_copyright(from_user[1],from_user[2], from_user[4], from_user[6])

if __name__ == "__main__":
    copyrights()    
    main()