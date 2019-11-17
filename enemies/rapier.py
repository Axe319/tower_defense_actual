import pygame
import os
from .enemy import Enemy

imgs = {}
for i in range(20):
   image = pygame.image.load(os.path.join('assets', 'enemies', 'rapier', 'walk', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['rapier1walkright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['rapier1walkleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.image.load(os.path.join('assets', 'enemies', 'rapier', 'attack', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['rapier1attackright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['rapier1attackleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.image.load(os.path.join('assets', 'enemies', 'rapier', 'die', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['rapier1dieright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['rapier1dieleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))


class Rapier(Enemy):
   def __init__(self, path):
      super().__init__(path)
      self.name = 'rapier'
      self.speed = 0.0
      self.all_images = imgs
      self.enemy_directions = 2
      self.total_animations = 19
      self.health = 3
      self.reward = 8
