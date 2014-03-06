import requests
from bs4 import BeautifulSoup


class Sulit:
    @staticmethod
    def search(self, term):
        s_url = 'http://www.sulit.com.ph/index.php/classifieds+directory/q/'
        data = Util.scrape(s_url + term)
        soup = BeautifulSoup(data)
        return soup


class Ad:
    def __init__(self, id, title, price):
        self.id = id
        self.name = self._get_name(title)
        self.price = price

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    @classmethod
    def from_id(cls, id):
        sid = str(id)
        data = Util.scrape('http://sulit.com.ph/' + sid)
        soup = BeautifulSoup(data)

        title = soup.title.string
        price_ = soup.find('span', itemprop='price').string.replace(',', '')
        price = float(price_)

        _ad = cls(id, title, price)
        return _ad

    def _get_name(self, title):
        idx = title.rfind('-')
        idx = title.rfind('-', 0, idx)
        name = title[:idx].strip()
        return name


class Ads:
    pass


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


print str(Ad.from_id(36874892))
