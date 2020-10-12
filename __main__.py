import discord
from discord.ext import commands
import io
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")
prefix = os.getenv("prefix")

bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')


@bot.command()
@commands.has_permission(manage_server=True)  
async def start(ctx, amount: int = 50):
  em1 = discord.Embed(title="Starting...", color=discord.Color.blue(), description=f"I will start uploading **{amount}** kekw emojis!")
  em2 = discord.Embed(title="Finished", color=discord.Color.green())
  msg = await ctx.send(embed=em1)
  cur = int(1)
  while cur <= amount:
    with open("kekw.png", "rb") as f:
      res = f.read()
      await ctx.guild.create_custom_emoji(name=f"kekw{cur}", image=res)
      cur += 1
  await msg.edit(embed=em2)
  print(f"Uploaded: `{amount}` kekw emojis to {ctx.guild.name}")

@bot.event
async def on_ready():
  bot.change_presence(status=discord.Status.online, activity=discord.Activity(name="kekw's laugh",type=discord.ActivityType.watching))
  print(f"Bot ready, logged in as {bot.user} ({bot.user.id})")

bot.load_extension('help')
bot.run(token)
