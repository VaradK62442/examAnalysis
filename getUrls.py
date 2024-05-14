'''
python program to get names of all URLs from 
`https://www.gla.ac.uk/myglasgow/registry/exams/examtimetables/#april%2Fmay2024examtimetable`
of exam timetables for all schools
save them to a file named `urls.txt`
'''

import requests
from bs4 import BeautifulSoup

URL = "https://www.gla.ac.uk/myglasgow/registry/exams/examtimetables/#april%2Fmay2024examtimetable"
DOMAIN = "https://www.gla.ac.uk"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

timetable_list = soup.find_all('ul')[8] # 8th ul tag contains all the links
timetable_links = [link['href'] for link in timetable_list.find_all('a', href=True)]

with open('urls.txt', 'w') as f:
    for link in timetable_links:
        f.write(DOMAIN + link + '\n')
