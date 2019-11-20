import pygame
import os
from towers.wood import Wood
from towers.steel import Steel
from towers.fire import Fire

imgs = {}
image = pygame.image.load(os.path.join('assets', 'general', 'table.png'))
imgs['table'] = pygame.transform.scale(image, (500, 250))
imgs['pricetag'] = pygame.transform.scale(image, (100, 50))
image = pygame.image.load(os.path.join('assets', 'general', 'rope.png'))
imgs['rope'] = pygame.transform.scale(image, (16, 150))
image = pygame.image.load(os.path.join('assets', 'general', 'shop.png'))
imgs['shop'] = pygame.transform.scale(image, (125, 64))
image = pygame.image.load(os.path.join('assets', 'general', 'close.png'))
imgs['close'] = pygame.transform.scale(image, (32, 32))
image = pygame.image.load(os.path.join('assets', 'general', 'background.png'))
imgs['bg'] = pygame.transform.scale(image, (100, 175))
image = pygame.image.load(os.path.join('assets', 'general', 'star.png'))
imgs['star'] = pygame.transform.scale(image, (26, 26))

class Shop:
   def __init__(self):
      self.images = imgs
      self.opened = False
      self.height = 250
      self.width = 500
      self.shop_width = 0
      self.window_width = 0
      self.window_height = 0
      self.wood_price = '125'
      self.steel_price = '200'
      self.fire_price = '325'
      self.money_font = pygame.font.SysFont('comicsans', 50)

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
         window.blit(self.images['rope'], ((window_width / 2) - (self.width / 2) + 60, 0))
         window.blit(self.images['rope'], ((window_width / 2) + (self.width / 2) - 60 - 16, 0))
         window.blit(self.images['bg'], ((window_width / 2) - (self.width / 2) + 50,  (self.height / 2) + 50))
         window.blit(self.images['bg'], ((window_width / 2) - 50,  (self.height / 2) + 50))
         window.blit(self.images['bg'], ((window_width / 2) + (self.width / 2) - 150, (self.height / 2) + 50))

         window.blit(self.images['shop'], ((window_width / 2) - (self.shop_width / 2), (self.height / 2) - 10))
         window.blit(self.images['close'], ((window_width / 2) + (self.width / 2) - 32, (self.height / 2) - 10))

         window.blit(self.images['pricetag'], ((window_width / 2) - (self.width / 2) + 50, self.height + (self.height / 2) - 50))
         window.blit(self.images['pricetag'], ((window_width / 2) - 50, self.height + (self.height / 2) - 50))
         window.blit(self.images['pricetag'], ((window_width / 2) + (self.width / 2) - 150, self.height + (self.height / 2) - 50))

         window.blit(self.images['star'], ((window_width / 2) - (self.width / 2) + 55, self.height + (self.height / 2) - 42))
         wood_price = self.money_font.render(self.wood_price, 1, (255, 200, 0))
         window.blit(wood_price, ((window_width / 2) - (self.width / 2) + 81, self.height + (self.height / 2) - 42))

         window.blit(self.images['star'], ((window_width / 2) - 45, self.height + (self.height / 2) - 42))
         steel_price = self.money_font.render(self.steel_price, 1, (255, 200, 0))
         window.blit(steel_price, ((window_width / 2) - 19, self.height + (self.height / 2) - 42))

         window.blit(self.images['star'], ((window_width / 2) + (self.width / 2) - 145, self.height + (self.height / 2) - 42))
         fire_price = self.money_font.render(self.fire_price, 1, (255, 200, 0))
         window.blit(fire_price, ((window_width / 2) + (self.width / 2) - 119, self.height + (self.height / 2) - 42))
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
                  towers.append(Steel())
                  towers.append(Fire())

      return collided
