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
    def __init__(self, term, ad_list, nxt_page=False):
        self.term = term
        self.ad_list = ad_list
        self.nxt_page = nxt_page
        self.page = 1
        self.length = len(ad_list)

    def __iter__(self):
        return self

    def next(self):
        if self.ad_list:
            a = self.ad_list.pop()
            if 'listingAdsense' not in a.attrs['class']:
                link = a.find('a')['href']
                return Ad.from_url(link)
            return self.next()
        else:
            if self.nxt_page:
                self.page += 1
                self.ad_list, self.nxt_page = Util.search(self.term, self.page)
                return self.next()
            raise StopIteration

    @classmethod
    def search(cls, term, page=0):
        if page > 0:
            ad_list, nxt_page = Util.search(term, page)
            nxt_page = False
        else:
            ad_list, nxt_page = Util.search(term, 1)
        return cls(term, ad_list, nxt_page)


class Util:
    @staticmethod
    def search(term, page=1):
        s_url = 'http://www.sulit.com.ph/index.php/classifieds+directory/q/'
        page = ((page - 1) * 20) + 1
        data = Util.scrape(s_url + term + '?next=' + str(page))
        soup = BeautifulSoup(data)
        ad_list = soup('div', class_='listingItem')
        nextBtn = soup.find('li', class_='skipPage').next_sibling.next_sibling
        if nextBtn:
            return (ad_list, True)
        return (ad_list, False)

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
