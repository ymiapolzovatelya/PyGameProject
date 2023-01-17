import sys

import pygame.sprite

from settings import *


class Camera(object):
    def __init__(self):
        self.dx = 0

    def apply(self, obj):
        if obj != player:
            obj.rect.x += self.dx
            if obj.rect.x > 0:
                obj.rect.x = 0
                self.dx = 0
            if obj.rect.x < RIGHT_BOUND:
                obj.rect.x = RIGHT_BOUND
                self.dx = 0
        elif obj == player:
            obj.rect.x += self.dx

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)


class Lc(pygame.sprite.Sprite):
    image = load_image('l1c.png')

    def __init__(self):
        super().__init__(l_collision)
        self.image = Lc.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        bullets.add(self)


class Bg(pygame.sprite.Sprite):
    image = load_image('l1.png')

    def __init__(self):
        super().__init__(backgrounds)
        self.image = Bg.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


class Bullet(pygame.sprite.Sprite):
    image = load_image('bullet.png')

    def __init__(self):
        super().__init__(bullets)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.rect.width
        self.rect.y = player.rect.y
        self.view = player.view
        self.sv = player.sv
        self.s = player.horizontal_speed
        self.x_speed = 0
        self.y_speed = 0
        bullets.add(self)

    def update(self):
        if self.sv == 'up':
            self.y_speed = -10
        elif self.sv == 'down':
            self.y_speed = 10
        else:
            self.y_speed = 0
        if self.s == 0 and self.sv == 'up':
            self.x_speed = 0
        elif self.view == 'right':
            self.x_speed = 10
        elif self.view == 'left':
            self.x_speed = -10
        self.rect = self.rect.move(self.x_speed, self.y_speed)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(players)
        self.image = ANIMATIONS['stay_r'][0]
        self.rect = pygame.Rect(100, 170, 30, 40)
        self.frame = 0
        self.it = 0
        self.vertical_speed = 0
        self.horizontal_speed = 0
        self.pos = [self.rect.x, self.rect.y]
        self.anim_name = 'stay_r'
        self.view = 'right'
        self.jump = False
        self.lie = False
        self.sh = ''
        self.sv = ''

    def player_move(self):
        if self.rect.x < 0:
            self.horizontal_speed = 0
            self.rect.x = 1
        if 1 >= self.vertical_speed >= 0:
            if self.horizontal_speed > 0:
                if self.sv == 'up':
                    self.anim_name = 'run_r_u'
                    self.view = 'right'
                elif self.sv == 'down':
                    self.anim_name = 'run_r_d'
                    self.view = 'right'
                else:
                    self.anim_name = 'run_r'
                    self.view = 'right'
            elif self.horizontal_speed < 0:
                if self.sv == 'up':
                    self.anim_name = 'run_l_u'
                    self.view = 'left'
                elif self.sv == 'down':
                    self.anim_name = 'run_l_d'
                    self.view = 'left'
                else:
                    self.anim_name = 'run_l'
                    self.view = 'left'
            else:
                if self.lie:
                    if self.view == 'right':
                        self.anim_name = 'lej_r'
                    else:
                        self.anim_name = 'lej_l'
                elif self.sv == 'up' and self.view == 'right':
                    self.anim_name = 'stay_up_r'
                    self.view = 'right'
                elif self.sv == 'up' and self.view == 'left':
                    self.anim_name = 'stay_up_l'
                    self.view = 'left'
                elif self.view == 'right':
                    self.anim_name = 'stay_r'
                    self.view = 'right'
                else:
                    self.anim_name = 'stay_l'
                    self.view = 'left'
        elif self.vertical_speed < 0:
            if self.view == 'right':
                self.anim_name = 'jump_r'
            else:
                self.anim_name = 'jump_l'
        elif self.vertical_speed > 1:
            if self.view == 'right':
                self.anim_name = 'fall_r'
            else:
                self.anim_name = 'fall_l'

        if self.rect.y > 410:
            if self.view == 'right':
                self.anim_name = 'in_water_r'
            else:
                self.anim_name = 'in_water_l'
        if not pygame.sprite.collide_mask(self, level_collision):
            self.vertical_speed += GRAV
            if self.vertical_speed > 15:
                self.vertical_speed = 10
            self.jump = False
        else:
            if self.jump:
                self.vertical_speed = JUMP
            else:
                self.vertical_speed = 0

    def update(self, name):
        self.player_move()
        max_frame = len(ANIMATIONS[name])
        if self.it >= 4:
            self.frame = (self.frame + 1) % max_frame
            self.image = ANIMATIONS[name][self.frame]
            self.it = 0
        else:
            self.it += 1
        self.rect = self.rect.move(self.horizontal_speed, self.vertical_speed)


camera = Camera()

backgrounds = pygame.sprite.Group()
l_collision = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
bullets = pygame.sprite.Group()

background = Bg()
level_collision = Lc()
player = Player()

all_sprites.add(backgrounds, players, l_collision, bullets)

pygame.init()
name = 'stay_r'
x = 0
y = 0

while started:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            started = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if player.rect.x < 6164:
                    player.horizontal_speed = SPEED
            if event.key == pygame.K_LEFT:
                if player.rect.x > 5:
                    player.horizontal_speed = -SPEED
            if event.key == pygame.K_DOWN:
                player.lie = True
                player.rect = player.rect.move(0, 10)
            if event.key == pygame.K_w:
                player.sv = 'up'
            if event.key == pygame.K_s:
                player.sv = 'down'
            if event.key == pygame.K_d:
                Bullet()
            elif event.key == pygame.K_SPACE:
                if pygame.sprite.collide_mask(player, level_collision):
                    player.jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.horizontal_speed = 0
            if event.key == pygame.K_DOWN:
                player.lie = False
                player.rect = player.rect.move(player.horizontal_speed, -20)
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player.sv = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.sh = 0

    screen.fill('white')
    backgrounds.draw(screen)
    all_sprites.draw(screen)
    bullets.draw(screen)
    players.draw(screen)
    bullets.update()
    player.update(player.anim_name)
    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    pygame.display.flip()
    game_time.tick(FPS)
pygame.quit()
sys.exit()
