import discord
from discord.ext import commands
import os
import keep_alive
import json
import requests
import random
from replit import db

bot = commands.Bot(command_prefix="ma!")

responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
             "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
             "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
             "Yes.", "Yes – definitely.", "You may rely on it."]

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="MaiApi || ma!help"))
  print("The bot is ready!")

@bot.command()
async def website(ctx):
  await ctx.send(embed=discord.Embed(title="URL of our website",description="https://MaiAPI.dragonroyale.repl.co",color=0xFFFF66))

@bot.command()
async def info(ctx,endpoint=None):
  if endpoint == None:
    embed=discord.Embed(title="Info command",description = "Info is available on these endpoints:\n\n",color=0xFFFF66)
    for i in db.keys():
      embed.description += f"{str(i)}\n"
    embed.description += "\nType ma!info <endpoint> for info on a particular endpoint"
    await ctx.send(embed=embed)
  else:
    info = db[endpoint]
    if info is not None:
      em = discord.Embed(title=endpoint,description=info,color=0x0c4af8)
      await ctx.send(embed=em)

@bot.command()
async def fact(ctx):
  await ctx.send(requests.get("https://MaiAPI.dragonroyale.repl.co/fact").text)

@bot.command(name="8ball")
async def _8ball(ctx,*,query):
  em = discord.Embed(title=query,description=random.choice(responses),color=0x28c979)
  await ctx.send(embed=em)
