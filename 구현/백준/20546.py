money = int(input())
prices = list(map(int, input().split()))

jh, sm = money, money
jhStock, smStock = 0, 0
up, down = 0, 0
before = prices[0]

for price in prices:
    if jh >= price:
        available = jh // price
        jh -= available * price
        jhStock += available

    if before > price:
        if up:
            up = 0
        down += 1
    elif before < price:
        if down:
            down = 0
        up += 1
    else:
        up, down = 0, 0

    if up >= 3:
        sm += smStock * price
        smStock = 0
    elif down >= 3:
        available = sm // price
        sm -= available * price
        smStock += available

    before = price

jhTotal = jh + price * jhStock
smTotal = sm + price * smStock

if jhTotal > smTotal:
    print("BNP")
elif jhTotal < smTotal:
    print("TIMING")
else:
    print("SAMESAME")
