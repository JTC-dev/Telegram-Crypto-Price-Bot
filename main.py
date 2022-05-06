from asyncio import constants
import telebot
import time
import constants
from binance.client import Client


client = Client(constants.binance_api_key, constants.binance_secret)


tb = telebot.TeleBot(constants.token) #ENTER YOUR BOT TOKEN FROM THE BOTFATHER

chatid = constants.chatid #ENTER YOUR CHAT ID
notify = 0

while True:
    raw_price = client.get_avg_price(symbol='BTCUSDC')

    btc_price = raw_price['price']  

    @tb.message_handler(commands=['start', 'help', 'live'])
    def send_welcome(message):
        tb.reply_to(message, "I'm alive!")


    if int(float(btc_price)) < 35000 and notify == 0:
        tb.send_message(chat_id=constants.chatid, text=f'BTC price has fallen to {btc_price} check health factor')
        notify = notify + 1
    elif int(float(btc_price)) > 36000 and notify == 1:
        tb.send_message(chat_id=constants.chatid, text=f'BTC is back in a safe range at {btc_price}')
        notify = notify - 1

    time.sleep(5)
