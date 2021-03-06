##Здесь мы импортируем библиотеки

import telebot
from telebot import types

###Здесь токен бота
client = telebot.TeleBot("1678001294:AAEFFsRue9o2isVOMHSzWPFpSLMwcVMgQDE")

#Заносим комманды для запуска 
@client.message_handler(commands = ['get_info', 'info', 'start'])
##Здесь прописываем инлайновую клаву в этой функции
def get_answer(message):
	markup_inline = types.InlineKeyboardMarkup()
	item_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'yes')
	item_no = types.InlineKeyboardButton(text = 'нет', callback_data = 'no')
	markup_inline.add(item_yes, item_no)
	client.send_message(message.chat.id, 'Ты любишь питон?',
		reply_markup = markup_inline
		)
# Не знаю что за функция но она обязательно нужна
@client.callback_query_handler(func=lambda call: True)
#Заносим реплай клаву
def answer(call):
    if call.data == 'yes':
    	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
    	item_an = types.KeyboardButton('Отлично')
    	item_un = types.KeyboardButton('Мой ник')

    	markup_reply.add(item_an, item_un)
    	client.send_message(call.message.chat.id, 'Нажмите на одну из кнопок',
    		reply_markup = markup_reply)
#И просто выводим сообщения после сробатывания кнопок
@client.message_handler(content_types = ['text'])
def get_text(message):
    if message.text == 'Отлично':
       client.send_message(message.chat.id, f'Ну вот и хорошо')
    elif message.text == 'Мой ник':
       client.send_message(message.chat.id, f'Твой ник: {message.from_user.first_name}{message.from_user.last_name}')
client.polling(none_stop = True, interval = 0)



