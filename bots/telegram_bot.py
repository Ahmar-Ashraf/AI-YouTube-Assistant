from telegram.ext import Updater, CommandHandler
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def start(update, context):
    update.message.reply_text("Welcome! Send /tips for YouTube growth advice.")

def tips(update, context):
    prompt = "Give me one YouTube growth tip."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    update.message.reply_text(response["choices"][0]["message"]["content"])

updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("tips", tips))

updater.start_polling()
updater.idle()