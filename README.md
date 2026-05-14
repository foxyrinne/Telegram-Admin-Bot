# Telegram Admin Bot

A lightweight Telegram moderation bot built with `aiogram`. The bot adds group protection features like link deletion, media moderation, admin-only night mode, and rate limiting.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![aiogram](https://img.shields.io/badge/aiogram-v3.0%2B-blue?style=for-the-badge&logo=telegram)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 🛠️ Tech Stack

- **aiogram** — asynchronous Telegram Bot API framework
- **python-dotenv** — environment variable management

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/telegram-admin-bot.git
cd telegram-admin-bot
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install aiogram python-dotenv
```

### 4. Configure environment variables

Create a `.env` file in the project root or copy from `.env.example`:

```env
TOKEN=your_telegram_bot_token_here
```

> 💡 **How to get a token?**
> 1. Open Telegram and search for **@BotFather**
> 2. Send `/newbot`
> 3. Follow the instructions and copy the token

### 5. Run the bot

```bash
python main.py
```

## 📱 Usage

1. Add the bot to your group chat
2. Grant the bot permissions to delete messages
3. Use `/night_mode on` or `/night_mode off` as an admin
4. The bot will delete links and media from non-admin users automatically

## 🏗️ Project Structure

```text
telegram-admin-bot/
├── handlers/
│   └── routes.py        # Message handlers and moderation rules
├── middleware/
│   └── rate_limit.py    # Simple rate limiting middleware
├── .env.example         # Example environment variables
├── .gitignore           # Git ignore rules
├── main.py              # Main bot file
└── requirements.txt     # Project dependencies
```

## 📖 Documentation

- [aiogram Documentation](https://docs.aiogram.dev/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [python-dotenv](https://saurabh-kumar.com/python-dotenv/)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
