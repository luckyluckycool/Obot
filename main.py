#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt

# Объект бота
bot = Bot(token="")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

backButtons = ["Назад", "На початок"]


# START
@dp.message_handler(commands="start")
async def loginHandler(message: types.Message):
    await message.answer(
        f"СКОБ, {message.from_user.full_name}!\n\nЯ пластовий бот Львівської Округи.")
    await startHandler(message)


@dp.message_handler(text="На початок")
async def startHandler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["УПЮ", "УСП/УПС"]
    keyboard.add(*buttons)
    start_button = "Долучитися до Пласту"
    keyboard.add(start_button)

    await message.answer("Чим я можу тобі допомогти?", reply_markup=keyboard)


# УПЮ
@dp.message_handler(text="УПЮ")
async def uspHandler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("")
    keyboard.add(*backButtons)
    await message.answer("Дай боже)", reply_markup=keyboard)


# УСП/УПС
@dp.message_handler(text="УСП/УПС")
async def uspHandler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Як стати ДЧ?")
    keyboard.add(*backButtons)
    await message.answer("Що саме ти хочеш дізнатися?", reply_markup=keyboard)


# УСП/УПС відповіді
@dp.message_handler(text="Як стати ДЧ?")
async def howToDCH(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*backButtons)
    await message.answer('Для цього зареєструйся на [EPlast](https://plast.sitegist.net/uk/system/register/)',
                         parse_mode='Markdown', reply_markup=keyboard)


# Долучитися до Пласту
@dp.message_handler(text="Долучитися до Пласту")
async def joinPlastHandler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ageButtons = ["6-10", "11-17", "18+"]
    keyboard.add(*ageButtons)
    keyboard.add(*backButtons)
    await message.answer("Скільки тобі років?", reply_markup=keyboard)

    @dp.message_handler(text="6-10")
    async def joinUPNHandler(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*backButtons)
        await message.answer("Тобі в улад пластунів новаків!", reply_markup=keyboard)

    @dp.message_handler(text="11-17")
    async def joinUPUHandler(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*backButtons)
        await message.answer("Тобі в улад пластунів юнаків!", reply_markup=keyboard)

    @dp.message_handler(text="18+")
    async def joinDCHHandler(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*backButtons)
        await message.answer("Тобі в улад старшопластнуів або пластунів-сеньйорів!", reply_markup=keyboard)



# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
