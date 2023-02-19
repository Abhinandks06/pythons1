import csv
with open("dep.csv",newline='') as f:
    d=csv.DictReader(f)
    print("Data_value Subject")
    print("******************")
    for i in d:
        print(i['Data_value'],i['Subject'])