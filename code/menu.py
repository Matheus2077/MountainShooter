#!/usr/bin/python
# -*- coding: utf-8 -*-

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect()

    def run(self, ):
        pass
