import asyncio
import handlers
import config_bot
from aiogram  import Bot, Dispatcher

async def main():
	bot = Bot(config_bot.TOKEN)
	dp = Dispatcher()
	dp.include_routers(
		handlers.router,
	)
	await dp.start_polling(bot)

if __name__ == '__main__':
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print("EXIT")