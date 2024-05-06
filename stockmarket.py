class StockMarketTradingSystem:
    def __init__(self):
        self.portfolio = {}

    def buy_stock(self, symbol, quantity):
        # Simulated logic for buying a stock
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"Bought {quantity} shares of {symbol}")

    def sell_stock(self, symbol, quantity):
        # Simulated logic for selling a stock
        if symbol in self.portfolio and self.portfolio[symbol] >= quantity:
            self.portfolio[symbol] -= quantity
            print(f"Sold {quantity} shares of {symbol}")
            if self.portfolio[symbol] == 0:
                del self.portfolio[symbol]
        else:
            print("Not enough shares to sell.")

    def show_portfolio(self):
        print("Portfolio:")
        for symbol, quantity in self.portfolio.items():
            print(f"{symbol}: {quantity} shares")


# Example usage
if __name__ == "__main__":
    trading_system = StockMarketTradingSystem()
    trading_system.buy_stock("AAPL", 10)
    trading_system.buy_stock("MSFT", 5)
    trading_system.sell_stock("AAPL", 3)
    trading_system.sell_stock("GOOG", 2)  # Not enough shares to sell
    trading_system.show_portfolio()
