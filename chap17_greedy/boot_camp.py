def change_maker(number):
    CENTS = [100,50,25,10,5,1]
    coins = []
    for coin in CENTS:
        number_of_coins = number//coin
        for _ in range(number_of_coins):
            number -= coin
            coins.append(coin)
        
    return coins

print(change_maker(129))