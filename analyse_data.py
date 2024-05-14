'''
order by most common date
order by most common day
order by most common time
order by most common duration
'''

import json
from pprint import pprint
from collections import Counter
import matplotlib.pyplot as plt
from datetime import datetime, date, time

with open('exam_timetable_result.json', 'r') as f:
    data = json.load(f)

def order_by_category(data, category):
    categories = [entry[category] for entry in data]
    return Counter(categories).most_common()

most_common_dates = order_by_category(data, 'date')
most_common_days = order_by_category(data, 'day')
most_common_times = order_by_category(data, 'time')
most_common_durations = order_by_category(data, 'duration')

# print results
print('Most common dates:')
pprint(most_common_dates)
print('Most common days:')
pprint(most_common_days)
print('Most common times:')
pprint(most_common_times)
print('Most common durations:')
pprint(most_common_durations)

fig = plt.figure(figsize=(10, 10))

# format data for plt
ax1 = fig.add_subplot(221)
most_common_dates = [(datetime.strptime(entry[0], "%d/%m/%Y"), entry[1]) for entry in most_common_dates]
most_common_dates.sort(key=lambda x: x[0])
plt.bar([entry[0] for entry in most_common_dates], [entry[1] for entry in most_common_dates])
plt.xticks([entry[0] for entry in most_common_dates], rotation=90)
ax1.title.set_text('Most common dates')

order_days = {
    'Mon': 0,
    'Tue': 1,
    'Wed': 2,
    'Thu': 3,
    'Fri': 4
}
ax2 = fig.add_subplot(222)
most_common_days.sort(key=lambda x: order_days[x[0]])
plt.bar([entry[0] for entry in most_common_days], [entry[1] for entry in most_common_days])
plt.xticks(rotation=90)
ax2.title.set_text('Most common days')

ax3 = fig.add_subplot(223)
most_common_times.sort(key=lambda x: time.fromisoformat(x[0]))
plt.bar([entry[0] for entry in most_common_times], [entry[1] for entry in most_common_times])
plt.xticks(rotation=90)
ax3.title.set_text('Most common times')

ax4 = fig.add_subplot(224)
most_common_durations.sort(key=lambda x: time.fromisoformat(x[0]))
plt.bar([entry[0] for entry in most_common_durations], [entry[1] for entry in most_common_durations])
plt.xticks(rotation=90)
ax4.title.set_text('Most common durations')

plt.tight_layout()
plt.show()