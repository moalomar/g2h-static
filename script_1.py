from hijridate import *
from datetime import *
import json


date = datetime(1924, 8, 1)
calendar = {}

while True:
    try:
        y, m, d = date.year, date.month, date.day
        if y not in calendar:
            calendar[y] = {}
        if m not in calendar[y]:
            calendar[y][m] = {}
        calendar[y][m][d] = Gregorian(y, m, d).to_hijri().isoformat()
        date = date + timedelta(days=1)
    except:
        break


with open('output_1.js', 'w') as file:
    file.write('const calendar = ' + json.dumps(calendar, separators=(',', ':')))