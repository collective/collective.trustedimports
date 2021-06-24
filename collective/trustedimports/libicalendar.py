from collective.trustedimports.util import whitelist_module

whitelist_module(
    "icalendar",
    classes=[
        "Calendar",
        "Event",
        "Todo",
        "Journal",
        "FreeBusy",
        "Timezone",
        "TimezoneStandard",
        "TimezoneDaylight",
        "Alarm",
    ],
)
