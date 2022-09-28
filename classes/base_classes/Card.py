from classes import GameObject

class Card(GameObject):
    '''
    Cards are gameObjects that exist on the board, they handle the logic for their own skills
    '''
    def __init__(self):
        super().__init__()
    
    def attack(self, card):
        '''
        Function:   deals its dmg to a card while taking that cards dmg
        Input:      card to deal damage to
        Output:     None
        '''
        enemy_dmg = card.get_health()
        card.deal_damage(self.get_health())
        self.deal_damage(enemy_dmg)