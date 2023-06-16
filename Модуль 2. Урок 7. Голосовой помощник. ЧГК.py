#Голосовой помощник
import pyaudio
import speech_recognition as sr
import os
import pyttsx3
import random
import webbrowser

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say('Привет, я Джарвис')
voice.runAndWait()
greeings_list = ['Привет','Дароу','Как жизнь?','Здравствуй','Олё','Вечер в хату']
film_list = ['Шрек навсегда', 'Need for Speed', 'В поисках Дори']

while True:
    with sr.Microphone(device_index=1) as sourse:
        print('Скажите что-нибудь сейчас ...')
        audio = r.listen(sourse)

    speech = r.recognize_google(audio, language='ru_RU').lower()
    print('Вы сказали: '+ speech)

    if speech.find('привет') >=0 or speech.find('даров') >=0 or speech.find('здравствуй') >=0:
        voice.say(random.choice(greeings_list))
        voice.runAndWait()
#открыть сайт
    elif speech.find('ютуб')>=0:
        webbrowser.open_new('https://www.youtube.com/')
        voice.say('Ютуб запущен')
        voice.runAndWait()
#открыть файл
    elif speech.find('файл')>=0:
        os.startfile('C:\lesson7.py')
        voice.say('Файл открыт')
        voice.runAndWait()
    elif speech.find('фильм') >=0:
        voice.say(random.choice(film_list))
        voice.runAndWait()
    elif speech.find('пока')>=0:
        voice.say('До встречи')
        voice.runAndWait()
        break
    else:
        voice.say('Я вас не понимаю')
        voice.runAndWait()
