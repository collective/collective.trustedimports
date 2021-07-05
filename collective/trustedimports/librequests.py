from collective.trustedimports.util import wrap_protected, is_url_allowed
from AccessControl import (
    allow_class,
    ModuleSecurityInfo,
)

import requests

wrap_protected(requests.get, lambda url: is_url_allowed(url))
wrap_protected(requests.post, lambda url: is_url_allowed(url))
allow_class(requests.models.Response)
