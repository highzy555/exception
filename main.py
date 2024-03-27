from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from response import get_response
import discord
from flask import Flask, render_template
from threading import Thread
from dotenv import load_dotenv
app = Flask('')
@app.route('/')
def home():
  return "bot python is online!"
def index():
  return render_template("index.html")
def run():
  app.run(host='0.0.0.0', port=8080)
def high():
  t = Thread(target=run)
  t.start()

load_dotenv()
TOKEN = os.getenv('bot')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was emty because intents were not enabled probably)')
        return
        
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
        
        
        
    try:
        response: str = get_response(user_message)
        await message.channel.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
    
# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running!")
    
@client.event
async def on_ready() -> None:
  print(f"{client.user} is now running!")
  await client.change_presence(activity=discord.Streaming(
      name='Black Market!', url='https://www.twitch.tv/example_channel'))    
    
    
# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
        
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}" ')
    #await ctx.reply(message,user_message)
    await send_message(message, user_message)    
    
# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)
    
if __name__ == '__main__':
    high()
    main()
    
    
    
    
    