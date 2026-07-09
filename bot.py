import asyncio
import logging
import os
from datetime import datetime

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

TOKEN = os.getenv("BOT_TOKEN")
GIFT_ID = os.getenv("GIFT_ID", "")
LOG_FILE = "winners.log"
JACKPOT = 64
SLOT = "🎰"

bot = Bot(token=TOKEN)
dp = Dispatcher()


def log_winner(user_id: int, username: str) -> None:
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{ts} | id:{user_id} | @{username}\n")


@dp.message(F.dice.emoji == SLOT)
async def handle_spin(message: Message) -> None:
    if message.dice.value != JACKPOT:
        return

    user = message.from_user
    name = f"@{user.username}" if user.username else user.first_name

    try:
        await bot.send_gift(user_id=user.id, gift_id=GIFT_ID)
        await message.answer(f"🎰 JACKPOT! {name} выиграл подарок! 🎁")
        log_winner(user.id, user.username or str(user.id))
        logging.info(f"Gift sent to {user.id} ({name})")
    except Exception as e:
        logging.error(f"Failed to send gift to {user.id}: {e}")


@dp.message()
async def handle_other(message: Message) -> None:
    if not message.from_user or message.from_user.is_bot:
        return
    await message.reply("Отправь 🎰 чтобы сыграть! (стоит 1 ⭐)")


async def main() -> None:
    logging.info("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
