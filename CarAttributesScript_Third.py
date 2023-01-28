import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

#change this with the directory of the ClassesLinks.csv file you created from second script

df = pd.read_csv(
    "D:\CMP1- Materials\Second Year\First Term\Databases\DataCollectionScripts-Hatla2y\CarClassesLinks.csv", encoding='latin1')

car_classes = df['car class'].tolist()
car_classes_links=df.link.tolist()

originallink = "https://eg.hatla2ee.com"

#can be made using dictionary
warrenty=[]
engineCapacity=[]
horsePower=[]
maxSpeed=[]
Acc=[]
Speeds=[]
Transmission=[]
year=[]
fuel=[]
liter_100km=[]
originCountry=[]
AssemblyCountry=[]
Length=[]
Width=[]
Height=[]
GroundCl=[]
wheelbase=[]
Trunksize=[]
seats=[]
tractioType=[]
NOCylinder=[]
Fueltankcapacity=[]
touqueofnewton=[]
insuranceprice=[]
RegisterPrice=[]

j=0
for link in car_classes_links:
    print("Processing row ",j)
    j+=1
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    attributes = soup.find_all(
        "div", {"class": "newCarDescriptionList v3_newCarDescriptionList"})
    ul = attributes[0].find("ul",recursive=False)
    lis = ul.findChildren("li",recursive=False)
    for li in lis:
        list=li.find("span",recursive=False)
        strong = li.find("strong",recursive=False)
        if strong==None:
            strong=li.find("a",recursive=False)
        if strong==None:
            strong = li.find("div", {"class": "insurance_text"},recursive=False).find("strong",recursive=False)
        if list==None:
            list = li.find("div", {"class": "insurance_text"},recursive=False).find("p",recursive=False)
        if list.text == "warranty":
            warrenty.append(strong.text)
        elif list.text == "Engine capacity":
            engineCapacity.append(strong.text)
        elif list.text == "Horse Power":
            horsePower.append(strong.text)
        elif list.text == "Maximum Speed":
            maxSpeed.append(strong.text)
        elif list.text == "Acceleration":
            Acc.append(strong.text)
        elif list.text == "Speeds":
            Speeds.append(strong.text)
        elif list.text == "Transmission Type":
            Transmission.append(strong.text)
        elif list.text == "Year":
            year.append(strong.text)
        elif list.text == "Fuel":
            fuel.append(strong.text)
        elif list.text == "liter/100KM":
            liter_100km.append(strong.text)
        elif list.text == "Origin Country":
            originCountry.append(strong.text)
        elif list.text == "Assembly Country":
            AssemblyCountry.append(strong.text)
        elif list.text == "Length (mm)":
            Length.append(strong.text)
        elif list.text == "Width (mm)":
            Width.append(strong.text)
        elif list.text == "Height (mm)":
            Height.append(strong.text)
        elif list.text == "Ground Clearance":
            GroundCl.append(strong.text)
        elif list.text == "Wheel Base":
            wheelbase.append(strong.text)
        elif list.text == "Trunk Size":
            Trunksize.append(strong.text)
        elif list.text == "Seats":
            seats.append(strong.text)
        elif list.text == "Traction Type":
            tractioType.append(strong.text)
        elif list.text == "Number of cylinder":
            NOCylinder.append(strong.text)
        elif list.text == "Fuel tank capacity":
            Fueltankcapacity.append(strong.text)
        elif list.text == "Torque of newton":
            touqueofnewton.append(strong.text)
        elif list.text == "Insurance Price":
            insuranceprice.append(strong.text)
        elif list.text == "Register Price":
            RegisterPrice.append(strong.text)
        
    maxlen=len(engineCapacity)
    if len(warrenty)<maxlen:
        warrenty.append("")
    if len(engineCapacity) < maxlen:
        engineCapacity.append("")
    if len(horsePower) < maxlen:
        horsePower.append("")
    if len(maxSpeed) < maxlen:
        maxSpeed.append("")
    if len(Acc) < maxlen:
        Acc.append("")
    if len(Speeds) < maxlen:
        Speeds.append("")
    if len(Transmission) < maxlen:
        Transmission.append("")
    if len(year) < maxlen:
        year.append("")
    if len(fuel) < maxlen:
        fuel.append("")
    if len(liter_100km) < maxlen:
        liter_100km.append("")
    if len(originCountry) < maxlen:
        originCountry.append("")
    if len(AssemblyCountry) < maxlen:
        AssemblyCountry.append("")
    if len(Length) < maxlen:
        Length.append("")
    if len(Width) < maxlen:
        Width.append("")
    if len(Height) < maxlen:
        Height.append("")
    if len(GroundCl) < maxlen:
        GroundCl.append("")
    if len(wheelbase) < maxlen:
        wheelbase.append("")
    if len(Trunksize) < maxlen:
        Trunksize.append("")
    if len(seats) < maxlen:
        seats.append("")
    if len(tractioType) < maxlen:
        tractioType.append("")
    if len(NOCylinder) < maxlen:
        NOCylinder.append("")
    if len(Fueltankcapacity) < maxlen:
        Fueltankcapacity.append("")
    if len(touqueofnewton) < maxlen:
        touqueofnewton.append("")
    if len(insuranceprice) < maxlen:
        insuranceprice.append("")
    if len(RegisterPrice) < maxlen:
        RegisterPrice.append("")

#for testing the results
print(len(warrenty))
print(len(engineCapacity))
print(len(horsePower))
print(len(maxSpeed))
print(len(Acc))
print(len(Speeds))
print(len(Transmission))
print(len(year))
print(len(fuel))
print(len(liter_100km))
print(len(originCountry))
print(len(AssemblyCountry))
print(len(Length))
print(len(Width))
print(len(Height))
print(len(GroundCl))
print(len(wheelbase))
print(len(Trunksize))
print(len(seats))
print(len(tractioType))
print(len(NOCylinder))
print(len(Fueltankcapacity))
print(len(touqueofnewton))
print(len(insuranceprice))
print(len(RegisterPrice))




with open(".\Attributes.csv", "w", newline='')as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Car Model", 'warranty', 'Engine capacity', 'Horse Power', 'Maximum Speed', 'Acceleration', 'Speeds', 'Transmission Type', 'Year', 'Fuel',
                'liter/100KM', 'Origin Country', 'Assembly Country', 'Length (mm)', 'Width (mm)', 'Height (mm)', 'Ground Clearance', 'Wheel Base', 'Trunk Size', 'Seats', 'Traction Type', 'Number of cylinder', 'Fuel tank capacity', 'Torque of newton', 'Insurance Price', 'Register Price'])
    for i in range(len(car_classes)):
        try:
            wr.writerow([car_classes[i], warrenty[i],engineCapacity[i][1:-1],horsePower[i],maxSpeed[i],Acc[i],Speeds[i],Transmission[i],year[i],fuel[i],liter_100km[i],originCountry[i],AssemblyCountry[i],Length[i],Width[i],Height[i],GroundCl[i],wheelbase[i],Trunksize[i],seats[i],tractioType[i][:-1],NOCylinder[i][:-1],Fueltankcapacity[i][:-1],touqueofnewton[i][:-1],insuranceprice[i],RegisterPrice[i]])
        except:
            print("error in line ", i)






