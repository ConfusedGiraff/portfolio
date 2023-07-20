import datetime as dt
import math
import time
import win32com.client

your_email = 'your.email@gmail.com'
exclude = ['Lunch', 'Focus Time', 'timecard', 'Gym Time'] # list the names of meetings you don't want to include

# Gets info from your outlook calendar
def get_calendar(begin,end,exclude):
    outlook = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')
    calendar = outlook.getDefaultFolder(9).Items
    calendar.IncludeRecurrences = True
    calendar.Sort('[Start]')
    restriction = "[Start] >= '" + begin.strftime('%m/%d/%Y') + "' AND [END] <= '" + end.strftime('%m/%d/%Y') + "'"
    calendar = calendar.Restrict(restriction) 
    categories = {}
    for c in calendar:
        if c.subject not in exclude:
            starttime = c.start.strftime("%d/%m/%Y %H:%M")
            endtime = c.end.strftime("%d/%m/%Y %H:%M")
            time_diff = (time.mktime(dt.datetime.strptime(endtime, "%d/%m/%Y %H:%M").timetuple())) - (time.mktime(dt.datetime.strptime(starttime, "%d/%m/%Y %H:%M").timetuple()))
            time_diff = (time_diff//60)/60
            time_diff = math.ceil(time_diff)
            #time_diff = round(time_diff * 2) / 2
            categories.setdefault(c.Categories, 0)
            categories[c.Categories] += time_diff
                

    return categories

# Writes a text file that lists how many hours you spent on a given activity based on how you categorize your meetings
now = dt.datetime.now()
monday = now - dt.timedelta(days = now.weekday())
begin = dt.datetime(monday.year, monday.month, monday.day)
one_week = monday + dt.timedelta(days=5)
end = dt.datetime(one_week.year, one_week.month, one_week.day)
text = f'Hours for the week of {monday}\n'
for k, v in get_calendar(begin, end, exclude).items():
    text += f'{v} {k}\n'

with open('timecard_assistant.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print(text)