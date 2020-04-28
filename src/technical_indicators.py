from bs4 import BeautifulSoup
from interval import Interval
import time


class TechnicalIndicators:
    def __init__(self, symbol, exchange, interval, driver):
        self.symbol = symbol
        self.exchange = exchange
        self.interval = interval
        self.driver = driver
        self.url = self.build_url()

    def build_url(self):
        return "https://www.tradingview.com/symbols/" + self.exchange + "-" + self.symbol + "/technicals/"

    def get_data(self):
        tech_indicators_dict = {}
        self.driver.get(self.url)

        if self.interval == Interval.INTERVAL_1MIN:
            self.driver.find_element_by_xpath("//*[text()='1 minute']").click()
        elif self.interval == Interval.INTERVAL_5MIN:
            self.driver.find_element_by_xpath("//*[text()='5 minutes']").click()
        elif self.interval == Interval.INTERVAL_15MIN:
            self.driver.find_element_by_xpath("//*[text()='15 minutes']").click()
        elif self.interval == Interval.INTERVAL_1HR:
            self.driver.find_element_by_xpath("//*[text()='1 hour']").click()
        elif self.interval == Interval.INTERVAL_4HR:
            self.driver.find_element_by_xpath("//*[text()='4 hours']").click()
        elif self.interval == Interval.INTERVAL_1DAY:
            self.driver.find_element_by_xpath("//*[text()='1 day']").click()
        elif self.interval == Interval.INTERVAL_1WK:
            self.driver.find_element_by_xpath("//*[text()='1 week']").click()
        elif self.interval == Interval.INTERVAL_1MTH:
            self.driver.find_element_by_xpath("//*[text()='1 month']").click()
        else:
            self.driver.find_element_by_xpath("//*[text()='15 minutes']").click()

        time.sleep(1)

        content = self.driver.page_source
        soup = BeautifulSoup(content, features='html.parser')
        for tr in soup.findAll('tr', href=False, attrs={'class': 'row-3rEbNObt'}):
            key = ""
            vals = []
            for child in tr.contents:
                if child.text.strip():
                    if not key:
                        key = child.text.strip()
                    else:
                        vals.append(child.text.strip())

            tech_indicators_dict[key] = vals

        print("Technical Indicators request completed.")
        return tech_indicators_dict

