import pygame
from levels import Level1, Level2, Level3
from classes import Player

BACKGROUND = (0, 154, 255)

# Screen dimensions
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 450

# Create a 1280x720 sized screen
high_score_manager = HighScore()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption("The Impossible Game")


# Handle movement of enemies
def enemy_mover(enemy_list):
    for enemy in enemy_list:
        enemy.move()

# Call this function so the Pygame library can initialize itself
pygame.init()

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

levels = [Level1(), Level2(), Level3()]

# Create the player paddle object
player = Player(70, 220)

clock = pygame.time.Clock()

for level in range(len(levels)):
    player.respawn.x = levels[level].playerRespawn.x
    player.respawn.y = levels[level].playerRespawn.y
    player.winning_cube = levels[level].winning_cube
    player.walls = levels[level].wall_list
    player.enemies = levels[level].enemy_list
    all_sprite_list.add(levels[level].level_sprite_list)
    all_sprite_list.add(player)
    player.reset()
    player_speed = levels[level].playerSpeed
    done = False
    player.win = False
    while not done:

        n = n + 10
        if player.win == True:
            break


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.changespeed(-1 * player_speed, 0)
                elif event.key == pygame.K_d:
                    player.changespeed(player_speed, 0)
                elif event.key == pygame.K_w:
                    player.changespeed(0, -1 * player_speed)
                elif event.key == pygame.K_s:
                    player.changespeed(0, player_speed)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.changespeed(player_speed, 0)
                elif event.key == pygame.K_d:
                    player.changespeed(-1 * player_speed, 0)
                elif event.key == pygame.K_w:
                    player.changespeed(0, player_speed)
                elif event.key == pygame.K_s:
                    player.changespeed(0, -1 * player_speed)

        enemy_mover(levels[level].enemy_list)

        all_sprite_list.update()

        screen.fill(BACKGROUND)

        all_sprite_list.draw(screen)

        pygame.display.flip()

        player.winner()

        clock.tick(60)

    all_sprite_list.remove(levels[level].level_sprite_list)
    all_sprite_list.remove(player)

    if done:
        pygame.quit()
        break
BACKGROUND = (0, 154, 255)

# Screen dimensions
SCREEN_WIDTH = 550
SCREEN_HEIGHT = 250

# Create a 1280x720 sized screen
high_score_manager = HighScore()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption("")
new_score = 9999 - n
high_score_manager.update_high_scores(new_score)
high_score_manager.display_high_scores(screen)  # Draw high scores after updating the display
pygame.quit()

