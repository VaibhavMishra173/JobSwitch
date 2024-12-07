# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


# prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
prices = [1,2]
# cr_stk=0
# profit=0

# for i in range(len(prices)-1,cr_stk+1,-1):
#     profit=max(profit,(prices[i]-prices[cr_stk]))
#     print(prices[cr_stk],prices[i],profit,i)
#     cr_stk+=1

# print(profit,end=" ")


# Accepted
min_price=float('inf')
max_profit=0
for price in prices:
    min_price=min(min_price,price)
    max_profit=max(max_profit,price-min_price)
print(max_profit)



