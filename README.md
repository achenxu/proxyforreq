# proxyforreq
Formats proxies for use in python requests

Usage:
-------------------------------------
Place proxyforreq.py in your package directory

All proxy types are supported


Example Usage:
-------------------------------------
```
from proxyforreq import proxyforreq

proxy = "111.11.1.12:56:user:pass"
proxies = proxyforreq(proxy=proxy)
requests.get(url, proxies=proxies)
```
