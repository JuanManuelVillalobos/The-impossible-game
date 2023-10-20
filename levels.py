import pygame
from classes import Wall, Enemy, WinningCube


class BaseLevel:
    def __init__(self):
        self.level_sprite_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.winning_cube = pygame.sprite.Group()
        self.playerRespawn = pygame.Vector2()
        self.playerSpeed = 2
        self.enemySpeed = 3


class Level1(BaseLevel):
    def __init__(self):
        super().__init__()
        # Determine Player Respawn
        self.playerRespawn.x = 70
        self.playerRespawn.y = 220

        # Make the walls. (x_pos, y_pos, width, height)
        wall1 = Wall(22, 122, 110, 5)
        wall2 = Wall(22, 122, 5, 220)
        wall3 = Wall(22, 342, 185, 5)
        wall4 = Wall(132, 122, 5, 185)
        wall5 = Wall(132, 307, 40, 5)
        wall6 = Wall(172, 157, 5, 150)
        wall7 = Wall(207, 307, 5, 35)
        wall8 = Wall(172, 157, 333, 5)
        wall9 = Wall(207, 307, 335, 5)
        wall10 = Wall(502, 122, 5, 35)
        wall11 = Wall(542, 157, 5, 150)
        wall12 = Wall(542, 157, 35, 5)
        wall13 = Wall(502, 122, 190, 5)
        wall14 = Wall(577, 157, 5, 185)
        wall15 = Wall(692, 122, 5, 220)
        wall16 = Wall(577, 342, 115, 5)
        self.wall_list.add(wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12,
                           wall13, wall14, wall15, wall16)
        self.level_sprite_list.add(self.wall_list)

        # Create enemies
        enemy1 = Enemy(190, 212, 530, 212, self.enemySpeed)
        enemy2 = Enemy(190, 289, 530, 289, self.enemySpeed)
        enemy3 = Enemy(530, 177, 190, 177, self.enemySpeed)
        enemy4 = Enemy(530, 252, 190, 252, self.enemySpeed)
        self.enemy_list.add(enemy1, enemy2, enemy3, enemy4)
        self.level_sprite_list.add(self.enemy_list)

        # Create winning block
        self.winning = WinningCube(632, 232)
        self.winning_cube.add(self.winning)
        self.level_sprite_list.add(self.winning_cube)


class Level2(BaseLevel):
    def __init__(self):
        super().__init__()
        # Determine Player Respawn
        self.playerRespawn.x = 70
        self.playerRespawn.y = 238

        # Make the walls. (x_pos, y_pos, width, height)
        wall1 = Wall(42, 207, 5, 70)
        wall2 = Wall(684, 207, 5, 70)
        wall3 = Wall(42, 207, 108, 5)
        wall4 = Wall(576, 207, 108, 5)
        wall5 = Wall(42, 277, 108, 5)
        wall6 = Wall(576, 277, 108, 5)
        wall7 = Wall(150, 133, 5, 74)
        wall8 = Wall(576, 133, 5, 74)
        wall9 = Wall(150, 277, 5, 73)
        wall10 = Wall(576, 277, 5, 73)
        wall11 = Wall(150, 133, 426, 5)
        wall12 = Wall(150, 350, 426, 5)
        self.wall_list.add(wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12)
        self.level_sprite_list.add(self.wall_list)

        # Create enemies
        enemy1 = Enemy(176, 150, 176, 340, self.enemySpeed)
        enemy2 = Enemy(248, 150, 248, 340, self.enemySpeed)
        enemy3 = Enemy(320, 150, 320, 340, self.enemySpeed)
        enemy4 = Enemy(392, 150, 392, 340, self.enemySpeed)
        enemy5 = Enemy(464, 150, 464, 340, self.enemySpeed)
        enemy6 = Enemy(536, 150, 536, 340, self.enemySpeed)
        enemy7 = Enemy(213, 340, 213, 150, self.enemySpeed)
        enemy8 = Enemy(283, 340, 283, 150, self.enemySpeed)
        enemy9 = Enemy(353, 340, 353, 150, self.enemySpeed)
        enemy10 = Enemy(423, 340, 423, 150, self.enemySpeed)
        enemy11 = Enemy(493, 340, 493, 150, self.enemySpeed)
        enemy12 = Enemy(563, 340, 563, 150, self.enemySpeed)
        self.enemy_list.add(enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10, enemy11,
                            enemy12)
        self.level_sprite_list.add(self.enemy_list)

        # Create winning block
        self.winning = WinningCube(630, 220)
        self.winning_cube.add(self.winning)
        self.level_sprite_list.add(self.winning_cube)


class Level3(BaseLevel):
    def __init__(self):
        super().__init__()
        # Determine Player Respawn and Speed
        self.playerRespawn.x = 35
        self.playerRespawn.y = 185

        # Ovverdie enemy speed
        self.enemySpeed = 2

        # Make the walls. (x_pos, y_pos, width, height)
        wall1 = Wall(13, 163, 58, 5)
        wall2 = Wall(13, 163, 5, 58)
        wall3 = Wall(13, 221, 58, 5)
        wall4 = Wall(70, 105, 5, 58)
        wall5 = Wall(70, 221, 5, 58)
        wall6 = Wall(70, 105, 115, 5)
        wall7 = Wall(79, 278, 276, 5)
        wall8 = Wall(185, 105, 5, 116)
        wall9 = Wall(185, 221, 58, 5)
        wall10 = Wall(243, 105, 5, 116)
        wall11 = Wall(243, 105, 284, 5)
        wall12 = Wall(357, 163, 5, 115)
        wall13 = Wall(357, 163, 58, 5)
        wall14 = Wall(415, 163, 5, 115)
        wall15 = Wall(415, 278, 115, 5)
        wall16 = Wall(530, 105, 5, 58)
        wall17 = Wall(530, 221, 5, 58)
        wall18 = Wall(530, 163, 58, 5)
        wall19 = Wall(530, 221, 58, 5)
        wall20 = Wall(587, 163, 5, 58)
        self.wall_list.add(wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12,
                           wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20)
        self.level_sprite_list.add(self.wall_list)

        adder = 30
        # Create enemies
        enemy1 = Enemy(85, 122, 85 + adder, 122, self.enemySpeed, 0, adder, adder, adder)
        enemy2 = Enemy(142, 1220, 142 + adder, 1220, self.enemySpeed, 0, adder, adder, adder)
        enemy3 = Enemy(314, 122, 314 + adder, 122, self.enemySpeed, 0, adder, adder, adder)
        enemy4 = Enemy(371, 122, 371 + adder, 122, self.enemySpeed, 0, adder, adder, adder)
        enemy5 = Enemy(428, 122, 428 + adder, 122, self.enemySpeed, 0, adder, adder, adder)
        enemy6 = Enemy(485, 122, 485 + adder, 122, self.enemySpeed, 0, adder, adder, adder)
        enemy7 = Enemy(85, 179, 85 + adder, 179, self.enemySpeed, 0, adder, adder, adder)
        enemy8 = Enemy(142, 179, 142 + adder, 179, self.enemySpeed, 0, adder, adder, adder)
        enemy9 = Enemy(256, 179, 256 + adder, 179, self.enemySpeed, 0, adder, adder, adder)
        enemy10 = Enemy(313, 179, 313 + adder, 179, self.enemySpeed, 0, adder, adder, adder)
        enemy11 = Enemy(427, 179, 427 + adder, 179, self.enemySpeed, 0, adder, adder, adder)
        enemy12 = Enemy(484, 179, 484 + adder, 179, self.enemySpeed, 0, adder, adder, adder)
        enemy13 = Enemy(85, 236, 85 + adder, 236, self.enemySpeed, 0, adder, adder, adder)
        enemy14 = Enemy(142, 236, 142 + adder, 236, self.enemySpeed, 0, adder, adder, adder)
        enemy15 = Enemy(199, 236, 199 + adder, 236, self.enemySpeed, 0, adder, adder, adder)
        enemy16 = Enemy(256, 236, 256 + adder, 236, self.enemySpeed, 0, adder, adder, adder)
        enemy17 = Enemy(313, 236, 313 + adder, 236, self.enemySpeed, 0, adder, adder, adder)
        enemy18 = Enemy(427, 236, 427 + adder, 236, self.enemySpeed, 0, adder, adder, adder)
        enemy19 = Enemy(484, 236, 484 + adder, 236, self.enemySpeed, 0, adder, adder, adder)
        self.enemy_list.add(enemy1)#, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10, enemy11,
                            #enemy12, enemy13, enemy14, enemy15, enemy16, enemy17, enemy18, enemy19)
        self.level_sprite_list.add(self.enemy_list)

        # Create winning block
        self.winning = WinningCube(537, 170)
        self.winning_cube.add(self.winning)
        self.level_sprite_list.add(self.winning_cube)

def hidden_level(player_x, player_y, levels):
    if player_x == 117 and player_y == 127:
        levels.insert(1,Level3())
        return True