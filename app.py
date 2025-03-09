from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
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
    
    # Create application
    application = Application.builder().token(AUTH).build()
    
    # Add handlers to application
    application.add_handler(CommandHandler("start", genesis.start, filters=(filters.COMMAND | filters.Regex(r'^/start@[\w.]+$'))))
    application.add_handler(CommandHandler("help", genesis.help, filters=(filters.COMMAND | filters.Regex(r'^/menu@[\w.]+$'))))
    application.add_handler(CommandHandler("dev", genesis.dev, filters=(filters.COMMAND | filters.Regex(r'^/dev@[\w.]+$'))))
    
    application.add_handler(InlineQueryHandler(genesis.inline_query))
    application.add_handler(CallbackQueryHandler(genesis.callback_query))
    
    application.add_error_handler(genesis.error)
    
    # Set up webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=int(PORT),  # Ensure PORT is an integer
        webhook_url=HOOK
    )

if __name__ == '__main__':
    app()
