import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from target import Target

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Space War")
    play_button=Button(ai_settings,screen,"Play")
    stats=GameStats(ai_settings)
    ship=Ship(ai_settings,screen)
    bullets=Group()
    target=Target(ai_settings,screen)
    while True:
        gf.check_events(ai_settings,screen,stats,play_button,ship,target,bullets)
        if stats.game_active:
            ship.update()
            target.update()
            gf.update_bullets(ai_settings,screen,ship,target,bullets)
            gf.update_target(ai_settings,stats,screen,ship,target,bullets)
            gf.check_fail(ai_settings,bullets,stats,target,screen)
        gf.update_screen(ai_settings,screen,stats,ship,target,bullets,play_button)

run_game()