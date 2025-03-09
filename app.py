from telegram.ext import (
    Updater, 
    CommandHandler, 
    MessageHandler, 
    filters,  # Changed from Filters to filters (lowercase)
    CallbackQueryHandler, 
    InlineQueryHandler
)
from bot import GenesisBot
import os

PORT = os.environ.get('PORT', 5000)
AUTH = os.environ.get('GENESYS_BOT_TOKEN')
HOOK = os.environ.get('WEBHOOK')

def app():
    genesis = GenesisBot()
    updater = Updater(AUTH, use_context=True)

    dp = updater.dispatcher

    # Updated filter syntax
    dp.add_handler(CommandHandler("start", genesis.start, filters=(filters.COMMAND | filters.Regex(r'^/start@[\w.]+$'))))
    dp.add_handler(CommandHandler("help", genesis.help, filters=(filters.COMMAND | filters.Regex(r'^/menu@[\w.]+$'))))
    dp.add_handler(CommandHandler("dev", genesis.dev, filters=(filters.COMMAND | filters.Regex(r'^/dev@[\w.]+$'))))

    dp.add_handler(InlineQueryHandler(genesis.inline_query, pass_chat_data=True))
    dp.add_handler(CallbackQueryHandler(genesis.callback_query))

    dp.add_error_handler(genesis.error)

    updater.start_webhook(listen='0.0.0.0', port=PORT, webhook_url=HOOK)
    updater.idle()

if __name__ == '__main__':
    app()
