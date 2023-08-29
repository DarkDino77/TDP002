#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import random
import string

def create_card(value, suit):
    return (value, suit)

def insert_card(deck, card, position):
    deck[1].insert(position-1, card)
    
def place_card_on_top(deck, card):
    insert_card(deck, card, 0)

def create_deck():
    deck = ['deck', [] ]
    for suit in range(1, 3):
        #Card number 14 is joker
        for value in range(1, 15):
            
            if value * 2 == 28:
                card = create_card(27, suit)
            elif suit == 2:
                card = create_card(value + 13, suit)
            else:
                card = create_card(value, suit)
            deck[1].append(card)
    return deck

def get_value(card):
    return card[0]

def get_suit(card):
    return card[1]
    
def remove_card(deck, card):
    deck[1].remove(card)

def move_card(deck, card, position):
    remove_card(deck, card)
    insert_card(deck, card, position)
    
def get_card_at_index(deck, index):
    return deck[1][index]

def move_index(deck, index, position):
    card = get_card_at_index(deck, index)
    remove_card(deck, card)
    insert_card(deck, card, position)

def deck_shuffle(deck):
    random.seed(10)
    random.shuffle(deck[1])
    
def index_of_card(deck, card):
    return deck[1].index(card)

def identify_joker_index_by_suit(deck, suit):
    for card in deck[1]:
        if get_value(card) == 27:
            if get_suit(card) == suit:
                return index_of_card(deck, card)
            
def identify_joker_index(deck):
    for card in deck[1]:
        if get_value(card) == 27:
                return index_of_card(deck, card)
            


def move_index_down_one(deck, index):
    if (index + 1) > 28:
        move_index(deck, index, 0)
    else:
        move_index(deck, index, index + 1)

def move_joker_down_one(deck, suit):
    index = identify_joker_index_by_suit(deck, suit)
    move_index_down_one(deck, index)
    
def move_joker_1(deck):
    move_joker_down_one(deck, 1)
#Detta är fult
def move_joker_2(deck):
    move_joker_down_one(deck, 2)
    move_joker_down_one(deck, 2)
    
def section_of_deck(deck, start, end):
    return deck[1][start:end]

def remove_index_from_deck(deck, index):
    del deck[1][index]
    
    
def remove_section_of_deck(deck, start, end):
    for index in range(end -1 , start -1 , -1):
        remove_index_from_deck(deck, index)
        
    

def split_deck_in_3(deck):
    firstJoker = identify_joker_index(deck)
    section_A = section_of_deck(deck, 0, firstJoker)
    remove_section_of_deck(deck, 0, firstJoker)
    firstJoker = identify_joker_index(deck)
    suitOfFirstJoker = get_suit(get_card_at_index(deck, firstJoker))
    if suitOfFirstJoker == 1:
        secondJoker = identify_joker_index_by_suit(deck, 2)
    else:
        secondJoker = identify_joker_index_by_suit(deck,1)
    section_B = section_of_deck(deck, 0, secondJoker+1)
    remove_section_of_deck(deck, 0, secondJoker+1)
    section_C = section_of_deck(deck, 0, len(deck[1]))
    remove_section_of_deck(deck, 0, len(deck[1]))
    hole = section_C + section_B + section_A
    deck[1] = hole
 
def move_cards_down(deck):
    valueOfBottom = get_value(get_card_at_index(deck, len(deck[1])-1))
    for i in range(valueOfBottom):
        move_index(deck, 0, len(deck[1])-1)
'''
def get_letter_by_value(letter_value):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "X", "Y", "Z"]
    return alphabet[letter_value]
'''

def get_letter(deck,list_of_letters):
    alphabet = list(string.ascii_uppercase)
    value_of_top = get_value(get_card_at_index(deck, 0))
    if value_of_top != 27 :
        letter_value = get_value(get_card_at_index(deck, value_of_top + 1))
        #get_letter_by_value(letter_value) 

        list_of_letters.append(alphabet[letter_value - 1])
'''        Detta behövs inte mer 
def print_list(list_of_letters):
    for letter in list_of_letters:
        print(letter, end="")
    print("\n")
'''
#SUYLZJXNHTBLBIGNQLJMBNEEUAOZKN

def solitaire_keystream(length, deck):
    list_of_letters = []
    while len(list_of_letters) < length:
        deck_shuffle(deck)  
        move_joker_1(deck)
        move_joker_2(deck)
        split_deck_in_3(deck)
        move_cards_down(deck)
        get_letter(deck, list_of_letters)
    #print("".join(list_of_letters))
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
second_deck = create_deck()
key = solitaire_keystream(30, deck)
print(key)
deck1 = create_deck()
second_deck = create_deck()
encrypted_word = solitaire_encrypt("Python", deck1)
print(encrypted_word)
word = solitatire_decrypt(encrypted_word, second_deck)
print(word)



