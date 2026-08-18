import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")


async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.new_chat_members:
        return

    for user in update.message.new_chat_members:
        name = user.first_name or "Friend"

        if user.username:
            mention = f"@{user.username}"
        else:
            mention = name

        welcome_text = (
            f"🎉 <b>Welcome to the Group!</b> 🎉\n\n"
            f"👤 Welcome {mention}!\n"
            f"💙 আমরা তোমাকে আমাদের গ্রুপে পেয়ে আনন্দিত।\n\n"
            f"📜 <b>Group Rules:</b>\n"
            f"• সবাইকে সম্মান করুন 🤝\n"
            f"• Spam করবেন না 🚫\n"
            f"• অপ্রয়োজনীয় Link শেয়ার করবেন না 🔗\n\n"
            f"🔥 <b>Enjoy the Group!</b> ❤️"
        )

        await update.message.reply_text(
            welcome_text,
            parse_mode="HTML"
        )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 <b>Welcome Bot is Online!</b>\n\n"
        "আমি Group-এর নতুন Member-দের Welcome করব। ❤️",
        parse_mode="HTML"
    )


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN is missing!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome)
    )

    app.add_handler(
        MessageHandler(filters.COMMAND, start)
    )

    print("🤖 Welcome Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
