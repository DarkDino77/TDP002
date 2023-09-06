#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import string
from card_deck_adt import *
#Get token 
def get_letter(deck, list_of_letters):
    alphabet = list(string.ascii_uppercase)
    value_of_top = value_of_card_at_index(deck, 0)
    # Skippar jokern
    if value_of_top != 27 :
        # Får värdet för tokenen
        letter_value = value_of_card_at_index(deck, value_of_top + 1)
        #get_letter_by_value(letter_value)
        # Skippar jokern
        if letter_value != 27:
            # Sätter in tokenen i listan av tokens
            # Konveterar värde för token till token
            list_of_letters.append(alphabet[letter_value - 1])
            
'''        Detta behövs inte mer 
def print_list(list_of_letters):
    for letter in list_of_letters:
        print(letter, end="")
    print("\n")
'''

#SUYLZJXNHTBLBIGNQLJMBNEEUAOZKN

# Move the joker card down the deck by one
# If at bottom: move to one below top
def move_joker(deck, joker):
    index = index_of_card(deck, joker)
    if index <= length_of_deck(deck) - 1:
        move_index(deck, index, index + 1 )
    else:
        move_index(deck, index, 1 )
        
# Tar bort en del av decket 
def remove_section_of_deck(deck, start, end):
    for index in range(end -1 , start -1 , -1):
        remove_index_from_deck(deck, index)
        
# Hittar första jokern i decket
def identify_first_joker(deck):
    for index in range(length_of_deck(deck)):
        if index_of_card(deck, get_card_at_index(deck, index)) == index_of_card(deck, "jokerA") or index_of_card(deck, get_card_at_index(deck, index)) == index_of_card(deck, "jokerB"):
            return index
        
# Hittar andra jokern i decket
def identify_second_joker(deck, firstJoker):
    if firstJoker == index_of_card(deck, "jokerA"):
        return index_of_card(deck, "jokerB")
    else:
        return index_of_card(deck, "jokerA")
    
# Delar decket ABC till CBA
def split_deck_in_3(deck):
    #Delar in Deck A
    firstJoker = identify_first_joker(deck)
    section_A = section_of_deck(deck, 0, firstJoker)
    remove_section_of_deck(deck, 0, firstJoker)
    #Delar in Deck B
    firstJoker = identify_first_joker(deck)
    secondJoker = identify_second_joker(deck, firstJoker)
    section_B = section_of_deck(deck, 0, secondJoker+1)
    remove_section_of_deck(deck, 0, secondJoker+1)
    #Delar in Deck C
    section_C = section_of_deck(deck, 0, length_of_deck(deck))
    remove_section_of_deck(deck, 0, length_of_deck(deck))
    #Sätter i hop delarna till CBA
    whole = section_C + section_B + section_A
    merge_deck(deck, whole)
    
#Flyttar ner kort baserat på nedersta kortet 
def move_cards_down(deck):
    valueOfBottom = value_of_card_at_index(deck, length_of_deck(deck)-1)
    for i in range(valueOfBottom):
        move_index(deck, 0, length_of_deck(deck)-1)
        
def solitaire_keystream(length, deck):
    list_of_letters = []
    #Blanda kortleken inklusive jokrarna. 
    deck_shuffle(deck)
    while len(list_of_letters) < length:
        #Flytta joker A
        move_joker(deck, "jokerA")
        #Flytta joker B
        move_joker(deck, "jokerB")
        move_joker(deck, "jokerB")
        # Deck delar ABC till CBA
        split_deck_in_3(deck)
        #Flyttar ner kort
        move_cards_down(deck)
        #get token 
        get_letter(deck, list_of_letters)
    #Returnerar en stirng 
    return "".join(list_of_letters)

# Tar bort teken som inte är A-Z
def remove_unwanted_characters(word):
    alphabet = list(string.ascii_uppercase)
    word_list = []
    for letter in word:
        if letter in alphabet:
            word_list.append(letter)
    
    return word_list

# Kållar om summa värdet inte är över 26
#def cheack_value_if_exceds_accepteble_value(value):
#    if value > 26:
#        value = value - 26
#    return value

# Conveterar bokstäver till siffror
def convert_letters_to_numbers(list_of_letters):
    alphabet = list(string.ascii_uppercase)
    list_of_values = []
    #Går igenom listan
    for letter in list_of_letters:
        value = alphabet.index(letter) + 1 
        list_of_values.append(value)
    return list_of_values

# Adderar ihop två listor 
def addition_of_values(list_of_values_1, list_of_values_2):
    final_list_of_values = []
    for index in range(len(list_of_values_1)):
        value = list_of_values_1[index] + list_of_values_2[index]
        # Kollar om värdet är över 26 annars tar bort 26
        if value > 26:
            value = value - 26
        final_list_of_values.append(value)
    return final_list_of_values

# Gör om siffror till bokstäver
def convert_values_to_letters(list_of_values):
    alphabet = list(string.ascii_uppercase)
    list_of_letters = []
    for value in list_of_values:
        list_of_letters.append(alphabet[value-1])
    return list_of_letters

# Krypterar ett ord
def solitaire_encrypt(word, deck):
    word = word.upper()
    # Tarbort charactärer vi inte vill ha
    word = remove_unwanted_characters(word)
    # Generear en nykel
    key = solitaire_keystream(len(word),deck)
    # Gör om bokstäver till siffror
    word = convert_letters_to_numbers(word)
    key = convert_letters_to_numbers(key)
    # Adderar nykeln med ord
    encrypted_values = addition_of_values(word, key)
    # Gör om siffror tillbokstäver
    encrypted_letters = convert_values_to_letters(encrypted_values)
    
    return "".join(encrypted_letters)

# Subtraherar två listor från varandra 
def subtraktion_of_values(list_of_values_1, list_of_values_2):
    final_list_of_values = []
    for index in range(len(list_of_values_1)):
        value = list_of_values_1[index] - list_of_values_2[index]
        # Kollar om värdet är under 1 annars lägger till 26
        if value < 1 :
            value = value + 26
        final_list_of_values.append(value)
    return final_list_of_values

# Kör decrypterings processen
def solitatire_decrypt(encrypted_word, second_deck):
    # Generear en nykel#
    key = solitaire_keystream(len(encrypted_word), second_deck)
    # Gör om bokstäver till siffror
    word = convert_letters_to_numbers(encrypted_word)
    key = convert_letters_to_numbers(key)
    # Subtraherar ord med nykeln
    decrypted_values = subtraktion_of_values(word, key)
    # Gör om siffror tillbokstäver
    decrypted_letters = convert_values_to_letters(decrypted_values)
    return "".join(decrypted_letters)

def main():
    # Skapar deck
    deck = create_deck()
    # Kör keystream
    length = int(input("How long should the sipher be: " ))
    key = solitaire_keystream(length, deck)
    print(f"Detta är resultaten av en {length} length key steam: " + key)
    # Skapar decks
    deck1 = create_deck()
    second_deck = create_deck()
    # Kör krypteringen 
    word = input("Skriv in ord du vill kryptera: ")
    encrypted_word = solitaire_encrypt(word, deck1)
    print("Detta är ett krypterat ord: " + encrypted_word)
    # Kör dekrypteringen på det krypterade ordet
    decrypted_word = solitatire_decrypt(encrypted_word, second_deck)
    print("Detta är ett okryptterat ord: " + decrypted_word)

main()
