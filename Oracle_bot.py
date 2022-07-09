import discord
import os
import requests
import json

TOKEN = #thats the bot token 
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = message.content
    channel = message.channel.name
    print(f"{username}: {user_message} ({channel})") 

    if message.author == client.user:
        return

    if message.content.startswith('>hello'):
        await message.channel.send(f"Hello {username}")

    if message.channel.name == 'get-inspired':
        if message.content.startswith('>inspire'):
            quote = get_quote()
            await message.channel.send(quote)
    else:
        if message.content.startswith(">inspire"):
            await message.channel.send("I do not inspire here, you need to type it on #get-inspired")

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "*" + json_data[0]['q'] + "* \n**" + json_data[0]["a"] + "**"
    return(quote)


client.run(TOKEN)
