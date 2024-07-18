# imports
import discord, aiohttp, random, csv, re, asyncio, os
from configparser import ConfigParser
from discord.ext import commands, tasks
from discord.utils import find, get
from discord_components import DiscordComponents, Button, Select, SelectOption
#setting up ConfigParser
config = ConfigParser()
config.read('config.ini')

# setting up variables
TOKEN = os.environ['TOKEN']
PREFIX = config.get('info', 'prefix')
VERSION=config.get('info', 'version')


#INTENTS ARE NOT ENABLED, PLEASE ENABLE THEM IN THE DEV PORTAL -from snow

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, help_command=None, strip_after_prefix=True, intents = intents) #Updated by snow


# bot events
@bot.event
async def on_ready(): #I removed (ctx), discord.on_ready() takes no args, commands.Context would be invalid and crash the event- from snow
    DiscordComponents(bot)
    print("Bot Online pog")

@bot.event
async def on_command_error(ctx, error):
	await ctx.send(embed=discord.Embed(description=error,colour=discord.Colour.red()))

@bot.event
async def on_guild_join(guild): 
    general = find(lambda x: x.name == 'general',guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        welcomeEmbed = discord.Embed(title='Camee Bot',
          description=f"My Default Prefix is: ``{PREFIX}``.",
          color=0x36393E)


       
        welcomeEmbed.set_image(url="https://cdn.discordapp.com/attachments/874139644231561226/874504810399944754/Camee.png")
        welcomeEmbed.set_author(name="Camee V" + VERSION)
        welcomeEmbed.set_footer(text="Thanks for inviting me!")
        await general.send(embed=welcomeEmbed)

@bot.event
async def on_message(message):
	await bot.process_commands(message)
	if message.author.bot:
		pass
  
@bot.command()
async def MCtest(ctx):
  await ctx.send("<:MCdirt:914734151838597120>")

# run bot
# extensions
bot.load_extension('cogs.eval')
bot.load_extension('cogs.games')
bot.load_extension('cogs.help')
bot.run(TOKEN)
