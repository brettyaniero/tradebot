from bs4 import BeautifulSoup
import time
import urllib


class Gainers:
    def __init__(self):
        self.url = "https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/"

    def get_data(self):
        gainers_dict = {}

        source = urllib.request.urlopen(self.url).read().decode('utf-8').replace('\n', '').replace('\t', '')

        soup = BeautifulSoup(source, features='html.parser')
        for tr in soup.findAll('tr', href=False, attrs={'class': 'tv-data-table__row tv-data-table__stroke tv-screener-table__result-row'}):
            key = ""
            vals = []
            for child in tr.contents:
                if child.text.strip():
                    if not key:
                        # This is unfortunate
                        key = child.contents[0].contents[0].contents[0].text.strip()
                    else:
                        vals.append(child.text.strip())

            gainers_dict[key] = vals

        print("Gainers request completed.")
        return gainers_dict
