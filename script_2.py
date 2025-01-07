from hijridate import *
from datetime import *


date = datetime(1924, 8, 1)
with open('output_2.js', 'w') as file:
    file.write('calendar = {}')
    while True:
        try:
            temp = Gregorian(date.year, date.month, date.day)
            file.write(f"\ncalendar['{temp.isoformat()}'] = '{temp.to_hijri().isoformat()}'")
            date = date + timedelta(days=1)
        except:
            break
