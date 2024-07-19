import discord
from discord.ext import commands
from discord.ext import * 
import csv
import os
class utilitycog(commands.Cog):
  def __init__(self, bot):
    self.bot=bot


  @commands.command(name="bwtoggle")
  @commands.has_permissions(manage_guild=True)
  async def bwtoggle(self,ctx):
        with open('test.csv', mode='w') as keyfile:
            test_writer = csv.writer(keyfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        
            with open('bw.csv', mode='r') as keyfile:
                csv_reader = csv.reader(keyfile, delimiter=',')

                match=0
                # if os.path.getsize("bw.csv") == 0:
                #   test_writer.writerow([ctx.guild.id,"off"])
                # else:
                for row in csv_reader:
                    if row[0] == str(ctx.guild.id):
                        match=1

                        if row[1]=="off":
                            test_writer.writerow([ctx.guild.id, "on"])
                            sign="on"
                            word="Enabled"
                        else:
                            test_writer.writerow([ctx.guild.id, "off"])
                            sign="off"
                            word="Disabled"
                        
                    else:
                        test_writer.writerow([row[0],row[1]])
            
        if match==0:
            with open('test.csv', mode='a') as keyfile:
                test_a = csv.writer(keyfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                test_a.writerow([ctx.guild.id, "off"])
        os.rename('test.csv','bw.csv')
        try:
            if sign=="on":
                emoji="<a:ONs:874182129121103902>"
            else:
                emoji="<a:OFFs:874182119696515102>"
            em=discord.Embed(title=f"BadWord Toggles{emoji}",description=f"{word} Anti BadWord <:tool_cool:875562335253704796>")
            em.set_footer(text='Anti Badword 1.0 | Suggestions!')   
            await ctx.send(embed=em)
        except:
            
            await ctx.send("Enabling Anti Badword sys run ;bwtoggle again for it to finish!")

 
  



def setup(bot):
    bot.add_cog(utilitycog(bot))
