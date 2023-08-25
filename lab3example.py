#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import random
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

def display_card(card):
    
    match get_suit(card):
         case 1:
              suit ="Hearts "
         case 2:
              suit ="Spades" 
         case 3:
              suit ="Diamonds"
         case 4:
              suit ="Clubs"
    
    print(f"{get_value(card)} of {suit}")
    
def remove_card(deck, card):
    deck[1].remove(card)

def move_card(deck, card, position):
    remove_card(deck, card)
    insert_card(deck, card, position)
    
def get_card_at_index(deck, index):
    return deck[1][index-1]

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
    for index in range(start, end):
        remove_index_from_deck(deck, index)
    print(deck)
        
    

def split_deck_in_3(deck):
    firstjoker = identify_joker_index(deck)
    section_A = section_of_deck(deck, 0, firstjoker)
    remove_section_of_deck(deck, 0, firstjoker)
    secondjoker = identify_joker_index(deck)
    section_B = section_of_deck(deck, 0, secondjoker)
    remove_section_of_deck(deck, 0, secondjoker)
    section_C = section_of_deck(deck, 0, len(deck[1]))
    remove_section_of_deck(deck, 0, len(deck[1])-1)
    hole = section_C + section_B + section_A
    deck[1].append(hole)

'''    
def solitaire_keystream(length, deck):
    deck_shuffle(deck)
    move_joker_1(deck)
    move_joker_2(deck)
    split_deck_in_3(deck)
    move_cards_down(deck)
    get_letter(deck)
     

'''


