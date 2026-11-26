import pygame

class Camera: #создаем класс камеры, который будет отвечать за то что мы видим на экране
    def __init__(self, width, height): #настройка камеры при запуске 
        self.width = width #запоминаем ширину экрана
        self.height = height #запоминаем высоту экрана
        self.camera = pygame.Rect(0, 0, width, height) #создаем прямоугольник для хранение сдвига камеры, в скобках координаты и размеры прямоугольника


    def update(self, target): #функция слежки за игроком (target - объект, за которым следует камера)
        x = -target.rect.centrex + self.width//2 #считаем сдвиг по горизонтали в центр
        y = -target.rect.centery + self.height//2 #считаем сдвиг по вертикали в центр
        self.camera = pygame.Rect(x, y, self.width, self.height) #обновляем позицию камеры


    def apply(self, entity): #функция сдига любого объекта на экране
        return entity.rect.move(self.camera.topleft) #сдвигаем обЪект на величину камеры