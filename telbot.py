import telebot
#lanprin
bot = telebot.TeleBot('')

# Handler for /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi", parse_mode='html')

# Handler for text messages
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text, parse_mode='html')

# Start polling for messages
bot.infinity_polling(timeout=10, long_polling_timeout=5)
