from hijridate import *
from datetime import *


with open('calendar.js', 'w') as file:
    file.write('const CALENDAR = {\n')
    current = datetime(1924, 8, 1)
    while True:
        try:
            temp = Gregorian(current.year, current.month, current.day)
            file.write(f'    "{temp.isoformat()}" : "{temp.to_hijri().isoformat()}",\n')
            current = current + timedelta(days=1)
        except:
            file.write('}')
            break
