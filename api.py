import requests
from bs4 import BeautifulSoup


class Ad:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    @classmethod
    def from_id(cls, id):
        sid = str(id)
        data = Util.scrape('http://sulit.com.ph/' + sid)
        soup = BeautifulSoup(data)

        title = soup.title.string
        name = Util.get_name(title)
        price_ = soup.find('span', itemprop='price').string.replace(',', '')
        price = float(price_)

        _ad = cls(id, name, price)
        return _ad


class Ads:
    def __init__(self, adList):
        self.adList = adList
        self.length = len(adList)

    def __repr__(self):
        return "%s (%d results)" % (self.__class__, self.length)

    def __iter__(self):
        return self

    def next(self):
        if len(self.adList):
            a = self.adList.pop()
            link = a.find('a')['href']
            idx = link.find('/id/')
            idx_ = link.find('/', idx+4)
            return Ad.from_id(int(link[idx+4:idx_]))
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
        idx = title.rfind('-')
        idx = title.rfind('-', 0, idx)
        name = title[:idx].strip()
        return name


# print str(Ad.from_id(36874892))
ss = Ads.search('yyy')
print ss
for s in ss:
    print s
