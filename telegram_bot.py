#!usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3
import telebot
from parsers import ParsersForRyhmes
from config import token , admin_id

bot = telebot.TeleBot(token)

def update_language(telegram_id, language):
    """
    Change the user language in the database
    """
    try:
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        cursor.execute(f"UPDATE users SET language = '{language}' WHERE telegram_id = '{str(telegram_id)}'")
        connection.commit()
        connection.close()
    except Exception as e:
        bot_send_error_message_to_admin("update_language",str(e), telegram_id)

def choose_usser_language(telegram_id, language):
    """
    Checks the user's language settings. If the user is not in the database then he / she adds it, saving the language settings according to the client's telegram settings.
    """
    try:
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()

        try:
            language = cursor.execute(f"SELECT language FROM users WHERE telegram_id = '{str(telegram_id)}'").fetchall()[0][0]

        except:
            if language!='uk' or 'en' or 'ru':
                language = 'en'
            cursor.execute(f"INSERT INTO users VALUES (?,?)", (telegram_id, language))
            connection.commit()
            connection.close()
        return language
    except Exception as e:
        bot_send_error_message_to_admin("choose_user_language", str(e), telegram_id)

@bot.message_handler(commands=['start'])
def start_message(message):
    start_message = {'en':"Hello I rhyme bot, you input the any word I output rhyme. Let's enter the word.To select a (language, enter '/language')",
                    'uk':"Привіт я поет-бот, введи слово,  а я знайду до нього рими. Давай введи слово. (Для зміни мови введи '/language') ",
                    'ru':"Здраствуйте я бот рифмоплет, вы вводите слово я выдаю рифмы. Поехали введите слово. (Для выбора языка введи '/language')",
                    'pl':"Cześć, ja jestem rymobotem, wpisz słowo a ja znajde do njego rymy.Dawaj wpiszmy słowo. (Aby wybrać język, wpisz „/language”)",}
    bot.send_message(message.chat.id, start_message[choose_usser_language(message.from_user.id, message.from_user.language_code)])

@bot.message_handler(commands=['language'])#Select language menu
def select_language_menu(message):
    keyboard0 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard0.row('/English','/Українська','/Русский','/Polski')
    bot.send_message(message.chat.id,'select a language', reply_markup=keyboard0)

@bot.message_handler(commands=['English'])
def select_english_language(message):
    update_language(message.from_user.id, 'en')
    start_message(message)

@bot.message_handler(commands=['Українська'])
def select_ukranian_language(message):
    update_language(message.from_user.id, 'uk')
    start_message(message)

@bot.message_handler(commands = ['Русский'])
def select_russian_language(message):
    update_language(message.from_user.id, 'ru')
    start_message(message)

@bot.message_handler(commands = ['Polski'])
def select_polish_language(message):
    update_language(message.from_user.id, 'pl')
    start_message(message)

@bot.message_handler(content_types=['text'])
def analiz_message(message):
    try:
        parser = ParsersForRyhmes(message.text)
        language = choose_usser_language(message.from_user.id, message.from_user.language_code)

        if language == 'uk':
            bot.send_message(message.chat.id, f'Рими до слова {message.text} - {parser.selenium_parser_uk()}')

        elif language == 'ru':
            bot.send_message(message.chat.id, f'Рифмы к слову {message.text} - {parser.selenium_parser_ru()}')

        elif language == 'pl':
            bot.send_message(message.chat.id, f'Rymy do slowa {message.text} - {parser.selenium_parser_pl()}')

        else:
            bot.send_message(message.chat.id, f'{message.text} rhymes - {parser.selenium_parser_en()}')
    except Exception as e:
        bot_send_error_message_to_admin("analiz_message", str(e), message.from_user.id)

def bot_send_error_message_to_admin(function_name, e , telegram_id):
    bot.send_message(admin_id, f"Erro in the {function_name} - {e}")
    error_message = {'en':"Sorry we made a small mistake. The administrator is already working on this. Try repeating your actions, or try others.",
                    'uk':"Вибачте будь-ласка у нас сталася маленька помилка. Адміністратор вже працює над цим. Спробуйте повторити свої дії, або виконати інші. ",
                    'ru':"Простите пожалуйста у нас произошла маленькая ошибка. Администратор уже работает над этим. Попробуйте повторить свои действия, или выполнить другие.",
                    'pl':"Przepraszam, mamy mały błąd. Administrator już nad tym pracuje. Spróbuj powtórzyć swoje działania lub wykonać inne.",}
    bot.send_message(telegram_id, error_message(telegram_id))

if __name__ in "__main__":
    bot.polling(none_stop = True)
