from keep_alive import keep_alive
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import aiohttp
from io import BytesIO
import json
import random
#from pretty_help import PrettyHelp
TOKEN='empty'
GUILD='Ooof'
intents=discord.Intents.all()
bot = commands.Bot(command_prefix="+",intents=intents) #help_command=Prettyhelp()

#class MyHelpCommand(commands.MinimalHelpCommand):
 #   async def send_pages(self):
  #      destination = self.get_destination()
   #     e = discord.Embed(color=discord.Color.blurple(), description='')
    #    for page in self.paginator.pages:
     #       e.description += page
      #  await destination.send(embed=e)

#bot.help_command = MyHelpCommand()

#@bot.event
#async def on_message(message):
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
  #  if message.content == "help":
        # SENDS BACK A MESSAGE TO THE CHANNEL.
   #     await message.channel.send("`hey i see you need help here are all the commands: help, donate, about, version,`  `our syntax is +`")

    #await bot.process_commands(message)



@bot.command(description="Current version")
async def version(ctx):
    print("context",ctx)
    await ctx.channel.send("`CURRENT VERSION: 1.0 beta`")
print("Hi")
@bot.command(description="Referance Guide for mods")
async def rg(ctx):
    print("context",ctx)
    await ctx.channel.send("`minor stuff` <a:pepeshades:814160542309810216> :")
    await ctx.channel.send("` 1: Spamming,  2: idk other minor stuff`")
    await ctx.channel.send("`What you can do: warn, mute, kick, and temp ban`")
    await ctx.channel.send("` Serious stuff` <a:transparent:814160983572217877> :")
    await ctx.channel.send("`Rasicm, homophobia, gore etc`")
    await ctx.channel.send("`Temp ban, perma ban, mute 10-20 days etc`")
@bot.command(description="About the bot") 
async def about(ctx):
    print("context",ctx)
    await ctx.channel.send("`Wolfbot is a bot created for test purposes and for select servers. If you have any questions contact DragonRoyale` <:thonk:813989870799552512>")

@bot.command(description="Lists Premuim perks")   
async def premuim(ctx):
    print("context",ctx)
    await ctx.channel.send("`Premuim is a feature you can add to this bot, at least one member will have to donate to unlock premuim. Premuim will unlock 24/7 live support, quicker updates overall, sneak peaks to updats and so much more`<a:speed:804021879697965076>")


@bot.command(description="Displays emojis in use") 
async def emoji(ctx):
    print("context",ctx)
    await ctx.channel.send("<a :PoopGif:393553833927639040>")

@bot.command(description="Donation link")
async def donate(ctx):
    print("context",ctx)
    await ctx.channel.send("`Hi if you want to donate to the bot for lots of benifits visit` https://www.patreon.com/dragonroyale")




                
@bot.command(description="Link for FREE bobux.")
async def bobux(ctx):
    print("context",ctx)
    await ctx.channel.send("`link for free B O B U X` <https://cutt.ly/BlIKwqD>")



@bot.event
async def on_member_join(member):
    print("Im inside member join")
    for guild in bot.guilds:
        print("GUILD = ",guild, guild.id, guild.name, guild.member_count)
        if (guild.name == GUILD):
            my_guild=guild
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to {member.guild.name}.If you need help just say +help'
    )
    

@bot.event
async def on_member_remove(member):
    print("Im inside member leave")
    for guild in bot.guilds:
        print("GUILD = ",guild, guild.id, guild.name, guild.member_count)
        if (guild.name == GUILD):
            my_guild=guild
    await member.create_dm()
    await member.dm_channel.send(
        f'Sorry to see you go {member.name}, you are leaving {member.guild.name}, if you ever want to join again ask the server owner'
    )


