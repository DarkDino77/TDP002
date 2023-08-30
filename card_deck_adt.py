#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import random
from card_deck_adt import *

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

def length_of_deck(deck):
    return  len(deck[1])

def identify_second_joker(deck, firstJoker):
    suitOfFirstJoker = get_suit(get_card_at_index(deck, firstJoker))
    if suitOfFirstJoker == 1:
        return identify_joker_index_by_suit(deck, 2)
    else:
        return identify_joker_index_by_suit(deck,1)
def merge_deck(deck, hole):
    deck[1] = hole


def move_cards_down(deck):
    valueOfBottom = get_value(get_card_at_index(deck, length_of_deck(deck)-1))
    for i in range(valueOfBottom):
        move_index(deck, 0, length_of_deck(deck)-1)
'''
def get_letter_by_value(letter_value):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "X", "Y", "Z"]
    return alphabet[letter_value]
'''

