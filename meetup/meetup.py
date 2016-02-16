from datetime import date
import calendar

def meetup_day(year, month, weekday, nth):
    min = 1
    max = calendar.monthrange(year, month)[1]
    if nth == 'teenth':
        min = 13
        max = 19
    elif nth == '1st':
        max = 7
    elif nth == '2nd':
        min = 8
        max = 14
    elif nth == '3rd':
        min = 15
        max = 21
    elif nth == '4th':
        min = 22
        max = 28
    elif nth == '5th':
        if max<29:
            raise MeetupDayException('There is no 5th '+weekday+' in this month')
        min = 29
    elif nth == 'last':
        min = max-6

    for i in range(min, max+1):
        test_date = date(year, month, i)
        if calendar.day_name[test_date.weekday()] == weekday:
            return test_date

class MeetupDayException(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)
