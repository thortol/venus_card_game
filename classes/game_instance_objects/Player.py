from classes import GameObject

class Player(GameObject):
    '''
    Player contains the health and mana of the player
    '''
    def __init__(self):
        pass

    def get_display(self):
        '''
        Function:   shows what the ui wants to see for the player
        Input:      None
        Output:     returns an integer for the health of the player
        '''
        return self.get_health()