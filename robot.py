import discord, json
from aiohttp import request
from discord.ext import commands


with open("token.json") as token:
    token = json.load(token)

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!")

#client = discord.Client()

@bot.event
async def on_ready():
    print ('We have logged in as {0.user}'.format(bot))

@bot.command()
async def ping(ctx):
	await ctx.channel.send("pong")

@bot.command(name = "fact")
async def animal_fact(ctx):
    URL = "https://some-random-api.ml/animal/dog"
    
    async with request("GET", URL, headers=[]) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(data["fact"])

        else: 
            await ctx.send(f"API returned a {response.status} status.")

bot.run(token)