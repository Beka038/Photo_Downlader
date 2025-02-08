import telebot
from config import TOKEN
    
# Инициализация бота с использованием его токена
bot = telebot.TeleBot(TOKEN)

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
    
@bot.message_handler(content_types=['photo'])
def send_photo(message):
    bot.reply_to(message, "Скачал твою фотку")
    file_info = bot.get_file(message.photo[-1].file_id)
    download_file = bot.download_file(file_info.file_path)
    file_path = 'img/' + f'{message.photo[-1].file_id}.jpg'
    with open(file_path, 'wb') as file:
        file.write(download_file)
    bot.reply_to(message, "Скачал твоё фото")
    
    
# Запуск бота
bot.polling()
