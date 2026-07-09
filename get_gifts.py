"""Run once to find available gift IDs, then set GIFT_ID in .env"""
import asyncio
import os

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()


async def main() -> None:
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    gifts = await bot.get_available_gifts()
    print(f"{'ID':<20} {'Stars':>6} {'Stock':>8}")
    print("-" * 38)
    for g in gifts.gifts:
        stock = g.remaining_count if g.remaining_count is not None else "∞"
        print(f"{g.id:<20} {g.star_count:>6} {str(stock):>8}")
    await bot.session.close()


asyncio.run(main())
