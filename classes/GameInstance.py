from classes import Deck
from classes import Field
from classes import Hand
from classes import Player

class GameInstance:
    '''
    Contains all the info for 1 round of the game to run example field deck
    '''
    def __init__(self):
        self.decks = [Deck(), Deck()]
        self.fields = [Field(), Field()]
        self.hands = [Hand(), Hand()]
        self.players = [Player(), Player()]
        self.cur_player = 0
    
    def show_info(self, id):
        '''
        Function:   Returns all the info to be shown in the client
        Input:      id is the index of the player
        Output:     returns a dictionary of the game field
        '''
        info = {}
        info["deck"] = self.decks[id].get_display()
        info["field"] = self.fields[id].get_display()
        info["hand"] = self.hands[id].get_display()
        info["player"] = self.players[id].get_display()

    
    def get_other_player(self, id):
        '''
        Function:   Gets the id of the other player
        Input:      id is the index of the player
        Output:     returns an integer of the id of the other player
        '''
        return (id + 1) % 2
    

