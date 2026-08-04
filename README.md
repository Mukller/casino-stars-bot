<div align="center">

[English](README_EN.md) • **Русский**

</div>

# 🎰 Casino Stars Bot

<p align="center">
  <a href="https://github.com/Mukller">
    <img src="https://img.shields.io/badge/Anton%20Petnitsky-Developer-0d1117?style=for-the-badge&logo=github&logoColor=white&labelColor=0d1117&color=58a6ff" alt="Anton Petnitsky" />
  </a>
</p>


Telegram-бот казино для групп с платными сообщениями. Отправь 🎰, заплати 1 звезду — и попробуй поймать джекпот!

## Как работает

1. Группа настроена на **Paid Messages = 1 ⭐** за сообщение
2. Участник отправляет эмодзи 🎰
3. Telegram крутит слот-машину (честный рандом от Telegram)
4. Три семёрки (`value == 64`) → **победитель получает подарок 🎁**
5. Бот объявляет победу в группе

## Математика

| Параметр | Значение |
|----------|----------|
| Цена спина | 1 ⭐ |
| Шанс джекпота | 1 / 64 |
| Приз | Подарок 50 ⭐ |
| Средний доход за цикл | 64 ⭐ |
| Средний расход за цикл | 50 ⭐ |
| **Профит** | **+14 ⭐ на 64 спина** |

## Быстрый старт

### 1. Клонировать и настроить

```bash
git clone https://github.com/Mukller/casino-stars-bot.git
cd casino-stars-bot
cp .env.example .env
```

### 2. Получить GIFT_ID

```bash
pip install -r requirements.txt
python get_gifts.py
```

Скопируй ID подарка за 50 ⭐ и вставь в `.env`:

```env
BOT_TOKEN=your_bot_token
GIFT_ID=your_gift_id
```

### 3. Запустить через Docker

```bash
docker-compose up -d
```

## Настройка группы в Telegram

1. Добавь бота в группу как администратора
2. **Настройки группы → Монетизация → Платные сообщения → 1 ⭐**
3. Закрепи правила (пример ниже)

**Текст закреплённого сообщения:**
```
🎰 Казино | 1 сообщение = 1 ⭐
Отправь 🎰 и попробуй поймать три семёрки!
Джекпот = подарок 🎁
```

## Стек

- Python 3.11
- [aiogram 3.13](https://docs.aiogram.dev/)
- Docker + docker-compose
- Telegram Stars & Gifts API

## Лицензия

MIT © 2026 Anton Mukller
