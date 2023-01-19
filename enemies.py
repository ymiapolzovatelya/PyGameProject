from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(enemieses)
        self.image = load_image('enemie_l.png')
        self.rect = pygame.Rect(x, y, 20, 30)
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x

    def update(self):
        pass


enemieseses = []

enemieses = pygame.sprite.Group()

enemieseses.append(Enemy(600, 360))
enemieseses.append(Enemy(900, 230))
enemieseses.append(Enemy(1200, 360))
enemieseses.append(Enemy(1400, 260))
enemieseses.append(Enemy(2000, 170))
enemieseses.append(Enemy(1000, 170))
enemieseses.append(Enemy(2800, 360))
enemieseses.append(Enemy(2800, 110))
enemieseses.append(Enemy(3200, 240))
enemieseses.append(Enemy(4000, 300))
enemieseses.append(Enemy(3700, 360))
enemieseses.append(Enemy(4000, 290))
enemieseses.append(Enemy(3500, 110))
enemieseses.append(Enemy(4200, 110))
enemieseses.append(Enemy(4600, 230))
enemieseses.append(Enemy(4820, 360))
enemieseses.append(Enemy(5200, 260))
enemieseses.append(Enemy(5200, 110))
enemieseses.append(Enemy(5500, 230))
enemieseses.append(Enemy(5900, 190))
enemieseses.append(Enemy(6560, 110))
enemieseses.append(Enemy(6560, 360))
enemieseses.append(Enemy(6400, 230))
