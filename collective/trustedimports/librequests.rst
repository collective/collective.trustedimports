We can make a get request using the requests library
>>> import requests
>>> response = requests.get("https://example.com")
>>> response
<Response [200]>
>>> "Example Domain" in response.content
True

We can also make a post request
>>> import requests
>>> response = requests.post("https://postman-echo.com/post", data={"post_data": "This is expected to be sent back as part of response body."})
>>> response
<Response [200]>
>>> response.json()["json"]["post_data"]
u'This is expected to be sent back as part of response body.'


#TODO Add tests for allowlist and blocklist behaviour using requests