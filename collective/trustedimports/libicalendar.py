from collective.trustedimports.util import whitelist_module
import icalendar
from icalendar import Calendar, Event

whitelist_module("icalendar", classes=["Calendar", "Event"])
