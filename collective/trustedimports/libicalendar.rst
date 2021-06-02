icalendar
=========

I can import icalendar and it's classes

>>> import icalendar

>>> from icalendar import Calendar, Event

I can construct a new Calendar

>>> cal = Calendar()
>>> print(cal)
VCALENDAR({})

I can add properties to the calendar

>>> cal['dtstart'] = '20050404T080000'
>>> cal['summary'] = 'Python meeting about calendaring'

I can convert the calendar to a string

>>> cal.to_ical()
'BEGIN:VCALENDAR\r\nDTSTART:20050404T080000\r\nSUMMARY:Python meeting about calendaring\r\nEND:VCALENDAR\r\n'
