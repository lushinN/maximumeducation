from tkinter import *
import time

class Ball:
    def __init__(self, canvas, color, platform):
        self.canvas = canvas
        self.touch_bottom = False
        self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.x = 3
        self.y = 3
        self.platform = platform

    def touch_platform(self, ball_pos):
        platform_pos = self.canvas.coords(self.platform.rect)
        if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
            if ball_pos[3] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
                return True
        return False


    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        pos = self.canvas.coords(self.oval) # Список с коор-ми круга [x0, y0, x1, y1]
        if pos[3] >= 400:
            self.touch_bottom = True
        if pos[1] <= 0:
            self.y = 3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= 500:
            self.x = -3

        if self.touch_platform(pos) == True:
            self.y = -3

class Platform:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

    def left(self, event):
        self.x = -2
        print(self.x)

    def right(self, event):
        self.x = 2

    def draw(self):
        self.canvas.move(self.rect, self.x, 0)
        pos = self.canvas.coords(self.rect)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= 500:
            self.x = 0

window = Tk()
window.title('Аркада')
window.resizable(width=False, height=False)
window.wm_attributes('-topmost', 1) # Открытие приложения поверх всех окон

canvas = Canvas(window, width=500, height=400)
canvas.pack()

platform = Platform(canvas, 'green')
ball = Ball(canvas, 'red', platform)


while True:
    if ball.touch_bottom == False:
        ball.draw()
        platform.draw()
    else:
        break #Закрытие окна - конец игры
    window.update()
    time.sleep(0.01)