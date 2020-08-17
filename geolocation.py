import csv
import requests
import xlwt
from xlwt import Workbook
import time
from time import sleep
import pandas as pd

def main():
    locate()

def locate():
    locs = []
    ips = readCSVfile()
    count = 0
    total = 0
    for i in ips:
        #if count == 5:
            #count = 0
            #time.sleep(5)
        browser = requests.session()
        result = browser.get(f"https://freegeoip.app/json/{i}").json()
        count += 1
        total += 1
        print(total)
        locs.append(result)
    df = pd.DataFrame(locs)
    df.to_csv('results.csv')
def readCSVfile():
    l = []
    with open('input2.csv') as f:
        csvReader = csv.reader(f, delimiter = ',')
        for row in csvReader:
            l.append(row[3])
    return l

if __name__ == '__main__':
    main()
