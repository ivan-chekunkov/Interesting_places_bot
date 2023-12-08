from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F

import secret

BOT_TOKEN = secret.BOT_TOKEN
# API_CATS_URL = "https://api.thecatapi.com/v1/images/search"
# ERROR_TEXT = "Здесь должна была быть картинка с котиком :("

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь")


@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(
        "Напиши мне что-нибудь и в ответ " "я пришлю тебе твое сообщение"
    )


@dp.message()
async def send_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text="Данный тип апдейтов не поддерживается " "методом send_copy"
        )


if __name__ == "__main__":
    dp.run_polling(bot)
