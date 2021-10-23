import os
import json
import requests
import random
#import discord
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix = "!")
#client = discord.Client()

@client.event
async def on_ready():
  print("Beep bop bot is ready.")

@client.command()
async def doggo(ctx):
  dog_api = requests.get("https://dog.ceo/api/breeds/image/random")
  json_dog_data = json.loads(dog_api.text)
  image_link = json_dog_data["message"]
  await ctx.send(image_link)

@client.command()
async def pet(ctx):
  dog_behavior = ["woof", "bark", "*dog noise*", "growl"]
  await ctx.send(random.choice(dog_behavior))

@client.command()
async def specific_doggo(ctx, *, input):
  input = input.lower()
  dog_api = requests.get("https://dog.ceo/api/breed/{0}/images/random".format(input))
  json_dog_data = json.loads(dog_api.text)
  image_link = json_dog_data["message"]
  await ctx.send(image_link)

keep_alive()

client.run(os.getenv("TOKEN")) #the token can be found in your developer portal