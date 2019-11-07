import pygame
import os
from .enemy import Enemy

imgs = {}
for i in range(20):
   image = pygame.image.load(os.path.join('assets', 'enemies', 'fork', 'walk', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['fork1walkright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['fork1walkleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.image.load(os.path.join('assets', 'enemies', 'fork', 'attack', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['fork1attackright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['fork1attackleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.image.load(os.path.join('assets', 'enemies', 'fork', 'die', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['fork1dieright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['fork1dieleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))


class Fork(Enemy):
   def __init__(self, path):
      super().__init__(path)
      self.name = 'fork'
      self.speed = 0.0
      self.all_images = imgs
      self.enemy_directions = 2
      self.total_animations = 19
      self.health = 2
      self.reward = 10
