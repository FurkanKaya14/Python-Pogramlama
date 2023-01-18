#csv_okuma
import csv
with open('iris.data', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
#csv_yazma
import csv
baslik = ["sicaklik", "nem", "basinc"]
veri = [[30, 75.5, 10], [32.3, 50, 3]]
with open('sensor_veri.csv',
          'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(baslik)
    writer.writerows(veri)

#pandas
import pandas as pd

veri = pd.read_csv("iris.data")

print(veri.head())

print(veri.columns)

print(veri[3:5])

veri = veri.sort_values(by="sepal_length")
print(veri.head())

toplam_veri = veri["sepal_length"].sum()
ortalama_veri = veri["sepal_length"].mean()
ortanca_veri = veri["sepal_length"].median()

print("Sum:", toplam_veri,
      "\nMean:", ortalama_veri,
      "\nMedian:", ortanca_veri)
