from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from googletrans import Translator
BOT_TOKEN = '6395823895:AAEk0xLHkCDIlxj9zTbPfuJU8z2fWEO4tPI'
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome to the Translation Bot! Send me a word or phrase in English, and I will translate it to Farsi.')

def translate(update: Update, context: CallbackContext):
    text = update.message.text
    translator = Translator()
    translation = translator.translate(text, src='en', dest='fa')
    update.message.reply_text(f'Translation to Farsi: {translation.text}')

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
