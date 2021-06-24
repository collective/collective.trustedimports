icalendar
=========

I can import icalendar and it's classes

>>> teval("import icalendar")

>>> teval("from icalendar import Calendar, Event, Todo, Journal, FreeBusy, Timezone, TimezoneStandard, TimezoneDaylight, Alarm")

I can construct a new Calendar

>>> teval("from icalendar import Calendar; return Calendar()")
VCALENDAR({})

I can add properties to the calendar by using the `add` function

>>> teval("from icalendar import Calendar; cal = Calendar(); cal.add('summary', 'Python meeting about calendaring'); cal.add('attendee', 'MAILTO:maxm@mxm.dk'); cal.add('attendee', 'MAILTO:test@example.com'); return cal")
VCALENDAR({u'ATTENDEE': [vCalAddress('MAILTO:maxm@mxm.dk'), vCalAddress('MAILTO:test@example.com')], u'SUMMARY': vText('Python meeting about calendaring')})

But properties can't be added to the calendar by using the slice syntax (`[value] = new_value`)

>>> teval("from icalendar import Calendar; cal = Calendar(); cal['summary'] = 'Python meeting about calendaring'; cal['attendee'] = ['MAILTO:maxm@mxm.dk','MAILTO:test@example.com']; return cal")
Traceback (most recent call last):
...
TypeError: object does not support item or slice assignment

I can generate an ical string from the icalendar object

>>> teval("from icalendar import Calendar; cal = Calendar(); cal.add('summary', 'Python meeting about calendaring'); cal.add('attendee', 'MAILTO:maxm@mxm.dk'); cal.add('attendee', 'MAILTO:test@example.com'); return cal.to_ical()")
'BEGIN:VCALENDAR\r\nATTENDEE:MAILTO:maxm@mxm.dk\r\nATTENDEE:MAILTO:test@example.com\r\nSUMMARY:Python meeting about calendaring\r\nEND:VCALENDAR\r\n'