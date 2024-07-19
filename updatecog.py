import discord
from discord.ext import commands
VERSION = "1.0.1"

class updatecog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def update(self, ctx):
      updateHelp = discord.Embed(
        description=f"Changelog Notes For Beta **{VERSION}** | 8/6/2021",
        color=0x36393E
      )

      updateHelp.add_field(name="Additions", value="> [+] Added Help\n> [+] Added Bot Join Message",inline=False)

      await ctx.send(embed=updateHelp)

def setup(bot):
    bot.add_cog(updatecog(bot))
