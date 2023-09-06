#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import string
from card_deck_adt import *

def get_letter(deck, list_of_letters):
    alphabet = list(string.ascii_uppercase)
    value_of_top = value_of_card_at_index(deck, 0)
    if value_of_top != 27 :
        letter_value = value_of_card_at_index(deck, value_of_top + 1)
        #get_letter_by_value(letter_value) 
        if letter_value != 27:
            list_of_letters.append(alphabet[letter_value - 1])
            
'''        Detta behövs inte mer 
def print_list(list_of_letters):
    for letter in list_of_letters:
        print(letter, end="")
    print("\n")
'''

#SUYLZJXNHTBLBIGNQLJMBNEEUAOZKN

def move_joker(deck, joker):
    index = index_of_card(deck, joker)
    if index <= length_of_deck(deck) - 1:
        move_index(deck, index, index + 1 )
    else:
        move_index(deck, index, 1 )
def remove_section_of_deck(deck, start, end):
    for index in range(end -1 , start -1 , -1):
        remove_index_from_deck(deck, index)
        
def identify_first_joker(deck):
    for index in range(length_of_deck(deck)):
        if index_of_card(deck, get_card_at_index(deck, index)) == index_of_card(deck, "jokerA") or index_of_card(deck, get_card_at_index(deck, index)) == index_of_card(deck, "jokerB"):
            return index
"""  for card in deck[1]:
       if get_value(card) == 27:
               return index_of_card(deck, card)""" 

def identify_second_joker(deck, firstJoker):
    if firstJoker == index_of_card(deck, "jokerA"):
        return index_of_card(deck, "jokerB")
    else:
        return index_of_card(deck, "jokerA")

def split_deck_in_3(deck):
    firstJoker = identify_first_joker(deck)
    section_A = section_of_deck(deck, 0, firstJoker)
    remove_section_of_deck(deck, 0, firstJoker)
    firstJoker = identify_first_joker(deck)
    secondJoker = identify_second_joker(deck, firstJoker)
    section_B = section_of_deck(deck, 0, secondJoker+1)
    remove_section_of_deck(deck, 0, secondJoker+1)
    section_C = section_of_deck(deck, 0, length_of_deck(deck))
    remove_section_of_deck(deck, 0, length_of_deck(deck))
    whole = section_C + section_B + section_A
    merge_deck(deck, whole)

def move_cards_down(deck):
    valueOfBottom = value_of_card_at_index(deck, length_of_deck(deck)-1)
    for i in range(valueOfBottom):
        move_index(deck, 0, length_of_deck(deck)-1)
        
def solitaire_keystream(length, deck):
    list_of_letters = []
    deck_shuffle(deck)
    while len(list_of_letters) < length: 
        move_joker(deck, "jokerA")
        move_joker(deck, "jokerB")
        move_joker(deck, "jokerB")
        split_deck_in_3(deck)
        move_cards_down(deck)
        get_letter(deck, list_of_letters)
    return "".join(list_of_letters)

def remove_unwanted_characters(word):
    alphabet = list(string.ascii_uppercase)
    word_list = []
    for letter in word:
        if letter in alphabet:
            word_list.append(letter)
    
    return word_list

def cheack_value_if_exceds_accepteble_value(value):
    if value > 26:
        value = value - 26
    return value

def convert_letters_to_numbers(list_of_letters):
    alphabet = list(string.ascii_uppercase)
    list_of_values = []
    for letter in list_of_letters:
        value = alphabet.index(letter) + 1 
        list_of_values.append(value)
    return list_of_values

def addition_of_values(list_of_values_1, list_of_values_2):
    final_list_of_values = []
    for index in range(len(list_of_values_1)):
        value = list_of_values_1[index] + list_of_values_2[index]
        value = cheack_value_if_exceds_accepteble_value(value)
        final_list_of_values.append(value)
    return final_list_of_values
    
def convert_values_to_letters(list_of_values):
    alphabet = list(string.ascii_uppercase)
    list_of_letters = []
    for value in list_of_values:
        list_of_letters.append(alphabet[value-1])
    return list_of_letters

def solitaire_encrypt(word, deck):
    #transform_small_letters_to_large
    word = word.upper()
    word = remove_unwanted_characters(word)
    key = solitaire_keystream(len(word),deck)
    word = convert_letters_to_numbers(word)
    key = convert_letters_to_numbers(key)
    encrypted_values = addition_of_values(word, key)
    encrypted_letters = convert_values_to_letters(encrypted_values)
    
    return "".join(encrypted_letters)

def subtraktion_of_values(list_of_values_1, list_of_values_2):
    final_list_of_values = []
    for index in range(len(list_of_values_1)):
        value = list_of_values_1[index] - list_of_values_2[index]
        if value < 1 :
            value = value + 26
        final_list_of_values.append(value)
    return final_list_of_values

def solitatire_decrypt(encrypted_word, second_deck):
    key = solitaire_keystream(len(encrypted_word), second_deck)
    word = convert_letters_to_numbers(encrypted_word)
    key = convert_letters_to_numbers(key)
    decrypted_values = subtraktion_of_values(word, key)
    decrypted_letters = convert_values_to_letters(decrypted_values)
    return "".join(decrypted_letters)

deck = create_deck()
length = int(input("How long should the sipher be: " ))
key = solitaire_keystream(length, deck)
print(f"Detta är resultaten av en {length} length key steam: " + key)
deck1 = create_deck()
second_deck = create_deck()
word = input("Skriv in ord du vill kryptera: ")
encrypted_word = solitaire_encrypt(word, deck1)
print("Detta är ett krypterat ord: " + encrypted_word)
decrypted_word = solitatire_decrypt(encrypted_word, second_deck)
print("Detta är ett okryptterat ord: " + decrypted_word)
