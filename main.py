from nextcord.ext import commands
import requests, json, random, datetime, asyncio
import discord
import os


bot = commands.Bot(command_prefix="Water ")


@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Hello!')


async def schedule_daily_message():
    while True:
        now = datetime.datetime.now()
        #then = now+datetime.timedelta(days=0)
        then = now.replace(hour=15, minute=1)
        wait_time = (then - now).total_seconds()
        await asyncio.sleep(3600)

        channel = bot.get_channel(931040113146871822)

        await channel.send("Heyy Kiv have some water")

async def schedule_daily_message2():
    while True:
        now = datetime.datetime.now()
        #then = now+datetime.timedelta(days=0)
        then = now.replace(hour=15, minute=1)
        wait_time = (then - now).total_seconds()
        await asyncio.sleep(7200)

        channel = bot.get_channel(931040113146871822)

        await channel.send("Eat fruits and stay healthy kivv")

        
async def schedule_daily_message3():
    while True:
        now = datetime.datetime.now()
        #then = now+datetime.timedelta(days=0)
        then = now.replace(hour=15, minute=1)
        wait_time = (then - now).total_seconds()
        await asyncio.sleep(18000)

        channel = bot.get_channel(931040113146871822)

        await channel.send("You are cute and mine kiv - mish")
        
@bot.event
async def on_ready():
    print(f"Loggined in as: {bot.user.name}")
    await schedule_daily_message()
    await schedule_daily_message2()
    await schedule_daily_message3()



if __name__ == '__main__':
    bot.run(os.environ['DISCORD_TOKEN'])
