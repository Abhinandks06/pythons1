import csv
with open("detail.csv","r") as f:
    r=csv.reader(f)
    count=1
    try:
        with open("hw1.csv", "w") as f:
            w=csv.writer(f)
            for i in r:
                if(count==13):
                    break
                else:
                    w.writerow(i)
                    count=count+1
    except IOError:
        print("Input Output ERROR......")

p=csv.DictReader(open("hw1.csv"))
print("First five lines")
print("************************")
for i in p:
    print(i)