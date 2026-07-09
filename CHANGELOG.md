# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-07-09

### Added
- Slot machine handler for 🎰 Telegram Dice
- Jackpot detection (dice.value == 64)
- Gift payout via Telegram sendGift API
- Public win announcement in group
- Hint reply for non-🎰 messages
- Winner logging to winners.log
- Docker + docker-compose deployment
- get_gifts.py utility to discover available gift IDs
