"""Run once to find available gift IDs, then set GIFT_ID in .env"""
import os
import urllib.request
import json

token = os.getenv("BOT_TOKEN") or open(".env").read().split("BOT_TOKEN=")[1].split("\n")[0].strip()
url = f"https://api.telegram.org/bot{token}/getAvailableGifts"

with urllib.request.urlopen(url) as r:
    data = json.load(r)

if not data.get("ok"):
    print("Error:", data)
    exit(1)

print(f"{'ID':<25} {'Stars':>6}  {'Stock':>8}")
print("-" * 44)
for g in data["result"]["gifts"]:
    stock = str(g.get("remaining_count", "inf"))
    print(f"{g['id']:<25} {g['star_count']:>6}  {stock:>8}")
