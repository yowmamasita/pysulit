from pysulit.api import *

# fetches all 40+ results of 'magnet bracelet'
ads = Ads.search('magnet bracelet')
for ad in ads:
    print ad
