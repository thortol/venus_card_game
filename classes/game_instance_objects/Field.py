class Field:
    '''
    Field is the cards is the field of the player
    '''
    def __init__(self):
        self.field = []
    
    def get_display(self):
        '''
        Function:   shows what the ui wants to see for the field
        Input:      None
        Output:     returns a list for the field
        '''
        return self.field # incorrect need to get id etc