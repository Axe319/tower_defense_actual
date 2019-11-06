import pygame
import os
from towers.wood import Wood

imgs = {}
image = pygame.image.load(os.path.join('assets', 'general', 'table.png'))
imgs['table'] = pygame.transform.scale(image, (500, 250))
image = pygame.image.load(os.path.join('assets', 'general', 'rope.png'))
imgs['rope'] = pygame.transform.scale(image, (16, 150))
image = pygame.image.load(os.path.join('assets', 'general', 'shop.png'))
imgs['shop'] = pygame.transform.scale(image, (125, 64))
image = pygame.image.load(os.path.join('assets', 'general', 'close.png'))
imgs['close'] = pygame.transform.scale(image, (32, 32))


class Shop:
   def __init__(self):
      self.images = imgs
      self.opened = False
      self.height = 250
      self.width = 500
      self.shop_width = 0
      self.window_width = 0
      self.window_height = 0

   def open(self):
      self.opened = True

   def close(self):
      self.opened = False

   def display(self, window, window_height, window_width):
      self.shop_width = self.width / 4
      self.window_width = window_width
      self.window_height = window_height
      if self.opened:
         window.blit(self.images['table'], ((window_width / 2) - (self.width / 2), self.height / 2))
         window.blit(self.images['shop'], ((window_width / 2) - (self.shop_width / 2), (self.height / 2) - 10))
         window.blit(self.images['rope'], ((window_width / 2) - (self.width / 2) + 60, 0))
         window.blit(self.images['rope'], ((window_width / 2) + (self.width / 2) - 60 - 16, 0))
         window.blit(self.images['close'], ((window_width / 2) + (self.width / 2) - 32, (self.height / 2) - 10))
      else:
         window.blit(self.images['shop'], ((window_width / 2) - (self.shop_width / 2), 0))

   def collide(self, position, towers):
      """
      returns true if position collides with shop open close
      :param position: tuple
      :param towers: list of tower objects
      :return: bool
      """
      collided = False
      shop_start = (self.window_width / 2) - (self.shop_width / 2)
      close_start = (self.window_width / 2) + (self.width / 2) - 32, (self.height / 2) - 10

      if self.opened: # check if close hit
         if position[0] > close_start[0]:
            if position[0] < close_start[0] + 32:
               if position[1] > close_start[1]:
                  if position[1] < close_start[1] + 32:
                     collided = True

      else: # check if shop hit
         if position[0] > shop_start:
            if position[0] < shop_start + self.shop_width:
               if position[1] < self.height:
                  collided = True
                  towers.append(Wood())

      return collided
