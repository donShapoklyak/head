import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, InlineKeyboardBuilder
from aiogram import F
import requests
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
    markup.add(types.KeyboardButton(text="да!", width=1))
    markup = markup.as_markup() 
    await message.answer(text=f"привет! {username} хотите оформить заказ?", reply_markup=markup)
 
@dp.message(lambda message: 'да!' in message.text.lower())
async def cmd_random(message: types.Message):
    webAppInfo = types.WebAppInfo(url="https://donshapoklyak.github.io/head/")
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='собрать пк', web_app=webAppInfo))
    
    await message.answer(text="отлично предлагаю воспользоваться нашим конструктором для сборки пк", reply_markup=builder.as_markup())
def get_data_from_web_app():
    response = requests.get('https://example.com/api/endpoint')
    data = response.json()
    return data
@dp.message(~F.message.via_bot) 
async def web_app2(message: types.Message): 
    print(message.web_app_data) await message.answer("test")

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