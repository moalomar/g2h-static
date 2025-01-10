from hijridate import *
from datetime import *
from json import *
import re


calendar = {}
current = datetime(1924, 8, 1)
while True:
    try:
        y, m, d = current.year, current.month, current.day
        if y not in calendar:
            calendar[y] = {}
        if m not in calendar[y]:
            calendar[y][m] = {}
        calendar[y][m][d] = Gregorian(y, m, d).to_hijri().isoformat().replace('-', '')[1:]
        current = current + timedelta(days=1)
    except:
        break


calendar = re.sub(r'["\'](\w+)["\']\s*:', r'\1:', dumps(calendar, separators=(',', ':')))
with open('optimal.js', 'w') as file:
    file.write(f'const CALENDAR={calendar}')
