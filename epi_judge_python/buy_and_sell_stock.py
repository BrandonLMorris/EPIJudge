from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    min_so_far = 2 << 32
    best_profit = 0
    for price in prices:
        min_so_far = min(price, min_so_far)
        best_profit = max(price - min_so_far, best_profit)
    return best_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
