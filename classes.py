import pygame

WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

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

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
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
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        # Check and see if we hit an enemy
        enemy_hit_list = pygame.sprite.spritecollide(self, self.enemies, False)
        for enemy in enemy_hit_list:
            #Reset player:
            self.rect.x = self.respawn.x
            self.rect.y = self.respawn.y


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
        self.rect.center = pygame.Vector2(x,y)

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


class Level1():
    def __init__(self):
        self.level_sprite_list = pygame.sprite.Group()

        # Make the walls. (x_pos, y_pos, width, height)
        self.wall_list = pygame.sprite.Group()

        wall1 = Wall(0, 0, 10, 600)
        wall2 = Wall(10, 0, 790, 10)
        wall3 = Wall(10, 200, 100, 10)
        wall4 = Wall(200, 200, 100, 10)
        wall5 = Wall(300, 400, 200, 50)
        self.wall_list.add(wall1, wall2, wall3, wall4, wall5)
        self.level_sprite_list.add(self.wall_list)

        # Create enemies
        self.enemy_list = pygame.sprite.Group()

        enemy1 = Enemy(200, 200)
        enemy2 = Enemy(300, 300)
        enemy3 = Enemy(400, 400)
        self.enemy_list.add(enemy1, enemy2, enemy3)
        self.level_sprite_list.add(self.enemy_list)

        self.winning_rect = pygame.Rect(700, 500, 50, 50)
        self.level_sprite_list.add(self.winning_rect)


class Level2():
    def __init__(self):
        self.level_sprite_list = pygame.sprite.Group()

        # Make the walls. (x_pos, y_pos, width, height)
        self.wall_list = pygame.sprite.Group()

        wall1 = Wall(0, 0, 10, 600)
        wall2 = Wall(10, 0, 790, 10)
        wall3 = Wall(10, 200, 100, 10)
        wall4 = Wall(200, 200, 100, 10)
        wall5 = Wall(300, 400, 200, 50)
        self.wall_list.add(wall1, wall2, wall3, wall4, wall5)
        self.level_sprite_list.add(self.wall_list)

        # Create enemies
        self.enemy_list = pygame.sprite.Group()

        enemy1 = Enemy(200, 200)
        enemy2 = Enemy(300, 300)
        enemy3 = Enemy(400, 400)
        self.enemy_list.add(enemy1, enemy2, enemy3)
        self.level_sprite_list.add(self.enemy_list)
        pass

class Level3():
    def __init__(self):
        self.level_sprite_list = pygame.sprite.Group()

        # Make the walls. (x_pos, y_pos, width, height)
        self.wall_list = pygame.sprite.Group()

        wall1 = Wall(0, 0, 10, 600)
        wall2 = Wall(10, 0, 790, 10)
        wall3 = Wall(10, 200, 100, 10)
        wall4 = Wall(200, 200, 100, 10)
        wall5 = Wall(300, 400, 200, 50)
        self.wall_list.add(wall1, wall2, wall3, wall4, wall5)
        self.level_sprite_list.add(self.wall_list)

        # Create enemies
        self.enemy_list = pygame.sprite.Group()

        enemy1 = Enemy(200, 200)
        enemy2 = Enemy(300, 300)
        enemy3 = Enemy(400, 400)
        self.enemy_list.add(enemy1, enemy2, enemy3)
        self.level_sprite_list.add(self.enemy_list)
        pass