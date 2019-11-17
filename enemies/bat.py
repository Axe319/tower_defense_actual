import pygame
import os
from .enemy import Enemy

imgs = {}
for i in range(25):
   for level in range(2):
      image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level + 1), 'walk', 'downleft_' + str(i).rjust(2, '0') + '.png'))
      imgs['bat' + str(level + 1) + 'walkdownleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
      image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level + 1), 'walk', 'downright_' + str(i).rjust(2, '0') + '.png'))
      imgs['bat' + str(level + 1) + 'walkdownright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
      image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level + 1), 'walk', 'upleft_' + str(i).rjust(2, '0') + '.png'))
      imgs['bat' + str(level + 1) + 'walkupleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
      image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level + 1), 'walk', 'upright_' + str(i).rjust(2, '0') + '.png'))
      imgs['bat' + str(level + 1) + 'walkupright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
      image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level + 1), 'attack', 'downleft_' + str(i).rjust(2, '0') + '.png'))
      imgs['bat' + str(level + 1) + 'attackdownleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
      image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level + 1), 'attack', 'downright_' + str(i).rjust(2, '0') + '.png'))
      imgs['bat' + str(level + 1) + 'attackdownright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
      image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level + 1), 'attack', 'upleft_' + str(i).rjust(2, '0') + '.png'))
      imgs['bat' + str(level + 1) + 'attackupleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
      image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level + 1), 'attack', 'upright_' + str(i).rjust(2, '0') + '.png'))
      imgs['bat' + str(level + 1) + 'attackupright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
      if i < 24:
         image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level + 1), 'die', 'downleft_' + str(i).rjust(2, '0') + '.png'))
         imgs['bat' + str(level + 1) + 'diedownleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
         image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level + 1), 'die', 'downright_' + str(i).rjust(2, '0') + '.png'))
         imgs['bat' + str(level + 1) + 'diedownright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
         image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level + 1), 'die', 'upleft_' + str(i).rjust(2, '0') + '.png'))
         imgs['bat' + str(level + 1) + 'dieupleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
         image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level + 1), 'die', 'upright_' + str(i).rjust(2, '0') + '.png'))
         imgs['bat' + str(level + 1) + 'dieupright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))

class Bat(Enemy):
   def __init__(self, path):
      super().__init__(path)
      self.name = 'bat'
      self.speed = 0.0
      self.all_images = imgs
      self.enemy_directions = 4
      self.total_animations = 24
      self.health = 3.5
      self.reward = 10
