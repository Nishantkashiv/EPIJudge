from typing import List
from math import inf
from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min = inf
    max_profit = 0
    for i in prices:
        min = i if i < min else min
        profit = i - min
        max_profit = profit if profit > max_profit else max_profit
    
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
