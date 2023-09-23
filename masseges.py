class massege:
    def __init__(self, bot) -> None:
        self.bot = bot

    def start_message(self, message):
        user = message.from_user
        user_details = ""

        if user.first_name is None and user.last_name is None:
            pass
        elif user.first_name is not None and user.last_name is None:
            user_details += f"{user.first_name}"
        elif user.first_name is None and user.last_name is not None:
            user_details += f"{user.last_name}"
        else:
            user_details +=f"{user.first_name} {user.last_name}"

        reply_message = f"""👋 Welcome to our service, {user_details}!
Our bot 🤖 is designed to provide you with the date and time every morning. 🌞
With this feature, you'll always be up-to-date and won't miss any important events. ⏰
To ensure accuracy, please set your region and country  in the settings. 🌍
 We look forward to serving you. 😊🙌
"""

        self.bot.reply_to(message, reply_message)