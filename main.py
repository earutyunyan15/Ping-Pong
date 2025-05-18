from pygame import *

window = display.set_mode((700,500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('background.png'), (700,500))
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE', True, (255, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE', True, (255, 0, 0))
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
        if k_p[K_w] and self.rect.y > -5:
            self.rect.y-= self.speed
        if k_p[K_s] and self.rect.y < 380:
            self.rect.y += self.speed
    def update_r(self):
        k_p = key.get_pressed()
        if k_p[K_UP] and self.rect.y > -5:
            self.rect.y-= self.speed
        if k_p[K_DOWN] and self.rect.y < 380:
            self.rect.y += self.speed
    def ball(self):
        self.rect.x+=speed_x
        self.rect.y+=speed_y
r1 = Player('r1.png', 0, 50, 5, 50, 120)
r2 = Player('r2.png', 650, 100, 5, 40, 120)
ball = Player('image_true.png', 250, 350, 5 ,50, 50)

finish = False
game = True

speed_x = 2
speed_y = 2

while game:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        r1.update_l()
        r2.update_r()
        ball.ball()
    ball.reset()
    r2.reset()
    r1.reset()

    if ball.rect.y>450:
        speed_y*=-1
    if ball.rect.y<50:
        speed_y*=-1
    if sprite.collide_rect(r1,ball) or sprite.collide_rect(r2,ball):
        speed_x*=-1
    if ball.rect.x>710:
        window.blit(lose2,(350,250))
        finish = False
    if ball.rect.x<-10:
        window.blit(lose1,(250,350))
        finish = False

    display.update()
