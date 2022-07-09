from bs4 import BeautifulSoup 
import requests

url = "https://www.formula1.com/en/results.html/2022/drivers.html" 
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print()
for tr in doc.find_all('tr')[1:]:
    first_name = tr.find('span', class_="hide-for-tablet").string
    last_name = tr.find('span', class_ = "hide-for-mobile").string
    car = tr.find('a', class_ = "grey semi-bold uppercase ArchiveLink").string
    points = tr.find('td', class_ = "dark bold").string
    print(f"""Driver: {first_name} {last_name}
    Car: {car}
    POINTS: {points}""")

    #Git_Commit
