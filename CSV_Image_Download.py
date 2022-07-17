"""
Python script that downloads pictures from a csv column and converts them into .jpg pictures.
Uses pandas for csv reading, regular expressions for file endings and shutil for image conversions
"""
import pandas as pd
import requests
import shutil
import re
count = -1

def pic_request(url):
    global count
    url = str(url)
    print(url)
    count = count + 1
    file = "woo_komplett_http.csv"
    data = pd.read_csv(file, sep=";", encoding_errors="ignore")
    print(data["Artikelnummer"][count])
    try:
        filename = str(data["Artikelnummer"][count]) + re.findall("\..{3,4}?\Z", url)[0]
        res = requests.get(url, stream=True)
        if res.status_code == 200:
            with open(filename, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image successfully Downloaded: ', filename)
    except IndexError:
        print("Index-Error, Continuing")


file = "woo_komplett_http.csv"
data = pd.read_csv(file, sep=";", encoding_errors="ignore")
print(data)
data['Bilder'] = data['Bilder'].apply(lambda x: pic_request(x))
data.to_csv('CSV.csv', sep=";", errors="ignore")
print(data)
while True:
    inp = input("Success!\nEnter 'q' to quit")
    quit()
