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
            card = create_card(value, suit)
            deck[1].append(card)
    return deck

def get_value(card):
    value = card[0]
    suit = get_suit(card)
    if suit == 2 or value == 14 and suit == 1:
        value = value + 13
    return value

def get_suit(card):
    return card[1]
    
def remove_card(deck, card):
    deck[1].remove(card)

def move_card(deck, card, position):
    remove_card(deck, card)
    insert_card(deck, card, position)
    
def get_card_at_index(deck, index):
    return deck[1][index]

def deck_shuffle(deck):
    random.seed(10)
    random.shuffle(deck[1])

def identify_joker_index_by_suit(deck, suit):
    for card in deck[1]:
        if get_value(card) == 27:
            if get_suit(card) == suit:
                return index_of_card(deck, card)
    
def index_of_card(deck, card):
    if card == "jokerA":
        card = get_card_at_index(deck, identify_joker_index_by_suit(deck, 1))
    if card == "jokerB":
        card = get_card_at_index(deck, identify_joker_index_by_suit(deck, 2))
    return deck[1].index(card)

           
def identify_joker_index(deck):
   # print(index)
    #print(deck)
    for card in deck[1]:
        if get_value(card) == 27:
            return index_of_card(deck, card)
        
def remove_index_from_deck(deck, index):
    del deck[1][index]

def section_of_deck(deck, start, end):
    temp = deck[1][start:end]
    for index in range(end -1 , start -1 , -1):
        remove_index_from_deck(deck, index)
    return temp


def length_of_deck(deck):
    return len(deck[1])

def merge_deck(deck, hole):
    deck[1] = hole


def value_of_card_at_index(deck, index):
    return get_value(get_card_at_index(deck, index))

'''
def get_letter_by_value(letter_value):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "X", "Y", "Z"]
    return alphabet[letter_value]
'''