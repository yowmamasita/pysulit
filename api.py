import requests
from bs4 import BeautifulSoup


class Ad:
    def __init__(self, ad_id, name, price):
        self.ad_id = ad_id
        self.name = name
        self.price = price

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    @classmethod
    def from_id(cls, ad_id):
        sad_id = str(ad_id)
        data = Util.scrape('http://sulit.com.ph/' + sad_id)
        soup = BeautifulSoup(data)

        title = soup.title.string
        name = Util.get_name(title)
        price_ = soup.find('span', itemprop='price').string.replace(',', '')
        price = float(price_)

        _ad = cls(ad_id, name, price)
        return _ad

    @classmethod
    def from_url(cls, url):
        data = Util.scrape(url)
        soup = BeautifulSoup(data)

        ad_id = soup.find('input', {'name': 'adShortURL'})['value']
        ad_id = int(ad_id.replace('http://sulit.com.ph/', ''))
        title = soup.title.string
        name = Util.get_name(title)
        price = soup.find('span', itemprop='price').string.replace(',', '')
        price = float(price)

        return cls(ad_id, name, price)


class Ads:
    def __init__(self, adList):
        self.adList = adList
        self.length = len(adList)

    def __repr__(self):
        return "%s({'results': %d})" % (self.__class__, self.length)

    def __iter__(self):
        return self

    def next(self):
        if len(self.adList):
            a = self.adList.pop()
            if 'listingAdsense' not in a.attrs['class']:
                link = a.find('a')['href']
                return Ad.from_url(link)
            return self.next()
        else:
            raise StopIteration

    @classmethod
    def search(cls, term):
        s_url = 'http://www.sulit.com.ph/index.php/classifieds+directory/q/'
        data = Util.scrape(s_url + term)
        soup = BeautifulSoup(data)
        adList = soup('div', class_='listingItem')
        return cls(adList)


class Util:
    @staticmethod
    def scrape(url):
        s = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) '
            'Gecko/20100101 Firefox/27.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;'
            'q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
        }
        r = s.get(url, headers=headers)
        return r.text

    @staticmethod
    def get_name(title):
        ad_idx = title.rfind('-')
        ad_idx = title.rfind('-', 0, ad_idx)
        name = title[:ad_idx].strip()
        return name


# print str(Ad.from_ad_id(36874892))
# print str(Ad.from_url("http://sulit.com.ph/37683793"))
ss = Ads.search('cebu')
print ss
for s in ss:
    print str(s)
