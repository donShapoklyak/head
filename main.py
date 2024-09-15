import telebot
from telebot import types
import requests

# Replace 'your_api_key' with your actual API key
bot = telebot.TeleBot('7366753393:AAGmK2pf8x8Hw-xOdYevf59V_q9zE2sPaFs')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    webAppTest = types.WebAppInfo("https://donshapoklyak.github.io/head/")
    one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webAppTest)
    keyboard.add(one_butt)
    bot.send_message(message.chat.id, "Hello!", reply_markup=keyboard)
    


@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data
    bot.send_message(message.chat.id, data)

bot.polling()    

"""""
        webAppInfo = types.WebAppInfo(url="https://donshapoklyak.github.io/head/")
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Отправить данные', web_app=webAppInfo))
    
    await message.answer(text='Привет!', reply_markup=builder.as_markup())
"""""