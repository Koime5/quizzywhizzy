# File: quizzy_whizzy_bot.py
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Load answers from JSON file
def load_answers():
    with open("answers.json", "r") as file:
        return json.load(file)

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Zoo", callback_data='zoo')],
        [InlineKeyboardButton("Hrum", callback_data='hrum')],
        [InlineKeyboardButton("Time Farm", callback_data='timefarm')],
        [InlineKeyboardButton("Join Our Channel", url="https://t.me/quizzywhizzy")],  # Replace with your channel link
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    welcome_message = (
        "Welcome to Quizzy Whizzy!\n\n"
        "This bot helps you find answers to daily quiz and riddle challenges from Telegram mining bots.\n\n"
        "Click on any button below to see today's answers.\n\n"
        "For request and check for features, Join our telegram channel."
    )
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

# Help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "💡 **Quizzy Whizzy Help** 💡\n\n"
        "1️⃣ Use /start to see the main menu with options for daily answers.\n"
        "2️⃣ Click on buttons (Zoo, Hrum, Time Farm) to get today's answers.\n"
        "3️⃣ Use these commands to directly get answers:\n"
        "   - `/zoo`: See today's Zoo answers.\n"
        "   - `/hrum`: See today's Hrum answers.\n"
        "   - `/timefarm`: See today's Time Farm answers.\n\n"
        "🔗 [Join Our Channel](https://t.me/quizzywhizzy) for more updates and announcements!"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

# Callback query handler for buttons
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    option = query.data

    answers = load_answers()
    date = answers["date"]

    links = {
        "zoo": "t.me/zoo_story_bot/game?startapp=ref1801127297",  # Replace with the actual Zoo link
        "hrum": "t.me/hrummebot/game?startapp=ref1801127297",  # Replace with the actual Hrum link
        "timefarm": "https://t.me/TimeFarmCryptoBot?start=1xsyOvcuKsblc9aiz"  # Replace with the actual Time Farm link
    }
    if  option == "zoo":
        riddle = answers["zoo"]["riddle"]
        rubus = answers["zoo"]["rubus"]
        response = (
            f"**Date:** {date}\n\n"
            f"**Riddle:**\n{riddle['question']}\n**Answer:** {riddle['answer']}\n\n"
            f"**Rubus:**\n{rubus['question']}\n**Answer:** {rubus['answer']}\n\n"
            f"[Tap here to play Zoo]({links['zoo']})"
        )
    else:
        question = answers[option]["question"]
        answer = answers[option]["answer"]
        response = (
            f"**Date:** {date}\n\n"
            f"**Question:** {question}\n**Answer:** {answer}\n\n"
            f"[Tap here to play {option.capitalize()}]({links[option]})"
        )

    await query.message.reply_text(response, parse_mode="Markdown")


# Command handlers for /zoo, /hrum, /timefarm
async def zoo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    answers = load_answers()
    riddle = answers["zoo"]["riddle"]
    rubus = answers["zoo"]["rubus"]
    date = answers["date"]
    link = "t.me/zoo_story_bot/game?startapp=ref1801127297"  # Replace with the actual Zoo link
    response = (
        f"**Date:** {date}\n\n"
        f"**Riddle:**\n{riddle['question']}\n**Answer:** {riddle['answer']}\n\n"
        f"**Rubus:**\n{rubus['question']}\n**Answer:** {rubus['answer']}\n\n"
        f"[Tap here to play Zoo]({link})"
    )
    await update.message.reply_text(response, parse_mode="Markdown")

async def hrum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    answers = load_answers()
    question = answers["hrum"]["question"]
    answer = answers["hrum"]["answer"]
    date = answers["date"]
    link = "t.me/hrummebot/game?startapp=ref1801127297"  # Replace with the actual Hrum link
    response = (
        f"**Date:** {date}\n\n"
        f"**Question:** {question}\n**Answer:** {answer}\n\n"
        f"[Tap here to play Hrum]({link})"
    )
    await update.message.reply_text(response, parse_mode="Markdown")

async def timefarm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    answers = load_answers()
    question = answers["timefarm"]["question"]
    answer = answers["timefarm"]["answer"]
    date = answers["date"]
    link = "https://t.me/TimeFarmCryptoBot?start=1xsyOvcuKsblc9aiz"  # Replace with the actual Time Farm link
    response = (
        f"**Date:** {date}\n\n"
        f"**Question:** {question}\n**Answer:** {answer}\n\n"
        f"[Tap here to play Time Farm]({link})"
    )
    await update.message.reply_text(response, parse_mode="Markdown")

# Main function to set up the bot
def main():
    TOKEN = "7858543961:AAE07rDw_0HZx2ZskZ6c0y1qWbqpF344y4c"  # Replace with your bot token
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(CommandHandler("zoo", zoo))
    app.add_handler(CommandHandler("hrum", hrum))
    app.add_handler(CommandHandler("timefarm", timefarm))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()