import sys
import pygame
from bullet import Bullet
from target import Target
from time import sleep

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key==pygame.K_DOWN:
        ship.moving_down=True
    elif event.key==pygame.K_UP:
        ship.moving_up=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key==pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets)<ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings, screen,ship)
        bullets.add(new_bullet)

def check_fail(ai_settings,bullets,stats,target,screen):   #定义一个函数，在主函数中被调用
    for bullet in bullets.copy():   #bullets为其他程序其他地方定义的一个编组
        if bullet.rect.right>=screen.get_rect().right:   #判断bullet对象是否飞出屏幕右侧
            bullets.remove(bullet)    #若bullet飞出右侧，则销毁该bullet
            ai_settings.fail_times+=1    #fail_times自增1
            print(ai_settings.fail_times)    #控制台输出fail_times,用于监控不碰撞的次数
        elif pygame.sprite.spritecollide(target,bullets,True):
            ai_settings.fail_times=0    #失败清零``
        elif ai_settings.fail_times>2:
            ai_settings.fail_times=0    #失败清零
            stats.game_active=False    #游戏终止
            pygame.mouse.set_visible(True)    #鼠标可见


def check_keyup_events(event,ship):
    if event.key==pygame.K_DOWN:
        ship.moving_down=False
    elif event.key==pygame.K_UP:
        ship.moving_up=False


def check_events(ai_settings,screen,stats,play_button,ship,target,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,target,bullets,mouse_x,mouse_y)
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)

def check_play_button(ai_settings,screen,stats,play_button,ship,target,bullets,mouse_x,mouse_y):
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active=True

        bullets.empty()
        create_fleet(ai_settings,screen,ship,target)
        ship.center_ship()

def update_screen(ai_settings, screen, stats, ship, target,bullets, play_button):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    target.draw_target()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, target,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right>screen.get_rect().right:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,ship,target,bullets)

def check_bullet_alien_collisions(ai_settings,screen,ship,target,bullets):
    collisions=pygame.sprite.spritecollideany(target,bullets,False)

def create_fleet(ai_settings,screen,ship,target):
    target=Target(ai_settings,screen)

def check_fleet_edges(ai_settings,target):
    if target.check_edges():
        change_fleet_direction(ai_settings,target)

def change_fleet_direction(ai_settings,target):
    ai_settings.fleet_direction*=-1

def update_target(ai_settings,stats,screen,ship,target,bullets):
    check_fleet_edges(ai_settings,target)
    target.update()






