# AliExpress Scraper

[![Oxylabs promo code](https://raw.githubusercontent.com/oxylabs/product-integrations/refs/heads/master/Affiliate-Universal-1090x275.png)](https://oxylabs.io/pages/gitoxy?utm_source=877&utm_medium=affiliate&groupid=877&utm_content=aliexpress-scraper-github&transaction_id=102f49063ab94276ae8f116d224b67)

[![](https://dcbadge.limes.pink/api/server/Pds3gBmKMH?style=for-the-badge&theme=discord)](https://discord.gg/Pds3gBmKMH) [![YouTube](https://img.shields.io/badge/YouTube-Oxylabs-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@oxylabs)

[<u>AliExpress Scraper</u>](https://oxylabs.io/products/scraper-api/ecommerce/aliexpress) is a tool designed to collect public product data
from AliExpress on a large scale. This short tutorial will show you how
to scrape AliExpress with Oxylabs’ Scraper API.

## How it works

You can extract AliExpress data by sending a request to our API with
URLs you want to scrape. Our service will send back the HTML, parsed JSON, or Markdown output of any
AliExpress page.

### Python code example

This sample showcases how to make an API request and retrieve the HTML
of AliExpress search results for the keyword “laptop”:

```python
import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'universal',
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

```

See the
[<u>documentation</u>](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/all-domains)
for more code samples.

### Output sample

```json
{
  "results": [
    {
      "content": "<!doctype html>\n<html lang=\"en\">\n<head>
      ...
      </script></body>\n</html>\n",
      "created_at": "2023-09-07 14:04:18",
      "updated_at": "2023-09-07 14:04:42",
      "page": 1,
      "url": "https://www.aliexpress.com/w/wholesale-laptop.html?catId=0&initiative_id=SB_20230907055110&SearchText=laptop&spm=a2g0o.best.1000002.0",
      "job_id": "7105551359235115009",
      "status_code": 200
    }
  ]
}
```

The data harvesting process is significantly easier with Oxylabs’
AliExpress Scraper API. You can collect details such as pricing,
reviews, product information, and other public data. If you have any
questions, you can contact us via [<u>live
chat</u>](https://oxylabs.io/) or
[<u>email</u>](mailto:support@oxylabs.io).

Also, check this tutorial on [pypi](https://pypi.org/project/ali-express-scraper/)
