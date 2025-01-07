from hijridate import *
from datetime import *


date = datetime(1924, 8, 1)
with open('output_4.js', 'w') as file:
    file.write('const calendar = {\n')
    while True:
        try:
            temp = Gregorian(date.year, date.month, date.day)
            file.write(f"'{temp.isoformat()}':'{temp.to_hijri().isoformat()}',\n")
            date = date + timedelta(days=1)
        except:
            file.write('}')
            break
