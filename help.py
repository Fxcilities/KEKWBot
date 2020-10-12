import discord
from discord.ext import commands
from discord.ext import *
from discord.ext.commands import *
import asyncio

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
    
        embed = discord.Embed(
          title="Bois Help", 
          description="_ _\nThank you for inviting KEKW bot!\nCheck out our other bot, [Essentials](https://essentialsbot.xyz)\n_ _", 
          color=discord.Color.dark_gold()
        )
        embed.add_field(name="Main commands:", value="**```kekw!start (amount, defaults to 50)```**", inline=False)
        embed.set_footer(text="Requested by: " + str(ctx.author), icon_url=str(ctx.author.avatar_url))
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=30)

def setup(bot):
    bot.add_cog(help(bot))
