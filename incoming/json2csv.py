import json
import csv

f = open('maestro')
data = json.load(f)
f.close()

f=csv.writer(open('test.csv','wb+'))

for item in data:
    f.writerow([item['pk'], item['model']] + item['fields'].values())
