#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.entity import Entity

class Background(Entity):

    def __init__(self, name: str, position: tuple): # garante que o nome seja salvo no Entity
        super().__init__(name, position)
        self.name = name   # <-- reforço para evitar que fique None

    def move(self): # usa a velocidade correta do dicionário
        speed = ENTITY_SPEED.get(self.name, 0)  # se não achar, usa 0
        self.rect.centerx -= speed

        # reposiciona quando sai da tela
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH



# from code.Const import WIN_WIDTH, ENTITY_SPEED
# from code.entity import Entity
#
# class Background(Entity):
#
#     def __init__(self, name: str, position: tuple):
#         super().__init__(name, position)
#
#     def move(self, ):
#         self.rect.centerx -= ENTITY_SPEED[self.name]
#         if self.rect.right <= 0:
#             self.rect.left = WIN_WIDTH
