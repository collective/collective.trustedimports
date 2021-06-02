from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo
from collective.trustedimports.util import whitelist_module
from collective.trustedimports.util import wrap_protected
from Products.PythonScripts.Utility import allow_module
import icalendar

# from icalendar import Calendar, Event

whitelist_module("icalendar", classes=["Calendar", "Event"])
# ModuleSecurityInfo("icalendar").declarePublic("Calendar")
# allow_module("icalendar")
# allow_class(icalendar.Calendar)
# allow_class(icalendar.Event)

# wrap_protected(icalendar.Calendar.__setattr__)
# wrap_protected(icalendar.Calendar._write_)
# allow_class
# ModuleSecurityInfo("icalendar").declarePublic("Calendar")
# ModuleSecurityInfo("icalendar").declarePublic("Event")


# allow_module("icalendar.Calendar")
# allow_module("icalendar.Event")
