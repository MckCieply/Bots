from bs4 import BeautifulSoup 
import requests

url = "https://www.formula1.com/en/results.html/2022/drivers.html" 
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
table = doc.find("table")
td = table.find_all("td")
driver = table.find_all("span")
counter = 0
for i in range (147):
    if td[i].string is not None:
        print(td[i].string, end = " ")
        counter +=1
        if counter == 3:
            print("\n") 
            counter = 0
for i in range(63):
    if driver[i].string is not None:
        print(driver[i].string, end = " ")
        counter += 1
        if counter == 3:
            print("\n") 
            counter = 0
# tabela = doc.find("table")
# print(tabela)
    
