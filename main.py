from nextcord.ext import commands
import requests, json, random, datetime, asyncio
import discord
import os


bot = commands.Bot(command_prefix="/")


@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Hello!')


async def schedule_daily_message():
    while True:
        now = datetime.datetime.now()
        #then = now+datetime.timedelta(days=0)
        then = now.replace(hour=10, minute=1)
        wait_time = (then - now).total_seconds()
        await asyncio.sleep(wait_time)

        channel = bot.get_channel(931040113146871822)

        await channel.send("Heyy Kiv have some water")


@bot.event
async def on_ready():
    print(f"Loggined in as: {bot.user.name}")
    await schedule_daily_message()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))



if __name__ == '__main__':
    bot.run(os.environ['DISCORD_TOKEN'])
