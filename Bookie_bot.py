import discord

from urllib.request import urlopen

#TOKEN = ""
url = "https://www.formula1.com/en/results.html/2022/drivers.html"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
#client = discord.Client()
table_index = html.find("<table")
start_index = table_index + len('<table class="resultsarchive-table">')
end_index = html.find("</table")
#print(html[start_index:end_index])  

def standings():
    x = 1
    for x in range(10):
        table_index = html.find('dark">')
        start_index = table_index + len('dark">')
        end_index = html.find("</td>")
        print(html[start_index:end_index])
standings()
#client.run(TOKEN)