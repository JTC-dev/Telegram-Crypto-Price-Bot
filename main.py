from asyncio import constants
import requests
import telebot
import constants
from binance.client import Client


client = Client(constants.binance_api_key, constants.binance_secret)



tb = telebot.TeleBot(constants.token, parse_mode=None) #ENTER YOUR BOT TOKEN FROM THE BOTFATHER

chatid = constants.chatid #ENTER YOUR CHAT ID
notify = 0


raw_price = client.get_avg_price(symbol='BTCUSDC')

btc_price = raw_price['price']  

not_rounded_btc_price = int(float(btc_price))

rounded_btc_price = round(not_rounded_btc_price,2)

@tb.message_handler(commands=['start', 'help', 'live'])
def send_welcome(message):
        tb.reply_to(message, f"I'm Alive! Current BTC price: ${rounded_btc_price}USD")

if rounded_btc_price < 35000 and notify == 0:
    tb.send_message(chat_id=constants.chatid, text=f'BTC price has fallen to {btc_price} check health factor')
    notify = notify + 1

elif rounded_btc_price > 36000 and notify == 1:
    tb.send_message(chat_id=constants.chatid, text=f'BTC is back in a safe range at {btc_price}')
    notify = notify - 1

tb.infinity_polling()
