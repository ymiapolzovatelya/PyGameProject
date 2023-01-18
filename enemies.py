from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(enemieses)
        self.image = ANIMATIONS['stay_l'][0]
        self.rect = pygame.Rect(x, y, 20, 30)
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x

    def update(self):
        pass


enemieseses = []

enemieses = pygame.sprite.Group()

enemieseses.append(Enemy(600, 369))
enemieseses.append(Enemy(900, 240))
enemieseses.append(Enemy(1200, 369))
enemieseses.append(Enemy(1400, 270))
enemieseses.append(Enemy(2000, 182))
enemieseses.append(Enemy(1000, 182))
enemieseses.append(Enemy(2800, 369))
enemieseses.append(Enemy(2800, 120))
enemieseses.append(Enemy(3200, 240))
enemieseses.append(Enemy(4000, 300))
enemieseses.append(Enemy(3700, 369))
enemieseses.append(Enemy(4000, 300))
enemieseses.append(Enemy(3500, 120))
enemieseses.append(Enemy(4200, 120))
enemieseses.append(Enemy(4600, 240))
enemieseses.append(Enemy(4820, 369))
enemieseses.append(Enemy(5200, 270))
enemieseses.append(Enemy(5200, 120))
enemieseses.append(Enemy(5500, 240))
enemieseses.append(Enemy(5900, 300))
enemieseses.append(Enemy(6560, 120))
enemieseses.append(Enemy(6560, 365))
enemieseses.append(Enemy(6400, 240))
