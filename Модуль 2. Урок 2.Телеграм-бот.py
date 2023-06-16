import telebot
import random


token = '5925024191:AAGricm1h0xSnkMWZiAlbi__UudvJ5HscfQ' # СЮДА СВОЙ ТОКЕН API ИЗ ТГ!
bot = telebot.TeleBot(token) #TeleBot - обязательно в написании


@bot.message_handler(commands=['start', 'help']) #commands- это те команды которые будет телеграм-бот принимать
def send_welcome(message):
    welcome_text = """
    Привет! Я умею рассказывать стихи, знаю много интересных фактов и могу показать милых котиков!
    """
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)#resize_keyboard - расстягивает клавиатуру
    button1 = telebot.types.KeyboardButton('Стихотворение')
    button2 = telebot.types.KeyboardButton('Факт')
    button3 = telebot.types.KeyboardButton('Котик')
    keyboard.add(button1, button2, button3) # здесь мы привязали кнопки к каркасу
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворенье..."
    bot.send_message(message.chat.id, poem_text)

    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_url = telebot.types.InlineKeyboardButton('Перейти', url='https://stihi.ru/')
    keyboard.add(button_url)
    bot.send_message(message.chat.id, 'Больше стихов по ссылке ниже!', reply_markup=keyboard)

@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = str(random.randint(1,9))
    cat_img = open('img/' + cat_number + '.jpg', 'rb') #img - название папки с картинками, rb - формат открытия картинки
    bot.send_photo(message.chat.id, cat_img)

@bot.message_handler(commands_types = ['text'])
def answer(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Дарова!')
    elif message.text == 'Cтихотворение':
       send_poem(message)
    elif message.text == 'Котик':
          send_cat(message)

bot.polling()