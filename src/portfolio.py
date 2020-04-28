class Portfolio:
    def __init__(self):
        self.stocks = []
        self.profit = 0
        self.transactions = 0

    def buy(self, stock):
        stock.buy_price = stock.current_price
        self.stocks.append(stock)
        self.transactions = self.transactions + 1

    def sell(self, stock_to_sell):
        for stock in self.stocks:
            if stock_to_sell.symbol == stock.symbol:
                profit = stock.shares * (stock_to_sell.current_price - stock.buy_price)
                self.profit = self.profit + profit
                self.stocks.remove(stock)
                self.transactions = self.transactions + 1


class Stock:
    def __init__(self):
        self.symbol = ""
        self.current_price = 0
        self.buy_price = 0
        self.shares = 0
        self.exchange = ""
