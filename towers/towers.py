import math
import os
import pygame
from typing import List, Tuple


class Towers:
   """
   Each derivative class will need a move_with_base method
   """
   def __init__(self):
      self.firing = False
      self.bought = False
      self.moving = False
      self.target = None
      self.height = 96
      self.width = 64
      # ammo positions
      self.current_x = 0
      self.current_y = 0
      #predicted enemy position
      self.target_x = 0
      self.target_y = 0
      self.base = self.x - (self.width / 2), self.y - (self.height / 2), self.all_images['base' + str(self.level)]
      self.back = ()
      self.front = ()
      self.ammo = ()
      self.ammo_path = []
      self.ammo_element = 0
      self.firing_animation_count = 0
      self.fire_movements = 0
      self.enemy_movements = 0
      self.fire_animation_back = []
      self.fire_animation_ammo = []
      self.fire_animation_front = []
      self.move_with_base()

   def in_range(self, target):
      """
      checks if a target is in range or not
      if in range sets self.firing to true and
      generates the fir animation
      :param target:
      :return: bool
      """
      # default to not in range
      in_range = False
      if not self.firing and self.bought and target.health > 0:
         distance = math.sqrt((self.y - (self.height / 2) - target.y) ** 2 + (self.x - (self.width / 2) - target.x) ** 2)
         if distance <= self.range:
            in_range = True
            self.target = target
            self.firing = True
            self.get_fire_animation()

      return in_range

   def fire(self):
      """
      fires on a given enemy
      once the fire animation is complete,
      dedusts the the tower damage from enemy health
      :return: None
      """
      if len(self.fire_animation_back) > self.firing_animation_count + 1:
         self.firing_animation_count += 1
      else:
         # hit
         self.target.health -= self.damage
         self.firing = False
         self.firing_animation_count = 0

   def get_fire_animation(self):
      """
      get the fire animation for the target enemy
      starts out assuming 90 enemy movements until collision.
      counts the number of fire movements and then adjusts based on how far off the two are.
      if within 5 movements of each other, accepts the tolerance and assigns the the fire paths
      :return: None
      """
      self.fire_movements = 0
      self.enemy_movements = 90
      within_tolerance = False

      while not within_tolerance:
         self.predict_enemy_movement()

         self.move_with_base()
         self.fire_movements = len(self.fire_animation_ammo)

         hit_target = False
         for path in self.ammo_path[self.ammo_element:]:
            self.fire_movements += 1
            next_coordinate = path
            self.fire_animation_back.append(self.back)
            self.fire_animation_ammo.append((next_coordinate[0], next_coordinate[1], self.all_images['ammo']))
            self.fire_animation_front.append(self.front)

         self.current_x, self.current_y = next_coordinate

         if self.fire_movements > self.enemy_movements + 5:
            self.enemy_movements += 4
         elif self.fire_movements < self.enemy_movements - 5:
            self.enemy_movements -= 4
         else:
            within_tolerance = True

      # explosion animation
      for i in range(1, 6):
         for x in range(3):
            self.fire_animation_back.append(self.back)
            self.fire_animation_ammo.append((self.target_x - 12, self.target_y, self.all_images['explode' + str(i)]))
            self.fire_animation_front.append(self.front)


   def upgrade(self):
      pass

   def predict_enemy_movement(self):
      """
      predict where the enemy will be a certain amount of steps ahead
      assumes self.enemy_movements for the number of moves the enemy will take
      :return: None
      """
      # set some local variables
      current_tuple = self.target.current_tuple
      x = self.target.x
      y = self.target.y

      # how many moves ahead were going
      for i in range(self.enemy_movements):
         x1, y1 = self.target.path[current_tuple]

         if current_tuple + 1 >= len(self.target.path):
            x2, y2 = (1, 280)
         else:
            x2, y2 = self.target.path[current_tuple + 1]

         x1 -= (self.target.width / 2)
         x2 -= (self.target.width / 2)
         y1 -= (self.target.height / 2)
         y2 -= (self.target.height / 2)

         x, y = self.get_next_coordinate((x, y), (x2, y2), self.target.speed)

         if x2 >= x1: # moving right
            if y2 >= y1: # moving down
               if x >= x2 and y2 >= y:
                  current_tuple += 1
               elif x >= x2 and y >= y2:
                  current_tuple += 1
            else: #moving up
               if x >= x2 and y <= y2:
                  current_tuple += 1
               elif x >= x2 and y >= y2:
                  current_tuple += 1
         else: # moving left
            if y2 >= y1:  # moving down
               if x <= x2 and y >= y2:
                  current_tuple += 1
               else:
                  if x <= x2 and y <= y2:
                     current_tuple += 1
            else: #moving up
               if x <= x2 and y <= y2:
                  current_tuple += 1
               elif x <= x2 and y >= y2:
                  current_tuple += 1

      self.target_x = x + (self.target.width / 2)
      self.target_y = y + (self.target.height / 2)

   @staticmethod
   def get_next_coordinate(point_a: Tuple[float, float], point_b: Tuple[float, float], movement: float) -> Tuple[float, float]:
      """
      get the next coordinates from point_a to point_b a traveling a distance of movement
      :param point_a:
      :param point_b:
      :param movement:
      :return: Tuple
      """
      distance = math.sqrt((point_a[1] - point_b[1]) ** 2 + (point_a[0] - point_b[0]) ** 2)
      # slope = (point_a[1] - point_b[1]) / (point_a[0] - point_b[0])
      ratio_of_distance = movement / distance

      return ((1 - ratio_of_distance) * point_a[0] + ratio_of_distance * point_b[0]), ((1 - ratio_of_distance) * point_a[1] + ratio_of_distance * point_b[1])

   @staticmethod
   def get_path(start_pos: Tuple[int, int], target: Tuple[int, int], time_interval=0.2, time_to_reach=8.0, gravity=-9.8) -> List[Tuple[int, int]]:
      current_time = 0
      path = []

      x_distance = target[0] - start_pos[0]
      y_distance = start_pos[1] - target[1]

      x_velocity = x_distance / time_to_reach
      y_velocity = (y_distance - ((gravity * time_to_reach ** 2) / 2)) / time_to_reach

      while current_time < time_to_reach:
         current_time += time_interval

         x_increment = x_velocity * current_time
         y_increment = (y_velocity * current_time) + ((gravity * current_time ** 2) / 2)

         path.append((round(start_pos[0] + x_increment), round(start_pos[1] - y_increment)))

      return path
