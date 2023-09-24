from telebot import types
import gettext
class massege:
    def __init__(self, bot) -> None:
        self.bot = bot

    def ask_for_language(self, message):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("English", callback_data="en")
        button2 = types.InlineKeyboardButton("Persian", callback_data="fa")
        # Add more buttons for different languages
        markup.add(button1, button2)
        self.bot.send_message(message.chat.id, "Please select your language", reply_markup=markup)
        
    def start_message(self, message, user_language):
        user = message.from_user
        user_details = ""
        lang = user_language.get(user.id, "fa")
        t = gettext.translation('messages', localedir='locales', languages=[lang])
        _ = t.gettext

        if user.first_name is None and user.last_name is None:
            pass
        elif user.first_name is not None and user.last_name is None:
            user_details += f"{user.first_name}"
        elif user.first_name is None and user.last_name is not None:
            user_details += f"{user.last_name}"
        else:
            user_details +=f"{user.first_name} {user.last_name}"

        reply_message = _("👋 Welcome to our service, {user_details}! Our bot is designed to provide you with the date and time every morning. 🌞 With this feature, you'll always be up-to-date and won't miss any important events. 📅 To ensure accuracy, please set your region and country in the settings. 🌍 We look forward to serving you. 😊")
        reply_message = reply_message.format(user_details=user_details)

        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(_("Set Country"), callback_data="set_country")
        markup.add(button1)

        self.bot.reply_to(message, reply_message, reply_markup=markup)