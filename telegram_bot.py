import telebot
from keyboards import KeyboardsForBot
from bot_message import TextMessageClass
from parsers import ParsersForRyhmes

bot = telebot.TeleBot('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx')

class TelegramBot():
    language={}#Dictionary id:language
    userID=[]#Ussers list
    @bot.message_handler(commands=['start'])# /start
    def start_message(message):
        usser=False
        for us in TelegramBot.userID:
            if message.from_user.id==us:#if usser in list
                usser=True#...usser true
        if usser == False:#If usser false...
            TelegramBot.language[message.from_user.id]=message.from_user.language_code#Add usser to language dictionary(language auto select according to client setting)
            TelegramBot.userID.append(message.from_user.id)#Add usser to usser list
        print(TelegramBot.language[message.from_user.id],TelegramBot.userID,TelegramBot.language)
        bot.send_message(message.chat.id, TextMessageClass.start_message[TelegramBot.language[message.from_user.id]])
        
    @bot.message_handler(commands=['language'])#Select language menu
    def select_language_menu(message):
        bot.send_message(message.chat.id,'select a language', reply_markup=KeyboardsForBot.keyboard0)
        
    @bot.message_handler(commands=['English'])
    def select_english_language(message):
        TelegramBot.language[message.from_user.id]='en'
        TelegramBot.start_message(message)
        
    @bot.message_handler(commands=['Українська'])
    def select_ukranian_language(message):
        TelegramBot.language[message.from_user.id]='uk'
        TelegramBot.start_message(message)
        
    @bot.message_handler(commands = ['Русский'])
    def select_russian_language(message):
        TelegramBot.language[message.from_user.id]='ru'
        TelegramBot.start_message(message)
        
    @bot.message_handler(commands = ['Polski'])
    def select_polish_language(message):
        TelegramBot.language[message.from_user.id] ='pl'
        TelegramBot.start_message(message)
            
    @bot.message_handler(content_types=['text'])
    def analiz_message(message):
        tb=TelegramBot
        
        
        if tb.language[message.from_user.id] == 'uk':
            bot.send_message(message.chat.id, f'Рими до слова {message.text} - {ParsersForRyhmes.selenium_parser_uk(message.text)}')
        
        if tb.language[message.from_user.id] == 'ru':
            bot.send_message(message.chat.id, f'Рифмы к слову {message.text} - {ParsersForRyhmes.selenium_parser_ru(message.text)}')
        
        if tb.language[message.from_user.id] == 'pl':
            bot.send_message(message.chat.id, f'Rymy do slowa {message.text} - {ParsersForRyhmes.selenium_parser_pl(message.text)}')
        
        if tb.language[message.from_user.id] == 'en':
            bot.send_message(message.chat.id, f'{message.text} rhymes - {ParsersForRyhmes.selenium_parser_en(message.text)}')
        
bot.polling()
