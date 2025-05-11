from pygame import *

window = display.set_mode((700,500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('background.png'), (700,500))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update_l(self):
        k_p = key.get_pressed()
        if k_p[K_w] and self.rect.y > -80:
            self.rect.y-= self.speed
        if k_p[K_s] and self.rect.y < 300:
            self.rect.y += self.speed
    def update_r(self):
        k_p = key.get_pressed()
        if k_p[K_UP] and self.rect.y > -80:
            self.rect.y-= self.speed
        if k_p[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed  

r1 = Player('New Piskel 5.png', -81, 100, 10, 250, 250)
r2 = Player('New Piskel.png', 530, 100, 10, 250, 250)
finish = False
game = True
while game:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        r1.reset()
        r1.update_l()
        r2.reset()
        r2.update_r()

    display.update()
