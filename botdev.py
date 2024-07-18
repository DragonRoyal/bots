import discord
import json
from discord.ext import commands
from discord.ext.commands import errors, has_permissions, MissingPermissions

class botdev(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.command()
    @commands.is_owner()
    async def forceleave(self,ctx):
        await ctx.send("leaving server!")
        await ctx.guild.leave()
        
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send("Could not unload cog")
            return
        await ctx.send("Cog unloaded")

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could not load cog")
            return
        await ctx.send("Cog loaded")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could not reload cog")
            return
        await ctx.send("Cog reloaded")



def setup(bot):
    bot.add_cog(botdev(bot))
