import math


class Enemy:
    def __init__(self, path):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.death_animation_count = 0
        self.attack_animation_count = 0
        self.path = path
        self.current_tuple = 0
        self.x = self.path[self.current_tuple][0]
        self.y = self.path[self.current_tuple][1]
        self.move_dist = 5
        self.image_direction = ''
        self.level = 1

    def move(self):
        """
        move an enemy along the self.path of coordinates
        returns the direction the enemy is facing and the file extension
        :return: Tuple
        """

        x1, y1 = self.path[self.current_tuple]

        if self.current_tuple + 1 >= len(self.path):
            x2, y2 = (1, 280)
        else:
            x2, y2 = self.path[self.current_tuple + 1]

        x1 -= (self.width / 2)
        x2 -= (self.width / 2)
        y1 -= (self.height / 2)
        y2 -= (self.height / 2)

        if x2 > x1:
            self.image_direction = 'right'
            if self.enemy_directions == 4:
                if y2 > y1:
                    self.image_direction = f'down{self.image_direction}'
                else:
                    self.image_direction = f'up{self.image_direction}'
        else:
            self.image_direction = 'left'
            if self.enemy_directions == 4:
                if y2 > y1:
                    self.image_direction = f'down{self.image_direction}'
                else:
                    self.image_direction = f'up{self.image_direction}'

        image_count = '_' + str(self.animation_count).rjust(2, '0') + '.png'

        self.x, self.y = self.get_next_coordinate((self.x, self.y), (x2, y2), self.speed)

        if x2 >= x1:  # moving right
            if y2 >= y1:  # moving down
                if self.x >= x2 and y2 >= self.y:
                    self.current_tuple += 1
                elif self.x >= x2 and self.y >= y2:
                    self.current_tuple += 1
            else:  # moving up
                if self.x >= x2 and self.y <= y2:
                    self.current_tuple += 1
                elif self.x >= x2 and self.y >= y2:
                    self.current_tuple += 1
        else: # moving left
            if y2 >= y1:  # moving down
                if self.x <= x2 and self.y >= y2:
                    self.current_tuple += 1
                else:
                    if self.x <= x2 and self.y <= y2:
                        self.current_tuple += 1
            else:  # moving up
                if self.x <= x2 and self.y <= y2:
                    self.current_tuple += 1
                elif self.x <= x2 and self.y >= y2:
                    self.current_tuple += 1

        self.animation_count += 1
        if self.animation_count > self.total_animations:
            self.animation_count = 0

        return self.image_direction, image_count

    def walk(self):
        """
        make a given enemy walk along its self.path
        :return: Tuple
        """
        image_name = self.move()
        return self.x, self.y, self.all_images[self.name + str(self.level) + 'walk' + image_name[0] + image_name[1]]

    def die(self):
        """
        make an enemy stop and die in the direction it is facing
        it is the duty of the caller to stop the animation after it has completed
        :return: Tuple
        """
        image_name = '_' + str(self.death_animation_count).rjust(2, '0') + '.png'
        self.death_animation_count += 1
        return self.x, self.y, self.all_images[self.name + str(self.level) + 'die' + self.image_direction + image_name]

    def attack(self):
        """
        make an enemy stop and attack in the direction it is facing
        it is the duty of the caller to control the animation stop and restart it
        :return: Tuple
        """
        image_name = '_' + str(self.attack_animation_count).rjust(2, '0') + '.png'
        self.attack_animation_count += 1
        return self.x, self.y, self.all_images[self.name + str(self.level) + 'attack' + self.image_direction + image_name]

    @staticmethod
    def get_next_coordinate(point_a, point_b, movement):
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