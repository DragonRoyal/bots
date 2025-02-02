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




@bot.command(description="Kicks the specified user.")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    #await ctx.message.add_reaction(":white_check_mark:")
    await ctx.send(f"{member.name} has been kicked by {ctx.author.name}!")
    await ctx.channel.send(f"{ctx.author.name} has kicked {member.display_name}")

@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        server = ctx.message.server
        perms = discord.Permissions(send_messages=False, read_messages=True)
        mutedRole = await guild.create_role(server, name="Muted", permissions=perms)

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")




@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)


@bot.command(description="Bans the user.")
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} have been bannned sucessfully")




@bot.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		
	if (user.name, user.discriminator) == (member_name, member_discriminator):
 	    await ctx.guild.unban(user)
 	    await ctx.channel.send(f"Unbanned: {user.mention}")


#@bot.command()
#async def addMessage(ctx, messageID):
 #   global messageIDs
    
  #  emoji = "👍"
   # channel = ctx.message.channel

   # try:
    #    msg = await channel.fetch_message(messageID)
   # except:
    #    await ctx.send("Invalid Message ID!")
     #   return
   # await msg.add_reaction(emoji)
   # messageIDs.append(messageID)






@bot.command()
async def createemoji(ctx, url: str, *, name):
	guild = ctx.guild
	if ctx.author.guild_permissions.manage_emojis:
		async with aiohttp.ClientSession() as ses:
			async with ses.get(url) as r:
				
				try:
					img_or_gif = BytesIO(await r.read())
					b_value = img_or_gif.getvalue()
					if r.status in range(200, 299):
						emoji = await guild.create_custom_emoji(image=b_value, name=name)
						await ctx.send(f'Successfully created emoji: <:{name}:{emoji.id}>')
						await ses.close()
					else:
						await ctx.send(f'Error when making request | {r.status} response.')
						await ses.close()
						
				except discord.HTTPException:
					await ctx.send('File size is too big!')

@bot.command()
async def deleteemoji(ctx, emoji: discord.Emoji):
	guild = ctx.guild
	if ctx.author.guild_permissions.manage_emojis:
		await ctx.send(f'Successfully deleted (or not): {emoji}')
		await emoji.delete()



@bot.command(description="used to annoy raider")
async def bomb(ctx, member: discord.Member):
               await member.create_dm()
               await member.dm_channel.send(
                   f'Hi {member.name}, your are being bombed GL..F F F F F F F F F F F F  F F F F F F F F F  F F F F F F F F F F  F F F F F F F F F F F  F F F F F F F F F F F  FF F F  F F F F F  F FFF F F F F  FF   F F  FF FF  F FF  F  FF  F F F FF F  FF F  F FF FF F F  FF  F F FF  F F F F FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')
@bot.command(description="sector 5 :wink:")
async def warnf(ctx, member: discord.Member):
    await member.create_dm()
    await member.dm_channel.send(f'{member.name}... if you dare insult me then i shall make your inbox commit r/iwanttodie..you have been warned')              

#@bot.command
#async def memes(
#@bot.command()
#async def balance(ctx):await open_account(ctx.author)

#users = await get_bank_data()


#wallet_amt = users[str(user.id)]["wallet"]
#bank_amt = users[str(user.id)]["bank"]

#embed=discord.Embed(title="{}s balance:".format(member.name), color=0xe20303)
#embed.add_field(name="Wallet:", value=wallet_amt, inline=False)
#embed.add_field(name="Bank:", value=bank_amt, inline=False)

#await ctx.send(embed=embed)

#async def open_account(user):
 #   users = await get_bank_data()

  #  if str(user.id) in users:
   #     return False
    #else:
     #   users[str(user.id)] = {}
      #  users[str(user.id)]["wallet"] = 0
       # users[str(user.id)]["bank"] = 0

   # with open("bank.json", "w") as f:
    #    json.dump(users, f)
    #return True

#async def get_bank_data():
 #   with open("bank.json", "r") as f:
  #      users = json.load(f)
   # return users

#@bot.command()
#async def beg(ctx):

  #  users = await get_bank_data()
 #   user = ctx.author
   # earnings = random.randrange(2000)

    #if earnings == 0:
     #   await ctx.send(f"How unlucky... You didn't get anything...")

   # elif earnings > 50:
    #    await ctx.send(f"Nice you got ${earnings} from a cool dude")

   # elif earnings > 100:
    #    await ctx.send(f"Someone felt nice and gave you ${earnings}")

   # elif earnings > 500:
    #    await ctx.send(f"You seem to have a way with people! Someone gave you ${earnings}")

   # elif earnings > 800:
    #    await ctx.send(f"What a lucky day!! Someone gave you ${earnings}")

   # elif earnings > 1500:
    #    await ctx.send(f"A rich man passed by you and felt bad. So ha gave you ${earnings}")

   # elif earnings > 2000:
    #    await ctx.send(f"A shady man walked up to you and said 'I know how tough it can be out here' before giving you ${earnings}")


   # users[str(user.id)]["wallet"] += earnings

    #with open("bank.json", "r") as f:
     #   users = json.load(f)




#@bot.command(description="sector 0 :wink:")
#async def kill(ctx, member: discord.Member):
 #   embed = discord.Embed(title = member.name, description = member.mention, color=discord.Color.red)
  #  embed.add_field(name = "....you shall die", value="idk", inline = True)
   # await member.send(embed=embed)
    # await member.create_dm()
   # await member.dm_channel.send(f'{member.name}...you shall die')



#@bot.command()
#async def spamr(ctx, member

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=f"on {len(bot.guilds)} servers |+help "))

@bot.command()
async def invite(ctx):
    print("context", ctx)
   # await member.create_dm()
    await ctx.channel.send(' here is the link to invite the bot!: https://bit.ly/3ko8i3y')              


@bot.command(description="Credits") 
async def credits(ctx):
    print("context",ctx)
    await ctx.channel.send("`Some parts of this bots code was from a bot called WolfBot. If you like this bot then inviting wolfbot would help the dev a lot.")


messageIDs = []

@bot.event
async def on_raw_reaction_add(payload):
    global messageIDs

    for messageID in messageIDs:
        if messageID == payload.message_id:
            user = payload.member
            role = "roleName"
            await user.add_roles(discord.utils.get(user.guild.roles, name = role))

@bot.command()
async def addMessage(ctx, messageID):
    global messageIDs
    
    emoji = "👍"
    channel = ctx.message.channel

    try:
        msg = await channel.fetch_message(messageID)
    except:
        await ctx.send("Invalid Message ID!")
        return
    await msg.add_reaction(emoji)
    messageIDs.append(messageID)

@bot.command(aliases=["serverinfo","Server_info","Serverinfo","SERVERINFO","si","Si","SI"])
#@commands.has_any_role('Moderatori', 'Triumvirato', 'Co-Triumvirato', 'Senatori', '690956686147453048')
async def ServerInfo(ctx):
    author = ctx.author.name
    name_server = guild.name
    create_server = guild.create
    owner_server = guild.owner.name
    embed = discord.Embed(
        title="Informazioni del server",
        description=f'Tutte le informazioni generali del nostro server {name_server}',
        color=0x003399
    )
    embed.set_thumbnail(url='')
    embed.set_footer(text=f'Richiesto da: {author}')
    embed.add_field(
        name='Server creato il:',
        value='f{create_server}',
    )
    embed.add_field(
        name='Owner Attuale del server:',
        value='f{create_server}',
    )
    embed.add_field(
        name='Server creato il:',
        value=f'{create_server}',
    )
    embed.add_field(
        name='Server creato il:',
        value=f'{owner_server}',)
mainshop = [{"name":"Watch","price":100,"description":"Time"},
            {"name":"Laptop","price":1000,"description":"Work"},
            {"name":"PC","price":10000,"description":"Gaming"},
            {"name":"Ferrari","price":99999,"description":"Sports Car"},
            {"name": "Lucky Clover","price": 9393939292920,"discription": "can only be obtained by luck"}]
@bot.command(aliases=['bal'])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f'{ctx.author.name} Balance',color = discord.Color.red())
    em.add_field(name="Wallet Balance", value=wallet_amt)
    em.add_field(name='Bank Balance',value=bank_amt)
    await ctx.send(embed= em)

@bot.command()
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(2001)
    if earnings == 0:
        await ctx.send(f"How unlucky... you must be did you buy a unlucky clover?")

    elif earnings > 50:
        await ctx.send(f"Nice you got ${earnings} from a cool dude")

    elif earnings > 100:
        await ctx.send(f"Someone felt nice and gave you ${earnings}")

    elif earnings > 500:
        await ctx.send(f"You seem to have a way with people! Someone gave you ${earnings}")

    elif earnings > 800:
        await ctx.send(f"What a lucky day!! Someone gave you ${earnings}")

    elif earnings > 1500:
        await ctx.send(f"A rich man passed by you and felt bad. So he gave you ${earnings}")

    elif earnings > 2000:
        await ctx.send(f"A shady man walked up to you and said 'I know how tough it can be out here' before giving you ${earnings}")
    
    elif earnings == 2001:
        await ctx.send(f" A famous celebrity waked down the road.. you begged her so much you got 2001$



    await ctx.send(f'{ctx.author.mention} Got {earnings} coins!!')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)


@bot.command(aliases=['wd'])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    await ctx.send(f'{ctx.author.mention} You withdrew {amount} coins')


@bot.command(aliases=['dp'])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    await ctx.send(f'{ctx.author.mention} You deposited {amount} coins')


@bot.command(aliases=['sm'])
async def send(ctx,member : discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount,'bank')
    await update_bank(member,amount,'bank')
    await ctx.send(f'{ctx.author.mention} You gave {member} {amount} coins')


@bot.command(aliases=['rb'])
async def rob(ctx,member : discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)


    if bal[0]<100:
        await ctx.send('It is useless to rob him :(')
        
      

    earning = random.randrange(0,bal[0])

    await update_bank(ctx.author,earning)
    await update_bank(member,-1*earning)
    await ctx.send(f'{ctx.author.mention} You robbed {member} and got {earning} coins')


@bot.command()
async def slots(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return
    final = []
    for i in range(3):
        a = random.choice(['X','O','Q'])

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author,2*amount)
        await ctx.send(f'You won :) {ctx.author.mention}')
    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.send(f'You lose :( {ctx.author.mention}')


@bot.command()
async def shop(ctx):
    em = discord.Embed(title = "Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        description = item["description"]
        #dict.get("description", default=None)

        em.add_field(name = name, value = f"${price} | {description}")

    await ctx.send(embed = em)



@bot.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("Wth mate that item is not in the shop.")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item} What about you get a job?")
            return


    await ctx.send(f"You just bought {amount} {item}")


@bot.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.send(embed = em)


async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
l          name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]
    
@bot.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.7* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]

@bot.command(aliases = ["lb"])
async def leaderboard(ctx,x = 1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = bot.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)


async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json','w') as f:
        json.dump(users,f)

async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)

    return users


async def update_bank(user,change=0,mode = 'wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json','w') as f:
        json.dump(users,f)
    bal = users[str(user.id)]['wallet'],users[str(user.id)]['bank']
    return bal
        
keep_alive()
bot.run(TOKEN)


    return True


