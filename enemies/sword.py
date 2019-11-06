import pygame
import os
from .enemy import Enemy

imgs = {}
for i in range(20):
   image = pygame.image.load(os.path.join('assets', 'enemies', 'sword', 'walk', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['sword1walkright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['sword1walkleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.image.load(os.path.join('assets', 'enemies', 'sword', 'attack', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['sword1attackright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['sword1attackleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.image.load(os.path.join('assets', 'enemies', 'sword', 'die', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['sword1dieright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['sword1dieleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))


class Sword(Enemy):
   def __init__(self, path):
      super().__init__(path)
      self.name = 'sword'
      self.speed = 0.0
      self.all_images = imgs
      self.enemy_directions = 2
      self.total_animations = 19
      self.health = 2.5
