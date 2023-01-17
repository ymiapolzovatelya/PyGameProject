import pygame, os


def load_image(name, colorkey=None):
    fullname = os.path.join('img', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
    image = pygame.image.load(fullname)
    return image


def cut_sheet(name, sheet, columns, rows):
    rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                            sheet.get_height() // rows)
    a = []
    for j in range(rows):
        for i in range(columns):
            frame_location = (rect.w * i, rect.h * j)
            a.append(sheet.subsurface(pygame.Rect(
                frame_location, rect.size)))
    ANIMATIONS[name] = a


# main
WIDTH = 600
HEIGHT = 480
windowSize = (WIDTH,HEIGHT)
FPS = 40
screen = pygame.display.set_mode(windowSize)
game_time = pygame.time.Clock()
started = True

LEFT_BOUND = 0
RIGHT_BOUND = -6164

# physics
GRAV = 0.5

# player
SPEED = 4
JUMP = -10

# animations
ANIMATIONS = {}
cut_sheet('stay_r', load_image('stay.png'), 2, 1)
cut_sheet('stay_l', load_image('stay_l.png'), 2, 1)
cut_sheet('in_water_r', load_image('in_water.png'), 1, 1)
cut_sheet('in_water_l', load_image('in_water_l.png'), 1, 1)
cut_sheet('jump_r', load_image('jump_r.png'), 4, 1)
cut_sheet('jump_l', load_image('jump_l.png'), 4, 1)
cut_sheet('lej_r', load_image('lej_r.png'), 1, 1)
cut_sheet('lej_l', load_image('lej_l.png'), 1, 1)
cut_sheet('run_r', load_image('run_r.png'), 6, 1)
cut_sheet('run_r_u', load_image('run_r_u.png'), 3, 1)
cut_sheet('run_r_d', load_image('run_r_d.png'), 3, 1)
cut_sheet('run_l', load_image('run_l.png'), 6, 1)
cut_sheet('run_l_u', load_image('run_l_u.png'), 3, 1)
cut_sheet('run_l_d', load_image('run_l_d.png'), 3, 1)
cut_sheet('shoot_in_water_r', load_image('shoot_in_water.png'), 1, 1)
cut_sheet('shoot_in_water_l', load_image('shoot_in_water_l.png'), 1, 1)
cut_sheet('stay_up_r', load_image('stay_up.png'), 2, 1)
cut_sheet('stay_up_l', load_image('stay_up_l.png'), 2, 1)
cut_sheet('fall_r', load_image('fall_r.png'), 1, 1)
cut_sheet('fall_l', load_image('fall_l.png'), 1, 1)
print(ANIMATIONS)
