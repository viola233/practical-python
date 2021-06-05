# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    portfolio = []
    for row in rows:
        holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
        portfolio.append(holding)
    f.close()
    return portfolio


def read_prices(filename):
    f = open(filename, 'rt')
    rows = csv.reader(f)
    prices = {}
    for row in rows:
        prices[row[0]] = float(row[1])
    f.close()
    return prices


if __name__ == '__main__':
    # from pprint import pprint
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    total = 0
    for p in portfolio:
        total += p["shares"] * (prices[p["name"]] - p["price"])
    print(total)
    # pprint(portfolio)
    # print(portfolio[0])
    # print(portfolio[1])
    # print(portfolio[1]['shares'])
    # total = 0.0
    # for s in portfolio:
    #     total += s['shares'] * s['price']
    # print(total)
