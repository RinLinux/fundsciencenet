# -*- coding: utf-8 -*-

import csv
import json

with open('xxx.json', 'r',encoding = 'UTF-8') as f:
    rows = json.load(f)

f = open('data.csv', 'w',encoding = 'UTF-8',newline='')
csv_write = csv.writer(f)
csv_write.writerow(rows[0].keys())

for row in rows:
    csv_write.writerow(row.values())

f.close()