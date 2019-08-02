import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():

    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    play_button = Button(ai_settings, screen, "Play")

    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:

        screen.fill(ai_settings.bg_color)
        ship.blitme()

        gf.check_events(ai_settings, screen, stats, sb,
                        play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats,
                              sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats,
                             sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship,
                         aliens, bullets, play_button)

        pygame.display.flip()


run_game()
