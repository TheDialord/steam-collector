import steammarket
import threading
import requests
import time
import re
from BeautifulSoup import BeautifulSoup

items = steammarket.load_items()


class CheckingPriceThread(threading.Thread):
    def __init__(self, item):
        threading.Thread.__init__(self)
        self.item = item

    def run(self):
        while True:
            url = 'http://steamcommunity.com/market/listings/%s/%s' % (self.item['appid'], self.item['path'])
            request = requests.get(url)

            if request.ok:
                parsed_html = BeautifulSoup(request.content)

                listings = parsed_html.body.findAll('div', attrs={'class': lambda x: x and re.search(
                    '(\s|^)market_listing_row(\s|$)', x)
                })
                for listing in listings:
                    totalHtml = listing.find('span', attrs={'class': 'market_listing_price market_listing_price_with_fee'})
                    withoutHtml = listing.find('span', attrs={'class': 'market_listing_price market_listing_price_without_fee'})
                    listingId = listing['id'].split('_')[1]

                    total = int(float(totalHtml.getText().split(' ')[0].replace(',', '.')) * 100)
                    subtotal = int(float(withoutHtml.getText().split(' ')[0].replace(',', '.')) * 100)
                    fee = total - subtotal

                    print 'Fetched # %s : %s' % (str(listingId), str(total))

                    if total <= item['preferredPrice']:
                        steammarket.add_listing(int(listingId), fee, subtotal)

                time.sleep(self.item['interval'])

            time.sleep(1)
        return


for item in items:
    thread = CheckingPriceThread(item)
    thread.start()








