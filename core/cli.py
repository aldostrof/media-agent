import configparser

from telegram.ext import Updater
from telegram.ext import CommandHandler

from log_ss.log_man import LogManager

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def main():
    # initializes logging subsystem
    log_man = LogManager()
    log_man.setup()
    
    config = configparser.ConfigParser()
    config.read('config/bot.config')
    token = config['TOKEN']['bot_token']
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()


if __name__ == "__main__":
    main()

