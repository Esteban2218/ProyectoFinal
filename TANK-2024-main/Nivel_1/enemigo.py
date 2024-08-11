import pygame
from pygame.sprite import Sprite
import random


class Enemigo(Sprite):
    def __init__(self,dc_game):
        super().__init__()
        self.dc_game= dc_game
        self.screen  = dc_game.screen

        self.image = pygame.image.load('C:/Users/LENOVO/Documents/SOFTWARE/Algoritmos y estructura de Datos/Proyecto finalTK/TANK-2024-main/tanque_enemigo.png')
        self.rect = self.image.get_rect()  
        # Posiciona el enemigo en una posición horizontal aleatoria
        self.rect.x = random.randint(0, self.dc_game.ajustes.anchura - self.rect.width)
        
        # Posiciona el enemigo en la parte superior de la pantalla o en una posición vertical aleatoria
        self.rect.y = -self.rect.height
        self.y = float(self.rect.y)

        self.ajustes = dc_game.ajustes

    def update(self):
        self.rect.y += self.ajustes.velocidadEnemigo
        self.y += self.ajustes.velocidadEnemigo  
        self.rect.y = self.y  
