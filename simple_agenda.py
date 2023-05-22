# https://www.guru99.com/calendar-in-python.html

import calendar



c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatyear(2000, m=3)
print(str)
