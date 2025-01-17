# Task 2

stock = {"banana": 6,"apple": 0,"orange": 32,"pear": 15}
prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
total_prices = {item: stock[item] * prices[item] for item in stock if item in prices}

print(total_prices)