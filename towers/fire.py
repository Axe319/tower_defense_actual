import pygame
import os
from .towers import Towers

imgs = {}
for i in range(1, 4):
    image = pygame.image.load(os.path.join('assets', 'towers', 'fire', f'base{i}.png'))
    imgs[f'base{i}'] = pygame.transform.scale(image, (64, 96))
    image = pygame.image.load(os.path.join('assets', 'towers', 'fire', f'back{i}.png'))
    imgs[f'back{i}'] = pygame.transform.scale(image, (58, 16))
    image = pygame.image.load(os.path.join('assets', 'towers', 'fire', f'front{i}.png'))
    imgs[f'front{i}'] = pygame.transform.scale(image, (58, 16))

image = pygame.image.load(os.path.join('assets', 'towers', 'fire', 'ammo.png'))
imgs['ammo'] = pygame.transform.scale(image, (24, 24))
for i in range(1, 6):
    image = pygame.image.load(os.path.join('assets', 'towers', 'fire', f'explode{i}.png'))
    imgs[f'explode{i}'] = pygame.transform.scale(image, (24, 24))


class Fire(Towers):
    def __init__(self):
        self.x = 850
        self.y = 275
        self.range = 200
        self.level = 1
        self.all_images = imgs
        self.fire_speed = 2.4
        self.damage = 1.25
        self.price = 325
        super().__init__()

    def move_with_base(self):
        """
        moves the front, back and ammo images with the base
        will need to be called when moving the tower to ensure the
        pieces stay together
        :return: None
        """
        self.back = self.base[0], self.base[1] + (.4 * self.height), self.all_images[f'back{self.level}']
        self.front = self.back[0], self.back[1] + (self.height / 6) - 10, self.all_images[f'front{self.level}']
        self.ammo = self.back[0] + (self.width * .25), self.back[1], self.all_images['ammo']

        self.fire_animation_back = []
        self.fire_animation_ammo = []
        self.fire_animation_front = []

        position = self.back[1]
        ammo_y = self.ammo[1]
        ammo_x = self.base[0] + (self.width * .25)
        while position > self.base[1]:
            position -= self.fire_speed
            ammo_y -= self.fire_speed
            self.fire_animation_back.append((self.base[0], position, self.all_images[f'back{self.level}']))
            self.fire_animation_ammo.append((ammo_x, ammo_y, self.all_images['ammo']))
            self.fire_animation_front.append((self.base[0], position + (self.height / 6) - 4, self.all_images[f'front{self.level}']))

        if self.target is not None:
            self.ammo_path = self.get_path((ammo_x, ammo_y), (self.target_x - 12, self.target_y))

            self.ammo_element = 0

            while position < self.back[1]:
                position += self.fire_speed
                ammo_x = self.ammo_path[self.ammo_element][0]
                ammo_y = self.ammo_path[self.ammo_element][1]
                self.ammo_element += 1
                self.fire_animation_back.append((self.base[0], position, self.all_images[f'back{self.level}']))
                self.fire_animation_ammo.append((ammo_x, ammo_y, self.all_images['ammo']))
                self.fire_animation_front.append((self.base[0], position + (self.height / 6) - 4, self.all_images[f'front{self.level}']))
            self.ammo_element -= 1

        self.current_x = ammo_x
        self.current_y = ammo_y
