import telebot
from masseges import massege
import os
class Bot:
    def __init__(self) -> None:  
        self.BOT_TOKEN=os.environ.get("BOT_TOKEN")
        self.bot = telebot.TeleBot(self.BOT_TOKEN)
        self.masseges = massege(self.bot)
        self.register_handlers()

    def register_handlers(self):
        @self.bot.message_handler(commands=["start"])
        def start_message(message):
            self.masseges.start_message(message)

        
    def run(self) -> None :
        self.bot.infinity_polling()

bot_init = Bot()
bot_init.run()