import keyboards
import config_bot
import rates
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.types.message import ContentType

router = Router()

@router.message(CommandStart())
async def start(message: Message):
	await message.answer_photo(photo=config_bot.START_PHOTO, caption=config_bot.START_MSG, reply_markup=keyboards.start)

@router.callback_query(F.data == "rates")
async def rates_wait(callback: CallbackQuery):
	await callback.answer("")
	await callback.message.answer("Выберите Криптовалюту (например: BTC)", reply_markup=keyboards.rate_wait)

@router.message()
async def echo(message: Message):
	print(f"{message.from_user.username} : {message.text}")
	msg = message.text.lower()
	await message.answer(rates.rates(msg.upper()))
