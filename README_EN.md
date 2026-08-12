<div align="center">

**English** • [Русский](README.md)

</div>

# 🎰 Casino Stars Bot

<p align="center">
  <a href="https://github.com/Mukller">
    <img src="https://img.shields.io/badge/Anton%20Petnitsky-Developer-0d1117?style=for-the-badge&logo=github&logoColor=white&labelColor=0d1117&color=58a6ff" alt="Anton Petnitsky" />
  </a>
</p>


Telegram casino bot for groups with paid messages. Send 🎰, pay 1 star — try to hit the jackpot!

## How It Works

1. Group is configured with **Paid Messages = 1 ⭐** per message
2. A member sends the 🎰 emoji
3. Telegram spins the slot machine (fair randomness from Telegram)
4. Three sevens (`value == 64`) → **winner receives a gift 🎁**
5. Bot announces the win in the group

## Math

| Parameter | Value |
|-----------|-------|
| Spin cost | 1 ⭐ |
| Jackpot chance | 1 / 64 |
| Prize | Gift worth 50 ⭐ |
| Avg. income per cycle | 64 ⭐ |
| Avg. expense per cycle | 50 ⭐ |
| **Profit** | **+14 ⭐ per 64 spins** |

## Quick Start

### 1. Clone and configure

```bash
git clone https://github.com/Mukller/casino-stars-bot.git
cd casino-stars-bot
cp .env.example .env
```

### 2. Get GIFT_ID

```bash
pip install -r requirements.txt
python get_gifts.py
```

Copy the gift ID worth 50 ⭐ and add to `.env`:

```env
BOT_TOKEN=your_bot_token
GIFT_ID=your_gift_id
```

### 3. Run with Docker

```bash
docker-compose up -d
```

## Telegram Group Setup

1. Add the bot to your group as administrator
2. **Group Settings → Monetization → Paid Messages → 1 ⭐**
3. Pin the rules message (example below)

**Pinned message text:**
```
🎰 Casino | 1 message = 1 ⭐
Send 🎰 and try to hit three sevens!
Jackpot = gift 🎁
```

## Stack

- Python 3.11
- [aiogram 3.13](https://docs.aiogram.dev/)
- Docker + docker-compose
- Telegram Stars & Gifts API

## License

MIT © 2026 Anton Mukller
