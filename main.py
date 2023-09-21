import pygame

BACKGROUND = (0,154,255)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

for x in range(30):
    pass

# Create an 1280x720 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption('Worlds hardest game')


class Player(pygame.sprite.Sprite):
    """ This class represents the red square that the player
    controls. """

    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill('red')

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

        enemy_hit_list = pygame.sprite.spritecollide(self, self.enemies, False)
        for enemy in enemy_hit_list:
            #Reset player:
            self.rect.x = 55
            self.rect.y = 55


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

changingspeed_x = 0
changingspeed_y = 0
#Handle movement of enemies
def enemy_handler(x,y):
    global enemy_list
    for enemy in enemy_list:
        enemy.changespeed(x,y)
        #enemy.rect.center = (enemy.rect.center[0] + changingspeed_x, enemy.rect.center[1] + changingspeed_y)











# Call this function so the Pygame library can initialize itself
pygame.init()

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()


# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

wall1 = Wall(0, 0, 10, 600)
wall2 = Wall(10, 0, 790, 10)
wall3 = Wall(10, 200, 100, 10)
wall4 = Wall(200,200,100,10)
wall5 = Wall(300,400,200,50)
wall_list.add(wall1,wall2,wall3,wall4, wall5)
all_sprite_list.add(wall_list)


#Create enemies
enemy_list = pygame.sprite.Group()

enemy1 = Enemy(200,200)
enemy2 = Enemy(300,300)
enemy3 = Enemy(400,400)
enemy_list.add(enemy1,enemy2,enemy3)
all_sprite_list.add(enemy_list)


# Create the player paddle object
player = Player(50, 50)
player.walls = wall_list
player.enemies = enemy_list

all_sprite_list.add(player)



clock = pygame.time.Clock()



done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_d:
                player.changespeed(3, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, -3)
            elif event.key == pygame.K_s:
                player.changespeed(0, 3)

            elif event.key == pygame.K_LEFT:
                enemy1.changespeed(-3,0)
            elif event.key == pygame.K_RIGHT:
                enemy1.changespeed(3,0)
            elif event.key == pygame.K_UP:
                enemy1.changespeed(0,-3)
            elif event.key == pygame.K_DOWN:
                enemy1.changespeed(0,3)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.changespeed(3, 0)
            elif event.key == pygame.K_d:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, 3)
            elif event.key == pygame.K_s:
                player.changespeed(0, -3)


            elif event.key == pygame.K_LEFT:
                enemy1.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                enemy1.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                enemy1.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                enemy1.changespeed(0, -3)

    all_sprite_list.update()

    screen.fill(BACKGROUND)


    #draw enemies and update

    all_sprite_list.draw(screen)


    pygame.display.flip()

    clock.tick(60)

pygame.quit()