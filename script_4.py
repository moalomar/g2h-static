from hijridate import *
from datetime import *


with open('output_4.js', 'w') as file:
    file.write("const calendar = {'1924-08-01':'1343-01-01'")
    date = datetime(1924, 8, 1)
    while True:
        try:
            temp = Gregorian(date.year, date.month, date.day)
            file.write(f",'{temp.isoformat()}':'{temp.to_hijri().isoformat()}'")
            date = date + timedelta(days=1)
        except:
            file.write('}')
            break
