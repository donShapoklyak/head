import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup
global obj
global city

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7366753393:AAGmK2pf8x8Hw-xOdYevf59V_q9zE2sPaFs")

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user = message.from_user
    username = user.first_name
    markup = ReplyKeyboardBuilder()
    markup.add(types.KeyboardButton(text="начать поиск 🔎"))
    markup = markup.as_markup() 
    await message.answer(text=f"привет! {username} начнем?", reply_markup=markup)
 
@dp.message(lambda message: 'начать поиск 🔎' in message.text.lower())
async def cmd_random(message: types.Message):
    await message.answer(text="что будем искать ❓")
    obj = message.text
    print(obj)
    
    
 

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 




"""""
        webAppInfo = types.WebAppInfo(url="https://donshapoklyak.github.io/head/")
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Отправить данные', web_app=webAppInfo))
    
    await message.answer(text='Привет!', reply_markup=builder.as_markup())
"""""