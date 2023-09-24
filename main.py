import telebot
from masseges import massege
import os
import pickle

class Bot:
    def __init__(self) -> None:  
        self.BOT_TOKEN=os.environ.get("BOT_TOKEN")
        self.bot = telebot.TeleBot(self.BOT_TOKEN)
        self.masseges = massege(self.bot)
        self.ask_for_language_message_id = None
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
            with open('user_language.pkl', 'wb') as f:
                pickle.dump(self.user_language, f)
            self.masseges.update_user_language(self.user_language)  # Update user_language in massege class
            self.masseges.start_message(call, call.message, call.from_user.id, self.user_language)

            # Delete the "ask for language" message
            if self.ask_for_language_message_id:
                self.bot.delete_message(chat_id=call.message.chat.id, message_id=self.ask_for_language_message_id)


        @self.bot.message_handler(commands=["start"])
        def start_message(message):
            if message.from_user.id not in self.user_language:
                self.ask_for_language_message_id = self.masseges.ask_for_language(message).message_id
            else:
                self.masseges.start_message(message, message, message.from_user.id, self.user_language)
                # Delete the "ask for language" message if it exists
                if self.ask_for_language_message_id:
                    try:
                        self.bot.delete_message(chat_id=message.chat.id, message_id=self.ask_for_language_message_id)
                    except telebot.apihelper.ApiTelegramException:
                        pass

        @self.bot.callback_query_handler(func=lambda call: call.data == "select_country")
        def callback_set_region(call):
            # code to set country
            self.bot.answer_callback_query(call.id, "Country Set")

    def run(self) -> None :
        self.bot.infinity_polling()

bot = Bot()
bot.run()