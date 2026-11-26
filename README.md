# AliExpress Scraper

[![Oxylabs promo code](https://raw.githubusercontent.com/oxylabs/product-integrations/refs/heads/master/Affiliate-Universal-1090x275.png)](https://oxylabs.io/pages/gitoxy?utm_source=github&utm_medium=referral&utm_content=aliexpress-scraper&utm_campaign=banner&groupid=877)

<p align="left">
  <a href="https://dashboard.oxylabs.io"><img src="https://img.shields.io/badge/%F0%9F%9A%80_Get_Started-FF6B35?style=for-the-badge" alt="Get started"></a>
  <a href="https://developers.oxylabs.io/products/web-api"><img src="https://img.shields.io/badge/%F0%9F%93%9A_Documentation-4A90E2?style=for-the-badge" alt="Documentation"></a>
  <a href="https://dashboard.oxylabs.io"><img src="https://img.shields.io/badge/%F0%9F%93%8A_Dashboard-2EA44F?style=for-the-badge" alt="Dashboard"></a>
  <a href="https://discord.gg/Pds3gBmKMH"><img src="https://img.shields.io/badge/%F0%9F%92%AC_Discord-5865F2?style=for-the-badge" alt="Discord"></a>
  <a href="https://www.youtube.com/@oxylabs"><img src="https://img.shields.io/badge/%E2%96%B6%EF%B8%8F_YouTube-FF0000?style=for-the-badge" alt="YouTube"></a>
</p>

[<u>AliExpress Scraper</u>](https://oxylabs.io/products/scraper-api/ecommerce/aliexpress?utm_source=github&utm_medium=referral&utm_content=aliexpress-scraper&groupid=877) is a tool designed to collect public product data
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
[<u>documentation</u>](https://developers.oxylabs.io/api-targets/e-commerce/aliexpress)
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
chat</u>](https://oxylabs.io/?utm_source=github&utm_medium=referral&utm_content=aliexpress-scraper&groupid=877) or
[<u>email</u>](mailto:support@oxylabs.io).

Also, check this tutorial on [pypi](https://pypi.org/project/ali-express-scraper/)
