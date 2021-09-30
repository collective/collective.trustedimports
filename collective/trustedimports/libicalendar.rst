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

pytz
====

I can use pytz for timezone functions. These examples all come from the pytz docs https://pypi.org/project/pytz/

>>> from datetime import datetime, timedelta
>>> from pytz import timezone
>>> import pytz
>>> utc = pytz.utc
>>> utc.zone
'UTC'

>>> eastern = timezone('US/Eastern')
>>> eastern.zone
'US/Eastern'

>>> amsterdam = timezone('Europe/Amsterdam')
>>> fmt = '%Y-%m-%d %H:%M:%S %Z%z'
>>> loc_dt = eastern.localize(datetime(2002, 10, 27, 6, 0, 0))
>>> print(loc_dt.strftime(fmt))
2002-10-27 06:00:00 EST-0500

>>> ams_dt = loc_dt.astimezone(amsterdam)
>>> ams_dt.strftime(fmt)
'2002-10-27 12:00:00 CET+0100'

>>> utc_dt = datetime(2002, 10, 27, 6, 0, 0, tzinfo=utc)
>>> loc_dt = utc_dt.astimezone(eastern)
>>> loc_dt.strftime(fmt)
'2002-10-27 01:00:00 EST-0500'

>>> before = loc_dt - timedelta(minutes=10)
>>> before.strftime(fmt)
'2002-10-27 00:50:00 EST-0500'
>>> eastern.normalize(before).strftime(fmt)
'2002-10-27 01:50:00 EDT-0400'
>>> after = eastern.normalize(before + timedelta(minutes=20))
>>> after.strftime(fmt)
'2002-10-27 01:10:00 EST-0500'

>>> utc_dt = utc.localize(datetime.utcfromtimestamp(1143408899))
>>> utc_dt.strftime(fmt)
'2006-03-26 21:34:59 UTC+0000'
>>> au_tz = timezone('Australia/Sydney')
>>> au_dt = utc_dt.astimezone(au_tz)
>>> au_dt.strftime(fmt)
'2006-03-27 08:34:59 AEDT+1100'
>>> utc_dt2 = au_dt.astimezone(utc)
>>> utc_dt2.strftime(fmt)
'2006-03-26 21:34:59 UTC+0000'
>>> utc_dt == utc_dt2
True
