import csv
import requests
import time
from time import sleep
import pandas as pd

def main():
    locate()

def exportCSV(locs):
    df = pd.DataFrame(locs)
    df.to_csv('results.csv')
    
def locate():
    locs = []
    ips = readCSVfile()
    count = 0
    total = 0
    for i in ips:
        #if count == 5: 
            #count = 0
            #time.sleep(5)
        #sometimes the API doesnt like the amount of requests you send it and you might
        #need to make your program sleep in order to be able to return the full list
        browser = requests.session()
        result = browser.get(f"https://freegeoip.app/json/{i}").json()
        #count += 1
        #total += 1
        #print(total)
        locs.append(result)
    exportCSV(locs)
def readCSVfile():
    l = []
    with open('input2.csv') as f:
        csvReader = csv.reader(f, delimiter = ',')
        for row in csvReader:
            l.append(row[3]) #change this to whatever row your ips are in
    return l

if __name__ == '__main__':
    main()
