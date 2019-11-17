import pygame
import os
from .enemy import Enemy

imgs = {}
for i in range(20):
   image = pygame.image.load(os.path.join('assets', 'enemies', 'jarhead', 'walk', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['jarhead1walkright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['jarhead1walkleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.image.load(os.path.join('assets', 'enemies', 'jarhead', 'attack', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['jarhead1attackright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['jarhead1attackleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.image.load(os.path.join('assets', 'enemies', 'jarhead', 'die', 'right_' + str(i).rjust(2, '0') + '.png'))
   imgs['jarhead1dieright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
   image = pygame.transform.flip(image, True, False)
   imgs['jarhead1dieleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))


class Jarhead(Enemy):
   def __init__(self, path):
      super().__init__(path)
      self.name = 'jarhead'
      self.speed = 0.0
      self.all_images = imgs
      self.enemy_directions = 2
      self.total_animations = 19
      self.health = 1.5
      self.reward = 4
