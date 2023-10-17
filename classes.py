import pygame

WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
GREEN = (0, 255, 0)

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

        # Groups of player
        self.walls = None
        self.enemies = None
        self.winning_cube = None

        # Determine if cube won
        self.win = False

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
        for _ in enemy_hit_list:
            # Reset player:
            self.rect.x = self.respawn.x
            self.rect.y = self.respawn.y

    def reset(self):
        self.rect.x = self.respawn.x
        self.rect.y = self.respawn.y

    def winner(self):
        winning_cube_hit_list = pygame.sprite.spritecollide(self, self.winning_cube, False)
        for _ in winning_cube_hit_list:
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
    def __init__(self, starting_x, starting_y, final_x, final_y, step, stop1_x=0, stop1_y=0, stop2_x=0, stop2_y=0):
        super().__init__()
        # Positions of enemy
        self.startingPosition = pygame.Vector2(starting_x, starting_y)
        self.finalPosition = pygame.Vector2(final_x, final_y)
        self.stop1 = pygame.Vector2(stop1_x, stop1_y)
        self.stop2 = pygame.Vector2(stop2_x, stop2_y)

        self.radius = 8
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = pygame.Vector2(starting_x, starting_y)
        self.step = step
        self.inFinalPoint = False

        self.iteration = 0

        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def move(self):
        """ Move the enemy. """
        if self.stop1[0] != 0 or self.stop1[1] and self.stop2[0] != 0 or self.stop2[1] != 0:
            self.multiple_step_move()
        else:
            self.single_step_move(self.startingPosition[0], self.startingPosition[1], self.finalPosition[0],
                                  self.finalPosition[1])

    def single_step_move(self, starting_x, starting_y, final_x, final_y):
        """ Move the enemy with a single set of initial and final points. """
        position_x = self.rect.center[0]
        position_y = self.rect.center[1]
        final_point_difference_position_x = final_x - position_x
        final_point_difference_position_y = final_y - position_y
        starting_point_difference_position_x = starting_x - position_x
        starting_point_difference_position_y = starting_y - position_y
        if (abs(final_point_difference_position_x) <= self.step and
                abs(final_point_difference_position_y) <= self.step):
            self.inFinalPoint = True

        elif abs(starting_point_difference_position_x) <= self.step and abs(
                starting_point_difference_position_y) <= self.step:
            self.inFinalPoint = False

        if self.inFinalPoint:
            if starting_point_difference_position_x > 0:
                self.change_x = self.step
            elif starting_point_difference_position_x < 0:
                self.change_x = self.step * -1
            if starting_point_difference_position_y > 0:
                self.change_y = self.step
            elif starting_point_difference_position_y < 0:
                self.change_y = self.step * -1

        elif not self.inFinalPoint:
            if final_point_difference_position_x > 0:
                self.change_x = self.step
            elif final_point_difference_position_x < 0:
                self.change_x = self.step * -1
            if final_point_difference_position_y > 0:
                self.change_y = self.step
            elif final_point_difference_position_y < 0:
                self.change_y = self.step * -1

    def multiple_step_move(self):
        stop1_x = self.stop1[0] + self.startingPosition[0]
        stop1_y = self.stop1[1] + self.startingPosition[1]
        stop2_x = self.stop2[0] + self.startingPosition[0]
        stop2_y = self.stop2[1] + self.startingPosition[1]
        final_x = [stop1_x, stop2_x, self.finalPosition[0], self.startingPosition[0]]
        final_y = [stop1_y, stop2_y, self.finalPosition[1], self.startingPosition[1]]
        position_x = self.rect.center[0]
        position_y = self.rect.center[1]
        final_point_difference_position_x = final_x[self.iteration] - position_x
        final_point_difference_position_y = final_y[self.iteration] - position_y

        if abs(final_point_difference_position_x) <= self.step and abs(final_point_difference_position_y) <= self.step:
            if self.iteration + 1 == 4:
                self.iteration = 0
            else: self.iteration += 1

        if abs(final_point_difference_position_x) <= self.step:
            self.change_x = 0
        elif final_point_difference_position_x > 0:
            self.change_x = self.step
        elif final_point_difference_position_x < 0:
            self.change_x = self.step * -1
        if abs(final_point_difference_position_y) <= self.step:
            self.change_y = 0
        elif final_point_difference_position_y > 0:
            self.change_y = self.step
        elif final_point_difference_position_y < 0:
            self.change_y = self.step * -1

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
