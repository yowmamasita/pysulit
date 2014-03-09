# pysulit

Unofficial Sulit.com.ph SDK for Python

## Version

1.0

## How to use

Ads.search() fetches all results of supplied search term
Returns iterator of Ad instances
Has optional argument `page` that will only fetch results from that specific page
```
from pysulit.api import *

ads = Ads.search('video+card')
```

Ad.from_id() returns Ad instance of specified id (int)
Returns Ad instance

```
ad = Ad.from_id(1234567)
```

Ad.from_url() returns Ad instance of specified url
Returns Ad instance

```
ad = Ad.from_url('http://www.sulit.com.ph/index.php/view+classifieds/id/.../...')
```

An Ad instance has the ff properties: `ad_id` (int), `name` (str), and `price` (float)

As an example, please look at [example.py](https://github.com/yowmamasita/pysulit/blob/master/example.py)

## License

[MIT License](http://bensarmiento.mit-license.org/)

```
Copyright © 2014 Ben Sarmiento, http://bensarmiento.com <me@bensarmiento.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in
the Software without restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
