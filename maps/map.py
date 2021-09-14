import pygame
import os


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.enemy_width = 64
        self.enemy_height = 64
        self.maps = []
        self.map_paths = {}

        for i in range(3):
            image = pygame.image.load(os.path.join('assets', 'maps', 'map' + str(i) + '.png'))
            self.maps.append(pygame.transform.scale(image, (self.width, self.height)))
            self.map_paths[i] = []

        self.map_paths[0].append([(1392, 221), (1332, 217), (1285, 190), (1225, 162), (1157, 155), (1080, 157), (1001, 157), (934, 191), (888, 253), (871, 309), (847, 359), (798, 386), (718, 387), (654, 350), (554, 346), (495, 385), (460, 439), (450, 503), (433, 525), (378, 561), (282, 565), (146, 565), (7, 569)])
        self.map_paths[0].append([(1394, 568), (828, 564), (787, 542), (748, 530), (723, 459), (704, 389), (644, 350), (570, 349), (510, 379), (480, 421), (458, 489), (420, 545), (371, 572), (339, 575), (59, 575), (8, 573)])
        self.map_paths[1].append([(1396, 83), (572, 96), (516, 123), (483, 171), (475, 208), (488, 255), (540, 313), (584, 324), (642, 327), (814, 326), (859, 350), (899, 395), (913, 441), (903, 483), (869, 526), (802, 553), (734, 556), (484, 551), (458, 537), (435, 528), (407, 524), (369, 531), (336, 540), (310, 551), (247, 534), (234, 518), (207, 499), (149, 500), (9, 499)])
        self.map_paths[2].append([(1296, 738), (1292, 682), (1286, 638), (1258, 591), (1202, 565), (1155, 553), (1104, 537), (1078, 515), (1059, 493), (1049, 465), (1062, 403), (1104, 345), (1150, 329), (1193, 321), (1228, 309), (1288, 259), (1299, 213), (1283, 149), (1265, 115), (1216, 90), (1157, 78), (1032, 73), (1009, 62), (975, 53), (937, 53), (913, 60), (888, 68), (873, 78), (584, 89), (545, 107), (510, 141), (486, 197), (468, 256), (436, 300), (364, 324), (321, 336), (264, 363), (236, 421), (223, 489), (176, 542), (103, 561), (4, 560)])


    def get_full_path(self):
        pass
    # planning on building full paths of .05 movement then just grabbing a new full path on wave generation