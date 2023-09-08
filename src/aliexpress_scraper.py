import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'universal_ecommerce',
    'url': 'https://www.aliexpress.com/w/wholesale-laptop.html?catId=0&initiative_id=SB_20230907055110&SearchText=laptop&spm=a2g0o.best.1000002.0',
    'user_agent_type': 'desktop',
    'render': 'html',
    'geo_location': 'Germany'
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('USERNAME', 'PASSWORD'), #Your credentials go here
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())
