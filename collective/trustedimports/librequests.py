from AccessControl import (
    allow_class,
    ModuleSecurityInfo,
)

import requests

ModuleSecurityInfo("requests").declarePublic("get")
ModuleSecurityInfo("requests").declarePublic("post")
allow_class(requests.models.Response)
