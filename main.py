import discord
import os
import requests
import json
import time
from keep_alive import keep_alive
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$btc'):
    response_API = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT')
    data = response_API.text
    parse_json = json.loads(data)
    price = parse_json['price']
    print("BTC price:",price)
      
    await message.channel.send("BTC price is " + price + " $")

  if message.content.startswith('$eth'):
    response_API = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=ETHUSDT')
    data = response_API.text
    parse_json = json.loads(data)
    price = parse_json['price']
    print("ETH price:",price)
      
    await message.channel.send("ETH price is " + price + " $")

  if message.content.startswith('$ltc'):
    response_API = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=LTCUSDT')
    data = response_API.text
    parse_json = json.loads(data)
    price = parse_json['price']
    print("LTC price:",price)
      
    await message.channel.send("LTC price is " + price + " $")

  if message.content.startswith('$bch'):
    response_API = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=BCHUSDT')
    data = response_API.text
    parse_json = json.loads(data)
    price = parse_json['price']
    print("BCH price:",price)
      
    await message.channel.send("BCH price is " + price + " $")


keep_alive()

client.run(os.getenv('TOKEN'))
