import pygame
from levels import Level1, Level2, hidden_level
from classes import Player, HighScore, enemy_mover

BACKGROUND = (0, 154, 255)

# Screen dimensions
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 450

# Create a 1280x720 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption("The Impossible Game")




# Call this function so the Pygame library can initialize itself
pygame.init()

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

levels = [Level1(), Level2()]


# Create the player paddle object
player = Player(70, 220)

clock = pygame.time.Clock()
level = 0

running = True

for level in range(len(levels)+2):
    try:
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


            if hidden_level(player.rect.x,player.rect.y,levels):
                break

            if player.win:
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

            player.display_deaths(screen)

            clock.tick(60)


        all_sprite_list.remove(levels[level].level_sprite_list)
        all_sprite_list.remove(player)

        if done:
            break

    except IndexError:
        break

if done:
    pass

else:
    high_score_manager = HighScore()
    new_score = 10000 - ((pygame.time.get_ticks() / 10) * (1 + player.deaths))  # Calculate score
    high_score_manager.update_high_scores(new_score)

    pygame.display.set_caption('High Scores')  # Set the title of the window

    done = False
    while not done:
        screen.fill(BACKGROUND)  # Fill the screen with background color
        high_score_manager.display_high_scores(screen)  # Draw high scores after updating the display
        pygame.display.flip()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

pygame.quit()
