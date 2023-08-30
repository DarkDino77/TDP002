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

# Place a new card at top of the deck
def place_card_on_top(deck, card):
    insert_card(deck, card, 0)

# Create a new deck
def create_deck():
    deck = ['deck', []]

    for suit in range(1, 3):
        # Card number 14 is joker
        for value in range(1, 15):
            if value * 2 == 28:
                card = create_card(27, suit)
            elif suit == 2:
                card = create_card(value + 13, suit)
            else:
                card = create_card(value, suit)
            deck[1].append(card)
    return deck

# Return the value of a card
def get_value(card):
    return card[0]

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

# Shuffle the deck
def deck_shuffle(deck):
    random.seed(10)
    random.shuffle(deck[1])
    
# Get the index of a card in a deck
def index_of_card(deck, card):
    return deck[1].index(card)

# Get the index of first joker in deck that matches suit
def identify_joker_index_by_suit(deck, suit):
    for card in deck[1]:
        if get_value(card) == 27:
            if get_suit(card) == suit:
                return index_of_card(deck, card)
            
# Get the index of first joker in deck
def identify_joker_index(deck):
    for card in deck[1]:
        if get_value(card) == 27:
                return index_of_card(deck, card)

# Move the indexed card down the deck by one
# If at bottom: move to top
def move_index_down_one(deck, index):
    if (index + 1) > 28:
        move_index(deck, index, 0)
    else:
        move_index(deck, index, index + 1)

# Move the joker with indicated suit down one in the deck
def move_joker_down_one(deck, suit):
    index = identify_joker_index_by_suit(deck, suit)
    move_index_down_one(deck, index)

#Detta är fult
    # Ja, det är det -Phibr608
def move_joker_1(deck):
    move_joker_down_one(deck, 1)

def move_joker_2(deck):
    move_joker_down_one(deck, 2)
    move_joker_down_one(deck, 2)
    
# Return a new section of a deck between start and end
def section_of_deck(deck, start, end):
    return deck[1][start:end]

# Remove the card at the specified index in the deck
def remove_index_from_deck(deck, index):
    del deck[1][index]
    
# Remove a section from a deck
def remove_section_of_deck(deck, start, end):
    for index in range(end -1 , start -1 , -1):
        remove_index_from_deck(deck, index)

# Return the size of a deck
def length_of_deck(deck):
    return len(deck[1])

# 
def identify_second_joker(deck, firstJoker):
    suitOfFirstJoker = get_suit(get_card_at_index(deck, firstJoker))
    if suitOfFirstJoker == 1:
        return identify_joker_index_by_suit(deck, 2)
    else:
        return identify_joker_index_by_suit(deck,1)

# Merge two decks together
    # Does this work? -phibr608
def merge_deck(deck, whole):
    deck[1] = whole

# Move the whole deck down by one card?
def move_cards_down(deck):
    valueOfBottom = get_value(get_card_at_index(deck, length_of_deck(deck)-1))
    for i in range(valueOfBottom):
        move_index(deck, 0, length_of_deck(deck)-1)


'''
def get_letter_by_value(letter_value):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "X", "Y", "Z"]
    return alphabet[letter_value]
'''

