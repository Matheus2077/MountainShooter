#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = name  # Garante que o nome seja salvo para buscar a velocidade

    def move(self):
        # Busca a velocidade no dicionário
        speed = ENTITY_SPEED.get(self.name, 0)

        # Move para a esquerda
        self.rect.centerx -= speed

        # Se sair totalmente da tela pela esquerda, volta para a direita
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH