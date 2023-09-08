from pygame import*
init()

W = 800
H = 500

back = (0, 255, 120)
window = display.set_mode((W, H))
display.set_icon(image.load("tenis_ball.png"))
display.set_caption("pp by r1ze")

game = True
finish = False

class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) # створюємо картинку
        self.size_x = size_x
        self.size_y = size_y
        self.speed = player_speed
        self.rect = self.image.get_rect() # повертає прямокутник під картинкою
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < H - self.size_y:
            self.rect.y += self.speed
         
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < H - self.size_y:
            self.rect.y += self.speed


racket1 = Player('racket.png', 10, W/3, 50, 150, 5)
racket2 = Player('racket.png', 740, W/3, 50, 150, 5)
ball = GameSprite('tenis_ball.png', W/2, H/2, 50, 50, 4)

speed_x, speed_y = 4, 4
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        time.delay(10)
        racket1.reset()
        racket1.update_l()
        racket2.reset()
        racket2.update_r()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y < 0 or ball.rect.y > H-50:
            speed_y *= -1

    display.update()

    