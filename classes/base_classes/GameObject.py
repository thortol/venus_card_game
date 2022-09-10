class GameObject:
    '''
    GameObject is a class to be inherited by all game objects that exist on the board
    '''
    def __init__(self):
        self.health = 0
    
    def get_health(self):
        '''
        Function:   Gets the health of the gameObject
        Input:      None
        Output:     returns an integer of the current health
        '''
        return self.health
    
    def deal_damage(self, damage):
        '''
        Function:   Deals the damage to the GameObject
        Input:      damage is an integer of the damage to be taken
        Output:     None
        '''
        self.health -= damage
    
    def is_alive(self):
        '''
        Function:   Checks if the gameObject is alive health less than equal to 0
        Input:      None
        Output:     Boolean True or False
        '''
        if self.health <= 0:
            return True
        return False