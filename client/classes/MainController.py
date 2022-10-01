import pygame

from GlobalVariables import *
from classes import Card

class MainController:
    '''
    Main Controller for the ui, renders all the sprites via pygame
    '''
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.card = Card()
    
    def handle_event(self):
        '''
        Function:   called every itteration to handle things that happen to the screen
        Input:      None
        Output:     Boolean True or False depending on whether to continue loading the game
        '''
        self.screen.fill(COLORS["azure"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONUP:
                self.card.click_and_check_if_clicked(pygame.mouse.get_pos())
        self.screen.blit(self.card.sprite, self.card.dest)
        pygame.display.flip()
        return True