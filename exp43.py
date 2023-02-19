import csv
c=['ID','NAME','AGE']
d=[{'ID':1,'NAME':'a','AGE':21},
   {'ID':2,'NAME':'b','AGE':20},
   {'ID':3,'NAME':'c','AGE':23},
   {'ID':4,'NAME':'d','AGE':19},
   {'ID':5,'NAME':'e','AGE':22},
   {'ID':6,'NAME':'f','AGE':21},
   {'ID':7,'NAME':'g','AGE':18},
   {'ID':8,'NAME':'h','AGE':25},
   {'ID':9,'NAME':'i','AGE':19},
   {'ID':10,'NAME':'j','AGE':21},
   {'ID':11,'NAME':'k','AGE':20}]
try:
    with open("detail.csv","w") as f:
        w=csv.DictWriter(f,fieldnames=c)
        w.writeheader()
        for i in d:
            w.writerow(i)
except IOError:
    print("Input Output ERROR......")
p=csv.DictReader(open("detail.csv"))
print("CSV file output")
print("************************")
for i in p:
    print(i)
