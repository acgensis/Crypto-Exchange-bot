from aiogram.types import (
	InlineKeyboardMarkup,
	InlineKeyboardButton,
	ReplyKeyboardMarkup,
	KeyboardButton
)

start = InlineKeyboardMarkup(
	inline_keyboard=[
		[InlineKeyboardButton(text="Курс", callback_data="rates")],
		[InlineKeyboardButton(text="Исходный код", url="https://github.com/acgensis/Crypto-Exchange-bot")]
	]
)
rate_wait = ReplyKeyboardMarkup(
	keyboard=[
		[KeyboardButton(text="BTC"), KeyboardButton(text="ETH")],
		[KeyboardButton(text="XRP"), KeyboardButton(text="SOL")],
		[KeyboardButton(text="TRX"), KeyboardButton(text="TON")],
		[KeyboardButton(text="BNB"), KeyboardButton(text="ARB")]
	],
	resize_keyboard = True,
	one_time_keyboard = True,
	input_field_placeholder = "Выберите Криптовалюту..."
)