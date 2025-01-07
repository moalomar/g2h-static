from hijridate import *
from datetime import *


with open('output_301.js', 'w') as file:
    file.write('const calendar = {\n')
    date = datetime(1924, 8, 1)
    while True:
        try:
            temp = Gregorian(date.year, date.month, date.day)
            file.write(f"""    '{temp.isoformat()}' : '{temp.to_hijri().isoformat()}',\n""")
            date = date + timedelta(days=1)
        except:
            file.write('}')
            break
