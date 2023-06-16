#Игра в рыцаря и дракончиков с полным управлением по осям х и y
import random
from tkinter import *
window = Tk()

w = 600
h = 600
window.geometry(str(w) + 'x' + str(h))

canvas = Canvas(window, width=w, height=h)
canvas.place(in_=window, x=0, y=0)

bg_photo = PhotoImage(file='bg_2.png')

class Knight:
    def __init__(self):
        self.x = 150
        self.y = h//2
        self.yv = 0
        self.xv = 0
        self.photo = PhotoImage(file='knight.png')

    def up(self, event):
        self.yv = -5


    # Движение вниз
    def down(self, event):
        self.yv = 5


    # Остановка
    def stop(self, event):
        self.yv = 0
        self.xv = 0

    def right(self, event):
        self.xv = 5

    def left(self, event):
        self.xv = -5

class Dragon:
    def __init__(self):
        self.x = 750
        self.y = random.randint(100, 500)
        self.v = random.randint(1, 3)
        self.photo = PhotoImage(file='dragon.png')

knight = Knight()

dragons = []
for i in range(3):
    dragons.append(Dragon())


def game():
    canvas.delete('all')
    canvas.create_image(300, 300, image=bg_photo)
    canvas.create_image(knight.x, knight.y, image=knight.photo)
    knight.y += knight.yv
    knight.x += knight.xv
    if knight.y < 50:
        knight.y = 51
    elif knight.y > 565:
        knight.y = 564

    current_dragon = 0

    dragon_to_kill = -1

    for dragon in dragons:
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
        dragon.x -= dragon.v

        if ((dragon.x - knight.x) ** 2) + ((dragon.y - knight.y) ** 2) <= (96) ** 2:
            dragon_to_kill = current_dragon

        current_dragon += 1

        if dragon.x <= 0:
            canvas.delete('all')
            canvas.create_text(w // 2, h // 2, text="You lose!", font="Verdana 42", fill='red')
            break

    if dragon_to_kill >= 0:
        del dragons[dragon_to_kill]

    if len(dragons) == 0:
        canvas.delete('all')
        canvas.create_text(w // 2, h // 2, text="You win!", font="Verdana 42", fill='green')
    else:
        window.after(5, game)


game()

window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)
window.bind('<Key-Right>', knight.right)
window.bind('<Key-Left>', knight.left)

window.mainloop()

