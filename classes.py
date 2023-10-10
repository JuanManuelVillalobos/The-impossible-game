import pygame

WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
GREEN = (0, 255, 0)

highScore = open(HighScores.txt, 'r+') #open file for reading and writing
name = 'Juanma'


class Player(pygame.sprite.Sprite):
    """ This class represents the red square that the player
    controls. """

    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.respawn = pygame.Vector2()
        self.image = pygame.Surface([15, 15])
        self.image.fill('red')

        # Set respawn position
        self.respawn.x = x
        self.respawn.y = y

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None

        #Determine if cube won
        self.win = None


    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        blockHitList = pygame.sprite.spritecollide(self, self.walls, False)
        for block in blockHitList:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y


        # Check and see if we hit anything
        blockHitList = pygame.sprite.spritecollide(self, self.walls, False)
        for block in blockHitList:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        # Check and see if we hit an enemy
        enemyHitList = pygame.sprite.spritecollide(self, self.enemies, False)
        for enemy in enemyHitList:
            # Reset player:
            self.rect.x = self.respawn.x
            self.rect.y = self.respawn.y

    def win(self):
        winningCubeHitList = pygame.sprite.spritecollide(self, self.winning_cube, False)
        for winning_cube in winningCubeHitList:
            self.win = True


class Wall(pygame.sprite.Sprite):
    """ Wall the enemy can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the enemy can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.radius = 5
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = pygame.Vector2(x, y)

        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the enemy. """
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the enemy position. """
        self.rect.center = (self.rect.center[0] + self.change_x, self.rect.center[1] + self.change_y)


class WinningCube(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Make winning block
        self.image = pygame.Surface([50, 50])
        self.image.fill(GREEN)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class BaseLevel():
    def __init__(self):
        self.level_sprite_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.winning_cube = pygame.sprite.Group()

class Level1(BaseLevel):
    def __init__(self):
        super().__init__()
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
        self.wall_list.add(wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16)
        self.level_sprite_list.add(self.wall_list)

        # Create enemies
        enemy1 = Enemy(227, 212)
        enemy2 = Enemy(227, 289)
        enemy3 = Enemy(484, 177)
        enemy4 = Enemy(484, 252)
        self.enemy_list.add(enemy1, enemy2, enemy3, enemy4)
        self.level_sprite_list.add(self.enemy_list)

        # Create winning block
        self.winning = WinningCube(632, 232)
        self.winning_cube.add(self.winning)
        self.level_sprite_list.add(self.winning_cube)


class Level2(BaseLevel):
    def __init__(self):
        super().__init__()
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
        enemy1 = Enemy(166, 157)
        enemy2 = Enemy(238, 157)
        enemy3 = Enemy(310, 157)
        enemy4 = Enemy(382, 157)
        enemy5 = Enemy(454, 157)
        enemy6 = Enemy(526, 157)
        enemy7 = Enemy(203, 327)
        enemy8 = Enemy(273, 327)
        enemy9 = Enemy(343, 327)
        enemy10 = Enemy(413, 327)
        enemy11 = Enemy(483, 327)
        enemy12 = Enemy(553, 327)
        self.enemy_list.add(enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10, enemy11, enemy12)
        self.level_sprite_list.add(self.enemy_list)

        # Create winning block
        self.winning = WinningCube(630, 220)
        self.winning_cube.add(self.winning)
        self.level_sprite_list.add(self.winning_cube)

class Level3(BaseLevel):
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)
        wall1 = Wall(0, 0, 10, 600)
        wall2 = Wall(400, 0, 100, 10)
        wall3 = Wall(10, 200, 100, 10)
        wall4 = Wall(200, 200, 100, 10)
        wall5 = Wall(300, 400, 200, 50)
        self.wall_list.add(wall1, wall2, wall3, wall4, wall5)
        self.level_sprite_list.add(self.wall_list)

        # Create enemies
        enemy1 = Enemy(200, 200)
        enemy2 = Enemy(300, 300)
        enemy3 = Enemy(400, 400)
        self.enemy_list.add(enemy1, enemy2, enemy3)
        self.level_sprite_list.add(self.enemy_list)

        # Create winning block
        self.winning = WinningCube(500, 300)
        self.winning_cube.add(self.winning)
        self.level_sprite_list.add(self.winning_cube)


class HighScore():
    # Constructor function
    def __init__(self):
        self.score = 0
        self.high_score = 0

        highScores = highScore.readlines()

        for line in highScores:
            if line == name:
                self.high_score = int(highScores[highScores.index(line) + 1])
                break

def update(self):
        if self.score > self.high_score:
            self.high_score = self.score
            highScore.write(name + '\n' + str(self.high_score))
