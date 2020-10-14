import discord
from discord.ext import commands
import io
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

token = os.getenv("token")
prefix = os.getenv("prefix")

bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

@bot.command()
async def emojis(ctx):
  emojis = 0
  kekw_emojis = 0
  for emoji in ctx.guild.emojis:
    if emoji.name.startswith("kekw"):
      kekw_emojis += 1
    emojis  += 1
  e = discord.Embed(title=f"There are {emojis} emojis. There are {kekw_emojis} kekw emojis.", colour=discord.Colour.blue())
  await ctx.send(embed=e)

@bot.command()
@commands.has_permissions(manage_emojis=True)
async def start(ctx, amount: int = 50):
  em1 = discord.Embed(title="Starting...", color=discord.Color.blue(), description=f"I will start uploading **{amount}** kekw emojis!")
  em2 = discord.Embed(title="Finished", color=discord.Color.green())
  msg = await ctx.send(embed=em1)
  await asyncio.sleep(2)
  try:
    cur = int(1)
    while cur <= amount:
      with open("kekw.png", "rb") as f:
        res = f.read()
        await ctx.guild.create_custom_emoji(name=f"kekw{cur}", image=res)
        cur += 1
    await msg.edit(embed=em2)
    print(f"Uploaded: `{amount}` kekw emojis to {ctx.guild.name}")
  except Exception as e:
    error = discord.Embed(title="Error!", description=f"```{e}```", colour=discord.Colour.red())
    await msg.edit(embed=error)

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name="kekw's laugh",type=discord.ActivityType.watching))
  print(f"Bot ready, logged in as {bot.user} ({bot.user.id})")

bot.load_extension('help')
bot.run(token)
