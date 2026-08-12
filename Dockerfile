FROM python:3.11-slim

RUN useradd -m -u 1000 appuser

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py .
RUN chown -R appuser:appuser /app

USER appuser

CMD ["python", "bot.py"]

# Author: Anton Petnitsky
# GitHub: https://github.com/Mukller/casino-stars-bot
# Last modified: 2026-07-30 21:52:10 +0300
