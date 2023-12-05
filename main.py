import json
import requests
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
 
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
 
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
 
    res = json.loads(requests.post('http://127.0.0.1:8080', data= {"text": update.message.text}).text)
 
    await context.bot.send_message(chat_id=update.effective_chat.id, text=res.get("output"))
 
if __name__ == '__main__':
    application = ApplicationBuilder().token('').build()
 
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
 
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
 
    application.run_polling()
