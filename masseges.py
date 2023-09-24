from telebot import types
import gettext
class massege:
    def __init__(self, bot) -> None:
        self.bot = bot
    
    def _(self , text,user_language , user_id):
        lang = user_language.get(user_id, "fa")
        t = gettext.translation('messages', localedir='locales', languages=[lang])
        _ = t.gettext
        return _(text)

    def ask_for_language(self, message):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("English", callback_data="en")
        button2 = types.InlineKeyboardButton("فارسی", callback_data="fa")
        # Add more buttons for different languages
        markup.add(button1, button2)
        return self.bot.send_message(message.chat.id, "Please select your language", reply_markup=markup)
    
    def update_user_language(self, user_language):
        self.user_language = user_language

    def start_message(self, call ,message, user_id, user_language):
        user = call.from_user
        user_details = ""

        if user.first_name is None and user.last_name is None:
            pass
        elif user.first_name is not None and user.last_name is None:
            user_details += f"{user.first_name}"
        elif user.first_name is None and user.last_name is not None:
            user_details += f"{user.last_name}"
        else:
            user_details +=f"{user.first_name} {user.last_name}"

        reply_message = self._("Start_message👋",user_language,user_id)
        reply_message = reply_message.format(user_details=user_details)

        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(self._("Set Country",user_language,user_id), callback_data="select_country")
        button2 = types.InlineKeyboardButton(self._("Settings",user_language,user_id), callback_data="settings")
        markup.add(button1, button2)

        self.bot.send_message(chat_id=message.chat.id, text=reply_message, reply_markup=markup)
        # if you want to reply instead of direct message
        #self.bot.reply_to(message, reply_message, reply_markup=markup)