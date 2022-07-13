import discord
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

TOKEN = ""
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = message.content
    channel = message.channel.name

    if message.author == client.user:
        return 
    
    if message.content.startswith('>hello'):
        await message.channel.send(f"Hello {username}")

    if message.content.startswith('>f1'):
        standings()
        await message.channel.send(f"""
        1.{list[0].get('first_name')} {list[0].get('last_name')} \n Bolid: {list[0].get('car')} \n Punkty: ***{list[0].get('points')}***\n 
2. {list[1].get('first_name')} {list[1].get('last_name')} \n Bolid: {list[1].get('car')} \n Punkty: ***{list[1].get('points')}*** \n
3. {list[2].get('first_name')} {list[2].get('last_name')} \n Bolid: {list[2].get('car')} \n Punkty: ***{list[2].get('points')}*** \n
4. {list[3].get('first_name')} {list[3].get('last_name')} \n Bolid: {list[3].get('car')} \n Punkty: ***{list[3].get('points')}*** \n
5. {list[4].get('first_name')} {list[4].get('last_name')} \n Bolid: {list[4].get('car')} \n Punkty: ***{list[4].get('points')}*** \n
6. {list[5].get('first_name')} {list[5].get('last_name')} \n Bolid: {list[5].get('car')} \n Punkty: ***{list[5].get('points')}*** \n
7. {list[6].get('first_name')} {list[6].get('last_name')} \n Bolid: {list[6].get('car')} \n Punkty: ***{list[6].get('points')}*** \n
8. {list[7].get('first_name')} {list[7].get('last_name')} \n Bolid: {list[7].get('car')} \n Punkty: ***{list[7].get('points')}*** \n
9. {list[8].get('first_name')} {list[8].get('last_name')} \n Bolid: {list[8].get('car')} \n Punkty: ***{list[8].get('points')}*** \n
10. {list[9].get('first_name')} {list[9].get('last_name')} \n Bolid: {list[9].get('car')} \n Punkty: ***{list[9].get('points')}***\n 
        """)

def standings():
    url = "https://www.formula1.com/en/results.html/2022/drivers.html" 
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    global standings_list
    standings_list = []
    global list
    list = []
    for tr in doc.find_all('tr')[1:]:
        first_name = tr.find('span', class_="hide-for-tablet").string
        last_name = tr.find('span', class_ = "hide-for-mobile").string
        car = tr.find('a', class_ = "grey semi-bold uppercase ArchiveLink").string
        points = tr.find('td', class_ = "dark bold").string
        dict = {"first_name": first_name,
                "last_name": last_name,
                "car": car,
                "points": points}
        list.append(dict)
def one_driver():
    position = int(input("Input which position youd like to check: "))
    print(standings_list[position-1])



client.run(TOKEN)
