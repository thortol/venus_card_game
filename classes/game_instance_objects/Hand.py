class Hand:
    '''
    Hand is the cards in the hand of the player
    '''
    def __init__(self):
        self.hand = []
    
    def add_card(self, card):
        '''
        Function:   Adds a card to hand
        Input:      card is a card data type
        Output:     None
        '''
        self.hand.append(card)

    def get_display(self):
        '''
        Function:   shows what the ui wants to see for the hand
        Input:      None
        Output:     returns a list for the hand
        '''
        return self.hand # incorrect need to get id etc