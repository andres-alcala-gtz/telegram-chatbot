from telegram.ext import *
import env as keys
import responses as r

def start_command(update, context):
    update.message.reply_text('Type something to get started!')

def help_command(update, context):
    update.message.reply_text('If you need help you should ask for it on Google!')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.sample_responses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f'Update {update} caused error {context.error}')

def main():
    # Create Bot
    updater = Updater(keys.API_KEY, use_context=True)
    dispatcher = updater.dispatcher
    # Add Handlers
    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    dispatcher.add_error_handler(error)
    # Start Bot
    updater.start_polling()
    updater.idle()

print('Running chatbot...')
main()