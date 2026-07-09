import asyncio
import logging
import os
from datetime import datetime

from aiogram import Bot, Dispatcher, F
from aiogram.types import LabeledPrice, Message, PreCheckoutQuery
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


@dp.message(F.text == "/spin")
async def cmd_spin(message: Message) -> None:
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="🎰 Казино",
        description="Крутани слот-машину! Три семёрки = подарок 🎁",
        payload=f"spin_{message.from_user.id}",
        currency="XTR",
        prices=[LabeledPrice(label="1 спин", amount=1)],
    )


@dp.pre_checkout_query()
async def pre_checkout(query: PreCheckoutQuery) -> None:
    await query.answer(ok=True)


@dp.message(F.successful_payment)
async def handle_payment(message: Message) -> None:
    dice_msg = await message.answer_dice(emoji=SLOT)
    # ждём анимацию слот-машины
    await asyncio.sleep(3)

    value = dice_msg.dice.value
    user = message.from_user
    name = f"@{user.username}" if user.username else user.first_name

    if value == JACKPOT:
        try:
            await bot.send_gift(user_id=user.id, gift_id=GIFT_ID)
            await message.answer(f"🎰 JACKPOT! {name} выиграл подарок! 🎁")
            log_winner(user.id, user.username or str(user.id))
            logging.info(f"Gift sent to {user.id} ({name})")
        except Exception as e:
            logging.error(f"Failed to send gift to {user.id}: {e}")
    else:
        await message.answer(f"😢 Не повезло, {name}! Попробуй снова — /spin")


@dp.message()
async def handle_other(message: Message) -> None:
    if not message.from_user or message.from_user.is_bot:
        return
    await message.reply("Напиши /spin чтобы сыграть! (стоит 1 ⭐)")


async def main() -> None:
    logging.info("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
