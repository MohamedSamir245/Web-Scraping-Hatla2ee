import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

#change this with the directory of the data.csv file you created from first script
df = pd.read_csv(
    "D:\CMP1- Materials\Second Year\First Term\Databases\DataCollectionScripts-Hatla2y\CarModelLinks.csv", encoding='latin1')

model_links = df.link.tolist()
originallink = "https://eg.hatla2ee.com"

total_classes = []
total_classes_links = []

for i in range(len(model_links)-1):
    if i >= (len(model_links)-1):
        break
    if model_links[i] == model_links[i+1]:
        model_links.pop(i+1)

for link in model_links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    classes = soup.find_all("div", {"class": "newCarPricesItemBody"})
    for i in range(len(classes)-1):
        table = classes[i].find("table", recursive=False)
        tbody = table.find("tbody", recursive=False)
        trs = tbody.findChildren("tr", recursive=False)
        for tr in trs:
            tds = tr.findChildren("td", recursive=False)
            a = tds[0].find("a")
            if a != None:
                l = a.attrs['href']
                total_classes_links.append(originallink+l)
                total_classes.append(a.text)


with open(".\CarClassesLinks.csv", "w", newline='')as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["car class",'link'])
    for i in range(len(total_classes)):
        try:
            wr.writerow([total_classes[i],total_classes_links[i]])
        except:
            print("error in line ",i,"\n")
