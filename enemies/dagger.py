import pygame
import os
from .enemy import Enemy

imgs = {}
for i in range(20):
   image = pygame.image.load(os.path.join('assets', 'enemies', 'dagger', 'walk', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['dagger1walkright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['dagger1walkleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.image.load(os.path.join('assets', 'enemies', 'dagger', 'attack', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['dagger1attackright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['dagger1attackleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.image.load(os.path.join('assets', 'enemies', 'dagger', 'die', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['dagger1dieright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['dagger1dieleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))


class Dagger(Enemy):
   def __init__(self, path):
      super().__init__(path)
      self.name = 'dagger'
      self.speed = 0.0
      self.all_images = imgs
      self.enemy_directions = 2
      self.total_animations = 19
      self.health = 1
      self.reward = 5
