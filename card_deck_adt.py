#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import random
# Create a new card represented as Tuple.
def create_card(value, suit):
    return (value, suit)

# Insert a given card into a deck at the specified position
# Position 0 is top of deck
def insert_card(deck, card, position):
    deck[1].insert(position-1, card)
    
# Create a new deck
def create_deck():
    deck = ['deck', [] ]
    for suit in range(1, 3):
        #Card number 14 is joker
        for value in range(1, 15): 
            card = create_card(value, suit)
            deck[1].append(card)
    return deck
# Return the value of a card according to parameters 
def get_value(card):
    value = card[0]
    suit = get_suit(card)
    if suit == 2 or value == 14:
        value = value + 13
    return value

# Get the suit of a card
def get_suit(card):
    return card[1]

# Remove a card from a deck
def remove_card(deck, card):
    deck[1].remove(card)
    
# Move a card in a deck to another position in same deck
def move_card(deck, card, position):
    remove_card(deck, card)
    insert_card(deck, card, position)
    
# Return the card from deck at the specified index
def get_card_at_index(deck, index):
    return deck[1][index]

# Move a card in a deck to another position in same deck using the index as position
def move_index(deck, index, position):
    card = get_card_at_index(deck, index)
    remove_card(deck, card)
    insert_card(deck, card, position)
    
#Blanda kortleken inklusive jokrarna. 
def deck_shuffle(deck):
    random.seed(10)
    random.shuffle(deck[1])

# Get the index of first joker in deck that matches suit
def identify_joker_index_by_suit(deck, suit):
    for card in deck[1]:
        if get_value(card) == 27:
            if get_suit(card) == suit:
                return index_of_card(deck, card)

# Get the index of a card in a deck    
def index_of_card(deck, card):
    if card == "jokerA":
        card = get_card_at_index(deck, identify_joker_index_by_suit(deck, 1))
    if card == "jokerB":
        card = get_card_at_index(deck, identify_joker_index_by_suit(deck, 2))
    return deck[1].index(card)


"""  for card in deck[1]:
       if get_value(card) == 27:
               return index_of_card(deck, card)"""
      
# Return a new section of a deck between start and end            
def section_of_deck(deck, start, end):
    return deck[1][start:end]

# Remove the card at the specified index in the deck
def remove_index_from_deck(deck, index):
    del deck[1][index]
    
# Return the size of a deck
def length_of_deck(deck):
    return len(deck[1])

#Replace deck with another deck
def merge_deck(deck, whole):
    deck[1] = whole

#Return the value of an index
def value_of_card_at_index(deck, index):
    return get_value(get_card_at_index(deck, index))


'''
def get_letter_by_value(letter_value):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "X", "Y", "Z"]
    return alphabet[letter_value]
'''

