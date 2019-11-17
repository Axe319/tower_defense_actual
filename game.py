# todo

import pygame
import os
from menus.shop import Shop
from maps.map import Map
from enemies.bat import Bat
from enemies.jarhead import Jarhead
from enemies.dagger import Dagger
from enemies.fork import Fork
from enemies.sword import Sword
from enemies.rapier import Rapier
from towers.wood import Wood
from random import randint, uniform
import time


class Game:
   def __init__(self):
      self.width = 1400
      self.height  = 750
      pygame.init()
      self.window = pygame.display.set_mode((self.width, self.height))

      self.map = Map(self.width, self.height)
      self.map_choice = 1
      self.paths = self.map.map_paths[self.map_choice]
      self.bg = self.map.maps[self.map_choice]
      self.shop = Shop()
      self.clock = pygame.time.Clock()
      self.timer_font = pygame.font.SysFont('comicsans', 65)
      self.money_font = pygame.font.SysFont('comicsans', 65)

      self.towers = []
      self.enemies = [] # enemy instances this wave

      self.wave_active = True
      self.last_enemy_gen = time.time() + 10 # give 10 seconds to prep
      self.enemies_this_wave = 0 # enemies we've generated this wave
      self.enemies_killed_this_wave = 0 # enemies we've killed this wave
      self.wave_size = 4 # current wave size
      self.wave_speed = 0.8 # current wave speed
      self.max_level = 0 # max level of enemy to gen
      self.gen_interval = 1.5 # the current interval to gen enemies
      self.min_gen_interval = 1.5 # minimum interval to gen enemies
      self.all_enemies_count = 6 # max number of classes
      self.money = 150
      self.clicks = []

   def run(self):
      """
      Main Game Run Loop
      :return: None
      """
      run = True

      while run:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
               # self.clicks.append(pygame.mouse.get_pos())
               if self.shop.collide(pygame.mouse.get_pos(), self.towers):
                  self.shop.opened = not self.shop.opened

            elif event.type == pygame.MOUSEBUTTONUP:
               for tower in self.towers:
                  if tower.moving:
                     # add more logic later to make sure not colliding and enough moneys is had
                     tower.moving = False
                     if tower.price <= self.money:
                        tower.bought = True
                        self.money -= tower.price

            if pygame.mouse.get_pressed()[0]:
               mouse_position = pygame.mouse.get_pos()
               tower_element = self.get_tower_element(mouse_position)
               if tower_element is not None:
                  self.towers[tower_element].x = mouse_position[0]
                  self.towers[tower_element].y = mouse_position[1]
                  self.towers[tower_element].base = self.towers[tower_element].x - (self.towers[tower_element].width / 2), self.towers[tower_element].y - (self.towers[tower_element].height / 2), self.towers[tower_element].all_images['base' + str(self.towers[tower_element].level)]
                  self.towers[tower_element].move_with_base()
                  self.towers[tower_element].moving = True
                  self.shop.opened = False

         self.draw()

      # print(self.clicks)
      pygame.quit()

   def draw(self):
      """
      draw the game
      sorts drawable elements by x value to ensure background
      items don't get superimposed on foreground items
      :return: None
      """
      drawables = []
      to_del = []
      count_down = int(round(self.gen_interval - (time.time() - self.last_enemy_gen)))
      text = self.timer_font.render(str(count_down), 1, (255, 0, 0))
      money = self.money_font.render(str(self.money), 1, (255, 200, 0))

      self.window.blit(self.bg, (0, 0))

      if self.wave_active:
         self.get_wave()
      elif self.wave_size < self.enemies_killed_this_wave:
         self.init_new_wave()

      for enemy in self.enemies:
         if (enemy.death_animation_count == 24 and enemy.enemy_directions == 4) or (enemy.death_animation_count == 20 and enemy.enemy_directions == 2):
            to_del.append(enemy)
         elif enemy.x < 10 or enemy.health <= 0:
            drawables.append(enemy.die())
         else:
            drawables.append(enemy.walk())

      # should sort enemies here to make sure the don't superimpose on one another
      # todo
      drawables.sort(key=lambda tup: tup[1])

      for item in to_del:
         self.money += item.reward
         self.enemies.remove(item)
         self.enemies_killed_this_wave += 1

      for tower in self.towers:
         if tower.firing or self.get_closest_enemy(tower):
            drawables.append(tower.fire_animation_back[tower.firing_animation_count])
            drawables.append(tower.base)
            drawables.append(tower.fire_animation_ammo[tower.firing_animation_count])
            drawables.append(tower.fire_animation_front[tower.firing_animation_count])
            tower.fire()
         elif tower.bought:
            drawables.append(tower.back)
            drawables.append(tower.base)
            drawables.append(tower.ammo)
            drawables.append(tower.front)

      for drawable in drawables:
         self.window.blit(drawable[2], drawable[:2])

      self.shop.display(self.window, self.height, self.width)

      # draw the towers in the shop
      for tower in self.towers:
         if not tower.bought:
            self.window.blit(tower.back[2], tower.back[:2])
            self.window.blit(tower.base[2], tower.base[:2])
            self.window.blit(tower.ammo[2], tower.ammo[:2])
            self.window.blit(tower.front[2], tower.front[:2])

      if count_down > 0 and self.enemies_this_wave == 0:
         self.window.blit(text, (13, 13))
      self.window.blit(self.shop.images['star'], (13, self.height - 64))
      self.window.blit(money, (39, self.height - 64))

      self.del_unbought_towers()

      pygame.display.update()
      self.clock.tick(60)

   def get_wave(self):
      """
      generates enemies for the current active wave until the wave is completed
      :return: None
      """
      if self.enemies_this_wave > self.wave_size:
         self.wave_active = False
         self.enemies_this_wave = 0
      elif time.time() - self.last_enemy_gen > self.gen_interval:
         self.last_enemy_gen = time.time()

         num_of_paths = len(self.paths) - 1
         path = self.paths[randint(0, num_of_paths)]

         # regen all enemies and pick the correct one
         enemy_classes = [(Dagger(path), 1),
            (Jarhead(path), 1),
            (Fork(path), 1),
            (Sword(path), 1),
            (Rapier(path), 1),
            (Bat(path), 1),
            (Bat(path), 2)
            ]
         enemy_class, enemy_level = enemy_classes[randint(0, self.max_level)]
         self.enemies.append(enemy_class)

         # to avoid index oout of range
         # when we kill an enemy while wave is still genning
         current_enemy = len(self.enemies) - 1

         self.enemies[current_enemy].speed = self.wave_speed

         # increment health and level if higher
         if enemy_level > self.enemies[current_enemy].level:
            self.enemies[current_enemy].health += (enemy_level - self.enemies[current_enemy].level) * .5
            self.enemies[current_enemy].level = enemy_level

         self.enemies_this_wave += 1
         self.gen_interval = uniform(self.min_gen_interval, 1.5)

   def init_new_wave(self):
      """
      Initiates the next active wave
      Increasing the wave size and enemy speed
      :return: None
      """
      self.wave_size += 2
      self.wave_speed += .05
      if self.max_level < self.all_enemies_count:
         self.max_level += 1
      if self.min_gen_interval > .5:
         self.min_gen_interval -= .1
      self.enemies_killed_this_wave = 0
      self.wave_active = True
      self.last_enemy_gen = time.time() + 10 # give 10 seconds to prep
      self.gen_interval = uniform(self.min_gen_interval, 1.5)

   def get_closest_enemy(self, tower):
      """
      return true if enemy targeted
      :param tower:
      :return: bool
      """
      in_range = False
      for enemy in self.enemies:
         if tower.in_range(enemy):
            in_range = True
            break

      return in_range

   def get_tower_element(self, mouse_position):
      """
      check if the mouse position is over a tower
      retur the index of said tower if it is
      :param mouse_position:
      :return: int or None
      """
      for index, tower in enumerate(self.towers):
         if not tower.bought:
            if tower.price <= self.money:
               if mouse_position[0] > tower.x - (tower.width / 2):
                  if mouse_position[0] < tower.x + (tower.width / 2):
                     if mouse_position[1] > tower.y - (tower.height / 2):
                        if mouse_position[1] < tower.y + (tower.height / 2):
                           return index

   def del_unbought_towers(self):
      to_del = []

      if not self.shop.opened:
         for tower in self.towers:
            if not tower.bought and not tower.moving:
               to_del.append(tower)

         for item in to_del:
            self.towers.remove(item)
