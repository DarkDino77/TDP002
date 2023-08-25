import random
def create_card(value, suit):
    return (value, suit)

def insert_card(deck, card, position):
    deck[1].insert(position-1, card)
    
def place_card_on_top(deck, card):
    insert_card(deck, card, 0)

get_card_at_index()

def create_deck():
    deck =['deck', [] ]
    for suit in range(1, 3):
        #Card number 14 is joker
        for value in range(1, 15):
            card = create_card(value, suit)
            deck[1].append(card)
    return deck

def get_value(card):
    value = card[1]
    return card[1]

def get_suit(card):
    return card[0]

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

def move_index(deck, index, position):
    card = get_card_at_index(deck, index)
    remove_card(deck, card)
    insert_card(deck card, position)

def deck_shuffle(deck, seed):
    random.shuffle(deck[1], seed)


