import  os
import telebot 


class Bot:
    def __init__(self) -> None:
        global bot    
        self.BOT_TOKEN=os.environ.get("BOT_TOKEN")
        self.bot = telebot.TeleBot(self.BOT_TOKEN)
        bot = self.bot

    def run(self) -> None :
        bot.infinity_polling()



@bot.message_handler(commands=["start" ])
def start_message(message):
    bot.reply_to(message, "Welcome To My Bot")
