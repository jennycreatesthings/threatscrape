import requests
from bs4 import BeautifulSoup
import json
from termcolor import colored,  cprint 
import time

print(colored("""\

▀▀█▀▀ █░░█ █▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ ▒█▀▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀█ █▀▀ 
░▒█░░ █▀▀█ █▄▄▀ █▀▀ █▄▄█ ░░█░░ ░▀▀▀▄▄ █░░ █▄▄▀ █▄▄█ █░░█ █▀▀ 
░▒█░░ ▀░░▀ ▀░▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▒█▄▄▄█ ▀▀▀ ▀░▀▀ ▀░░▀ █▀▀▀ ▀▀▀ 

Webscraping script that scrapes data from attack.mitre.org.....by Jenius.io

 ""","red"))

print("Scraping site..")


def get_group(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

time.sleep(3)
print("Scraping site...")
time.sleep(3)
print("****************************************") 
groupArr = []
soup = get_group("https://attack.mitre.org/groups/")
for record in soup.select('tr:contains("group")'):
    groupObject = {
        "name": record.find('a').text,
        "description": record.find('p').text
        }      
    groupArr.append(groupObject)
    print (groupObject)

groupArr.append(groupObject)
with open('groupData.json', 'w') as outfile:
    json.dump(groupArr, outfile)
print("****************************************")
time.sleep(3)
print("Done")
time.sleep(3)
print("Generating threat group JSON file (groupData.json)")
time.sleep(3)
print("Complete!")

