# https://www.codingame.com/training/medium/stock-exchange-losses


def solution():
    num_stock_values = int(input())
    max_loss = 0
    buy_price = -1

    for stock in map(int, input().split()):
        if buy_price == -1 or stock > buy_price:
            buy_price = stock
        else:
            max_loss = min(max_loss, stock - buy_price)

    print(max_loss)


solution()
