import telebot
import csv

bot = telebot.TeleBot('984177260:AAEVmePjaW52DjM1ZFjLgAMgNSY_nDZErSQ')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('/ok', '/eщё')
def file_reader(file_l):#filereader
    targetmas = []
    reader = csv.DictReader(open('ot.csv'), delimiter = ',')
    for line in reader:
        targetmas.append(line[file_l])
    print(targetmas)
    return(targetmas)
    
    
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здрасвуй я бот рифмоплет, вы вводете слово я выдаю рифму. Если вам подходит вводим "/оk" если нет вводим "/ещё" и я выдаю вам  следующую рифму. Поехали введи слово',reply_markup=keyboard1)

@bot.message_handler(commands=['ok'])
def new_rifme(message):
    bot.send_message(message.chat.id, 'Мне это нравится может поищем рифмы для других слов? Введи слово рифмы для которого ты хочешь найти.')
    
    
@bot.message_handler(content_types=['text'])
def send_text(message,):
    word = []
    pack = []
    control=[]
    for liter in list(message.text.lower()):
        word.append(liter)
        print(word)
    word_revers = word[::-1]
    control= ''.join(word_revers)[0:2]
    pack = file_reader(control[::-1])
    bot.send_message(message.chat.id, str(pack))

bot.polling()
