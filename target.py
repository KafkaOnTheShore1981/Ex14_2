import pygame
from pygame.sprite import Sprite

class Target(Sprite):
    def __init__(self,ai_settings,screen):
        super(Target,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        self.rect=pygame.Rect(0,0,ai_settings.target_width,ai_settings.target_height)
        self.rect.right=self.screen.get_rect().right
        self.rect.centery=self.screen.get_rect().centery

        self.y=float(self.rect.y)
        self.color=ai_settings.target_color
        self.speed_factor=ai_settings.target_speed_factor

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.top<0:
            return True
        elif self.rect.bottom>screen_rect.bottom:
            return True

    def update(self):
        self.y+=(self.speed_factor*self.ai_settings.fleet_direction)
        self.rect.y=self.y

    def draw_target(self):
        pygame.draw.rect(self.screen,self.color,self.rect)