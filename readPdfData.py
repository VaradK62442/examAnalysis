# program to read in pdf files in downloads/
# extract date, time, school, subject, location, and exam type from each pdf
# store in JSON file

from pypdf import PdfReader
import glob
from pprint import pprint
import re
import json

pdf_files = glob.glob('downloads/*.pdf')

DAY = re.compile(r'Mon|Tue|Wed|Thu|Fri')
DATE = re.compile(r'\d{2}/\d{2}/\d{4}')
TIME_AND_DURATION = re.compile(r'\d{2}:\d{2} \d{2}:\d{2}')

# first four entries in first page is table headings
# incorrect actually ^
# use regex to find the first time a time appears in the string, start from there

results = []
for pdf in pdf_files:
    reader = PdfReader(pdf)
    for page in reader.pages:
        text_list = page.extract_text().split('\n')
        for text in text_list:
            if TIME_AND_DURATION.search(text):
                time, duration = TIME_AND_DURATION.search(text).group().split()
                day = DAY.search(text).group()
                date = DATE.search(text).group()
                results.append({
                    'time': time,
                    'duration': duration,
                    'day': day,
                    'date': date
                })

# write to json
with open('exam_timetable_result.json', 'w') as f:
    json.dump(results, f, indent=4)