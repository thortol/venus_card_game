import pygame
from GlobalVariables import *

class Card():
    '''
    Contains the details for 1 card to show the user
    '''
    def __init__(self):
        self.sprite = pygame.image.load(r"C:\Users\Scrub\Desktop\coding\venus\client\sprites\1.png")
        self.is_clicked = False
        self.dest = pygame.Rect((0,0), CARD_SIZE)
    
    def click_and_check_if_clicked(self, mouse):
        '''
        function:   Checks if a sprite is clicked and activates it if it is clicked
        input:      position of mouse (given by pygame)
        output:     boolean true or false depends on whether the sprite is in clicked state or not
        '''
        if self.dest.collidepoint(mouse):
            self.click()
        return self.is_clicked

    def click(self):
        '''
        function:   Activates the card as if it was clicked/unclicked
        input:      None
        output:     None
        '''
        if self.is_clicked:
            self.sprite = pygame.image.load(r"C:\Users\Scrub\Desktop\coding\venus\client\sprites\1.png")
        else:
            pygame.draw.rect(self.sprite, COLORS["red"], [0, 0,  CARD_SIZE[0],  CARD_SIZE[1]], 1)
        self.is_clicked = self.is_clicked == False
    
    def unclick(self):
        '''
        function:   Only unclicks the card
        input:      None
        output:     None
        '''
        self.sprite = pygame.image.load(r"C:\Users\Scrub\Desktop\coding\venus\client\sprites\1.png")
        self.is_clicked = False