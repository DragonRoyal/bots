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



# [maininfo,no color, color bad bad,hmmmm idk]

@bot.command()
async def add_endpoint(ctx):
  if not int(ctx.author.id) in [783136680923758622,599266233350881291,819786180597907497]:
    return
  
  await ctx.send("What is the name of the endpoint you want to add?")
  name = await bot.wait_for('message',check = lambda m: m.author == ctx.author and m.channel == ctx.channel)
  await ctx.send("What info do you want to add on the basis of this endpoint?")
  info = await bot.wait_for('message',check = lambda m: m.author == ctx.author and m.channel == ctx.channel)
  db[name.content] = info.content
  await ctx.send("Endpoint has been added.")

  

@bot.command()
async def remove_endpoint(ctx,name):
  if not int(ctx.author.id) in [783136680923758622,599266233350881291,819786180597907497]:
    return
  del db[name]
  await ctx.send("removed endpoint.")

@bot.command()
async def add_fact(ctx,*,fact):
  if not int(ctx.author.id) in [783136680923758622,599266233350881291,819786180597907497]:
    return
  if not db['facts']:
    db['facts'] = []
  db['facts'].append(fact)
  await ctx.send("Fact added to list")
  
@bot.command()
async def remove_fact(ctx,*,fact):
  if not int(ctx.author.id) in [783136680923758622,599266233350881291,819786180597907497]:
    return
  if not db['facts']:
    db['facts'] = []
  try:
    db['facts'].remove(fact)
    await ctx.send("Fact removed from list")
  except:
    await ctx.send("Fact not found")

keep_alive.keep_alive()
bot.run(os.getenv('TOKEN'))
