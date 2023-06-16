from fpdf import  FPDF
from  datetime import datetime


pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()

pdf.image('bg.jpg', h=297, x=0, y=0)

pdf.add_font('courier', '', 'C:\WINDOWS\FONTS\COUR.ttf', uni=True)
pdf.set_font('courier', size=35)

friend_name = input('Введите имя друга: ')

pdf.cell(0, 95, ln=1)
pdf.cell(0, 20, txt='Дорогой, ' + friend_name + '!', align='C', ln=1)

pdf.set_font('courier', size=18)
pdf.set_right_margin(50)
pdf.set_left_margin(50)

message = input('Ваши поздравления: ')

pdf.multi_cell(0, 20, txt=message, align='C')

pdf.set_text_color(124, 94, 147)

today = datetime.today().strftime('%d.%.%Y')
pdf.cell(0, 20, txt=today, align='R', ln=1)

author_name = input('Введите ваше имя: ')
pdf.cell(0, 20, txt=author_name, align='R', ln=1)

pdf.output('bday_card.pdf')


