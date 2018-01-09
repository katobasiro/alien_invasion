import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_set, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_set = ai_set
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (0, 0, 55)
        self.font = pygame.font.SysFont(None, 36)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        # At string formatting directive tells Python to insert commas
        # into numbers when converting a numerical value to a string—for
        # example, to output  1,000,000 instead of 1000000 .
        score_str = "Score: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_set.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 100
        self.score_rect.top = self.screen_rect.top + 15

    def show_score(self):
        """Draw scores and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships.
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "Highscore: {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color,
                                                 self.ai_set.bg_color)

        # Center the score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.centerx +\
                                     (self.screen_rect.right -
                                      self.screen_rect.centerx) / 2 - 350
        self.high_score_rect.top = self.screen_rect.top + 15

    def prep_level(self):
        """Turn the level  into a rendered image."""
        self.level_image = self.font.render("Level: " + str(self.stats.level), True,
                                            self.text_color, self.ai_set.bg_color)

        # Position the level velow the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx - 250
        self.level_rect.top = self.screen_rect.top + 15

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_set, self.screen)
            ship.image = pygame.image.load('ai_files/ship2.bmp')
            ship.rect = ship.image.get_rect()
            ship.rect.x = 20 + ship_number * (ship.rect.width + 15)
            ship.rect.y = 5
            self.ships.add(ship)
