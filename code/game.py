#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


#def mostrar_placar(window):
 #   pass


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            # código original do Prof.
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:

                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # close window
                quit()  # end pygame
            else:
                pass



            # if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
            #     level = Level(self.window, name='Level1', game_mode=menu_return)
            #     level.run()
            # elif menu_return == MENU_OPTION[4]:
            #     pygame.quit()
            #     quit()
            # elif menu_return == MENU_OPTION[3]:
            #     mostrar_placar(self.window)




            # Check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  # CloseWindow
            #         quit()  # end game