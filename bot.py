import discord
import logging
import os

from asyncio import sleep
from discord.ext import commands
from dotenv import load_dotenv

from constants import botStatus, salute

bot = commands.Bot(command_prefix = '!')
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename = 'discord.log', encoding = 'utf-8', mode = 'w')
handler.setFormatter(logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s'))
logger.addHandler(handler)

###---------------------------------------------------------------------

@bot.event
async def on_ready():
    print('\nBooting up...')
    print(bot.user.name)
    print('Now online!\n-------------')
    
    while True:
        game_status = await botStatus.chooseGame()
        
        await bot.change_presence(activity = discord.Game(name = game_status))
        await sleep(7200)
        
print('Loading extensions...\n')
for filename in os.listdir('./cogs'):
    try:
        if filename.endswith('.py'):
            bot.load_extension(F'cogs.{filename[:-3]}')
            
    except Exception as err:
        print(F'Failed to load {filename}. Check directory?\n')
        print(err)
    
    else:
        print(F'{filename} sucessfully loaded...')


@bot.listen('on_message')
async def Salute(message):
    if(message.author.id == bot.user.id):
        return
    
    elif 'rock and stone' in message.content.lower():
        await message.channel.send(await salute.RockandStone())

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)