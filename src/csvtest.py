import csv
import pprint

with open('名詞.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
    print(type(f))
