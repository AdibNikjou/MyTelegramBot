import telebot
from masseges import massege
import os
import pickle

class Bot:
    def __init__(self) -> None:  
        self.BOT_TOKEN=os.environ.get("BOT_TOKEN")
        self.bot = telebot.TeleBot(self.BOT_TOKEN)
        self.masseges = massege(self.bot)
        self.register_handlers()
        try:
            with open('user_language.pkl', 'rb') as f:
                self.user_language = pickle.load(f)
        except (OSError, IOError) as e:
            self.user_language = {}

    def register_handlers(self):

        @self.bot.callback_query_handler(func=lambda call: call.data in ["en", "fa"])
        def callback_query(call):
            # Store the user's language preference
            self.user_language[call.from_user.id] = call.data
            print(f"id of user_language in Bot: {id(self.user_language)}")  # print the id of user_language in Bot
            print(f"After update: {self.user_language}")  # print user_language after update
            print(f"call: {call}")  # print the call object
            with open('user_language.pkl', 'wb') as f:
                pickle.dump(self.user_language, f)
            self.masseges.update_user_language(self.user_language)  # Update user_language in massege class
            self.masseges.start_message(call.message, call.from_user.id, self.user_language)


        @self.bot.message_handler(commands=["start"])
        def start_message(message):
            if message.from_user.id not in self.user_language:
                self.masseges.ask_for_language(message)
            else:
                self.masseges.start_message(message, message.from_user.id, self.user_language)


        @self.bot.callback_query_handler(func=lambda call: call.data == "set_country")
        def callback_set_region(call):
            # code to set country
            self.bot.answer_callback_query(call.id, "Country Set")

    def run(self) -> None :
        self.bot.infinity_polling()

bot = Bot()
bot.run()