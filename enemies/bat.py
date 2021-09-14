import pygame
import os
from .enemy import Enemy

imgs = {}
for i in range(25):
    for level in (1, 2):
        image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level), 'walk', 'downleft_' + str(i).rjust(2, '0') + '.png'))
        imgs[f'bat{level}walkdownleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
        image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level), 'walk', 'downright_' + str(i).rjust(2, '0') + '.png'))
        imgs[f'bat{level}walkdownright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
        image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level), 'walk', 'upleft_' + str(i).rjust(2, '0') + '.png'))
        imgs[f'bat{level}walkupleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
        image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level), 'walk', 'upright_' + str(i).rjust(2, '0') + '.png'))
        imgs[f'bat{level}walkupright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
        image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level), 'attack', 'downleft_' + str(i).rjust(2, '0') + '.png'))
        imgs[f'bat{level}attackdownleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
        image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level), 'attack', 'downright_' + str(i).rjust(2, '0') + '.png'))
        imgs[f'bat{level}attackdownright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
        image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level), 'attack', 'upleft_' + str(i).rjust(2, '0') + '.png'))
        imgs[f'bat{level}attackupleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
        image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level), 'attack', 'upright_' + str(i).rjust(2, '0') + '.png'))
        imgs[f'bat{level}attackupright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
        if i < 24:
            image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level), 'die', 'downleft_' + str(i).rjust(2, '0') + '.png'))
            imgs[f'bat{level}diedownleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
            image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level), 'die', 'downright_' + str(i).rjust(2, '0') + '.png'))
            imgs[f'bat{level}diedownright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
            image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level), 'die', 'upleft_' + str(i).rjust(2, '0') + '.png'))
            imgs[f'bat{level}dieupleft_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))
            image = pygame.image.load(os.path.join('assets', 'enemies', 'bat', 'level', str(level), 'die', 'upright_' + str(i).rjust(2, '0') + '.png'))
            imgs[f'bat{level}dieupright_' + str(i).rjust(2, '0') + '.png'] = pygame.transform.scale(image, (64, 64))


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
