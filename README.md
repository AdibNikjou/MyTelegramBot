# MyTelegramBot
## Setting Up Your Bot Token
To set up your bot token, you need to export it as an environment variable. Use the following command:
```bash
export BOT_TOKEN=<Your Bot Token Here>
```
For convenience, if you don't want to export your bot token every time you log in, you can add the above line to your .bashrc file. This will automatically set the BOT_TOKEN environment variable whenever you start a new shell session.

## Installation and Execution

This project requires certain Python packages to run. You can install these packages using pip with the following command:

```bash
python -m pip install -r requirements.txt
```

After installing the necessary packages, you can get started by cloning the repository and running the main Python script. Use the following commands:
```bash
git clone https://github.com/AdibNikjou/MyTelegramBot.git
cd MyTelegramBot
python main.py
```
These commands will clone the repository into a directory named MyTelegramBot, navigate into that directory, and then run the main.py script, which starts the bot.