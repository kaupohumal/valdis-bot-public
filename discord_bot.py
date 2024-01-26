import discord
from discord.ext import commands
import sys
import requests
import os
import markovify
import logging

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.DEBUG)

description = "Kuradi neandertaalid raisk."
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='/', description=description, intents=intents)

TEXT_MODELS = {}
texts = os.listdir('corpus/')
for t in texts:
    f = open('corpus/' + t, 'r', encoding='utf-8')
    TEXT_MODELS[t] = markovify.NewlineText(f, state_size=2 ,well_formed = False)
    f.close()

@bot.event
async def on_ready():
    activity = discord.Game(name="Peksab karvaseid vitupäid", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    logging.info("~~ Logged in ~~")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if bot.user.mentioned_in(message):
        logging.debug(f"Bot mentioned")
        await message.channel.send(TEXT_MODELS['valdis.txt'].make_sentence(tries=100))

@bot.command()
async def parrot(ctx, repeat: int, message="squawk!"):
    logging.debug(f"Received command \"parrot\"")
    for i in range(0, repeat):
        await ctx.send(message)

@bot.command()
async def wikipedia(ctx):
    logging.debug(f"Received command \"wikipedia\"")
    r = requests.get("https://en.wikipedia.org/wiki/special:random")
    await ctx.send(r.url)

@bot.command()
async def imitate(ctx, person):
    logging.debug(f"Received command \"imitate\" with parameter: \"{person}\"")
    if person + '.txt' in TEXT_MODELS:
        await ctx.send(f"{TEXT_MODELS[person + '.txt'].make_sentence(tries=100)}")
    else:
        await("Sorry, I don't know anyone by that name.")


bot.run(os.getenv("DISCORD_API_KEY"))