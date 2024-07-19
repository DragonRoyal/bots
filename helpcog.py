import discord
from discord.ext import commands

class helpcog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        helpEmbed = discord.Embed(
          description="[Support Server](https://discord.gg/8dyj8qdDKD) | [Invite Me](https://discord.com/api/oauth2/authorize?client_id=873372643401809990&permissions=8&scope=bot)",
          color=0x36393E
        )
        helpEmbed.set_author(name=f"")
        helpEmbed.set_image(url="https://media.discordapp.net/attachments/873379802315366405/873406192339255346/MAFIA_4.png")
        await ctx.send(embed=helpEmbed)

def setup(bot):
    bot.add_cog(helpcog(bot))  
