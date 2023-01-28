import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

car_brands = []
car_models = []
links = []
detailed_models_links=[]

total_car_models = []


originallink = "https://eg.hatla2ee.com"
result = requests.get("https://eg.hatla2ee.com/en/new-car")
src = result.content
soup = BeautifulSoup(src, "lxml")

car_brands_ul = soup.find_all("ul", {"class": "unitChose topBrands"})[0]
brands = car_brands_ul.findChildren("li", recursive=False)
for i in brands:
    a = i.findChildren("a", recursive=False)
    links.append(originallink+a[0].attrs['href'])
    text = a[0].text[2:-1]
    car_brands.append(text)

car_brands_ul = soup.find_all("div", {"class": "MoreContent"})[0]
brands = car_brands_ul.findChildren("li", recursive=False)
for i in brands:
    a = i.findChildren("a", recursive=False)
    links.append(originallink + a[0].attrs['href'])
    text = a[0].text[2:-1]
    car_brands.append(text)



for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    titles = soup.find_all("a", {"class": "nCarListData_title"})
    car_models.append(titles)


for car in car_models:
    for model in car:
        detailed_models_links.append(originallink+model.attrs['href'])
        text = model.contents[0][1:-1]
        total_car_models.append(text)





data_file = [total_car_models, detailed_models_links]
exported = zip_longest(*data_file)

with open(".\CarModelLinks.csv", "w", newline='')as myfile:
    wr = csv.writer(myfile)
    wr.writerow(['Car Model','link'])
    wr.writerows(exported)


