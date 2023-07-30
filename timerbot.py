# python
import discord
from discord.ext import commands
import time

bot = commands.Bot(command_prefix='~')
start_time = None


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('------')


@bot.command()
async def timer(ctx):
    global start_time
    if start_time is None:
        start_time = time.time()
        await ctx.send("Timer started.")
    else:
        await ctx.send("Timer already running.")


@bot.command()
async def checktime(ctx):
    global start_time
    if start_time is not None:
        current_time = time.time() - start_time
        hours = int(current_time // 3600)
        minutes = int((current_time % 3600) // 60)
        seconds = int(current_time % 60)

        elapsed_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        await ctx.send(f"Elapsed Time: {elapsed_time}")
    else:
        await ctx.send("No timer running.")


@bot.command()
async def stop(ctx):
    global start_time
    if start_time is not None:
        start_time = None
        await ctx.send("Timer stopped.")
    else:
        await ctx.send("No timer running.")


bot.run('YOUR_DISCORD_BOT_TOKEN')