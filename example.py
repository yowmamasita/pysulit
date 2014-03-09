from pysulit.api import *

# fetches all 40+ results of 'magnet bracelet'
ads = Ads.search('magnet bracelet')
print ads
for ad in ads:
    print ad
    print ad.ad_id
    print ad.name
    print ad.price

# fetches/returns single ad instances
print Ad.from_id(37479238)
print Ad.from_url('http://www.sulit.com.ph/index.php/view+classifieds/id/37581660/Clown+Stuff+Toy')
