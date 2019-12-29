# find minimum number of coines required to make a given change Total
import numpy as np 
coins = [1,2,3,4,5]
total = 12
min_of_coins= float("inf")

# Naive Recursion  
def __minimum_coins(coin_value,min_of_coins):
    if coin_value == 0:
        return 0
    else:
        for coin in coins:
            if coin_value >= coin:
                min_of_coins= min(min_of_coins, __minimum_coins(coin_value-coin,min_of_coins)+1)
        return min_of_coins

# Dynamic Programming Method
def min_of_coins_dp(coins,total):
    columns = total+1
    rows = len(coins)
    my_array = np.array([[j if i==0 else 0 for j in range(columns)] for i in range(rows)])
    for i in range(1,rows):
        for j in range(columns):
            if coins[i] > j:
                my_array[i][j] = my_array[i-1][j]
            elif coins[i] <=j:
                my_array[i][j] = min(my_array[i-1][j],my_array[i][j-coins[i]]+1)
    print(my_array)            
    return my_array[rows-1][columns-1]

def minimum_coins(total):
    print("Minimum Number of Coins",min_of_coins_dp(coins,total))
    print("Minimum Number of Coins",__minimum_coins(total,min_of_coins))

minimum_coins(total)
