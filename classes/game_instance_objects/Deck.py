import random

class Deck:
    '''
    Deck is the cards in the players deck
    '''
    def __init__(self):
        self.cards = []
    
    def shuffle(self):
        '''
        Function:   shuffle the cards in the deck
        Input:      None
        Output:     None
        '''
        random.shuffle(self.cards)
    
    def get_display(self):
        '''
        Function:   shows what the ui wants to see for the deck
        Input:      None
        Output:     returns an integer for the size of the deck
        '''
        return len(self.cards)
    
    def draw(self, hand):
        '''
        Function:   Draws a card and adds it to the hand
        Input:      Hand is a class that represents the players hand
        Output:     None
        '''
        temp_card = self.cards[0]
        del self.cards[0]
        hand.add_card(hand)
        