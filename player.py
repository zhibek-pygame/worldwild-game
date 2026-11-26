import pygame

class Player: #создаем класс игрока
    def __init__(self, x, y): #функция которая запускается автоматически при создании персонажа
        player = Player(100, 410)
        self.width = 45
        self.height = 70 #размер персонажа

        self.rect = pygame.Rect(x, y, self.width, self.height) #создаёт прямоугольную область, которая представляет персонажа.

        self.speed = 5

        self.velocity_y = 0 #вертикальная скорость
        self.gravity = 0.7 #сила притяжения вниз
        self.jump_power = -14 #начальная скорость прыжка. Она отрицательна, потому что в пигейме У увеличивается вниз, поэтому отриц скорость поднимает перса вверх

    def update(self, keys, ground_y):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: #управления
            self.rect.x -= self.speed #Если нажата стрелка влево или A, персонаж движется влево
            


        


