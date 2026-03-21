#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY
from code.entity import Entity
from code.EnemyShot import EnemyShot # Vamos criar este arquivo no passo 2

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = name
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0:
            # Reseta o delay
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            # Retorna um tiro inimigo
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.left, self.rect.centery))
        return None