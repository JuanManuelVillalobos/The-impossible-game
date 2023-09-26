import pygame
from classes import Player,Wall,Enemy


BACKGROUND = (0,154,255)

# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Create an 1280x720 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption('Worlds hardest game')


#Handle movement of enemies
def enemy_handler(x,y):
    global enemy_list
    for enemy in enemy_list:
        enemy.changespeed(x,y)

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
                enemy_handler(-3,0)
            elif event.key == pygame.K_RIGHT:
                enemy_handler(3,0)
            elif event.key == pygame.K_UP:
                enemy_handler(0,-3)
            elif event.key == pygame.K_DOWN:
                enemy_handler(0,3)

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
                enemy_handler(3, 0)
            elif event.key == pygame.K_RIGHT:
                enemy_handler(-3, 0)
            elif event.key == pygame.K_UP:
                enemy_handler(0, 3)
            elif event.key == pygame.K_DOWN:
                enemy_handler(0, -3)

    all_sprite_list.update()

    screen.fill(BACKGROUND)

    all_sprite_list.draw(screen)


    pygame.display.flip()

    clock.tick(60)

pygame.quit()

for x in range(0,100):
    pass