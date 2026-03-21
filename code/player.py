#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name] # Garantia extra: salva o nome aqui também

    def move(self):
        pressed_key = pygame.key.get_pressed()

        # Movimento para CIMA
        # Movimento para CIMA
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        # Movimento para BAIXO
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        # Movimento para ESQUERDA (CORRIGIDO)
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        # Movimento para DIREITA
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

    # def shoot(self):
    #     self.shot_delay -= 1
    #     if self.shot_delay == 0:
    #         self.shot_delay = ENTITY_SHOT_DELAY[self.name]
    #         pressed_key = pygame.key.get_pressed()
    #         if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
    #            return  PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
    #     return None
    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0:  # Mudança aqui: verifica se o cooldown acabou
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Reseta o delay APENAS se atirou
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        return None




