import telebot
import ccxt
import time

token = '8481274077:AAFw52zzzcYSIMOjyynqxKpCulxqdFuQVOc'
api_key = '49475dac-2721-4a39-90c4-4dcdca2afae0'
api_secret = '7a2268fe-6f9e-4aee-a857-e01f26ca3447'

exchange = ccxt.bitexpro({
    'apiKey': api_key,
    'secret': api_secret,
})

bot = telebot.TeleBot(token)

def check_balance():
    balance = exchange.fetch_balance()
    usdt_balance = balance['USDT']['total']
    if usdt_balance >= 500:
        # سحب المبلغ إلى محفظتك
        # withdraw(usdt_balance, 'TSbfRe4s8uQu35i85Vh3QenuzZcbhX925V')
        bot.send_message('1967999105', 'رصيدك على Bitexpro هو: ' + str(usdt_balance))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'مرحبًا! البوت يعمل الآن.')
    while True:
        check_balance()
        time.sleep(60)

bot.polling()
