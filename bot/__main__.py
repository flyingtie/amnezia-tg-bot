import asyncio
import logging

from loader import dp, bot


async def main():
    await dp.start_polling(bot, dp.resolve_used_update_types())    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())