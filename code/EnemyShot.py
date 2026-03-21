#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED
from code.entity import Entity

class EnemyShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = name

    def move(self):
        # Tiros inimigos diminuem o X para ir da direita para a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name]