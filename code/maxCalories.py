# You are given Calories & Prices of each food item. You are also given some budget to spend on food item.
#Maximize the amount of calories one can get from buying given food items. You cannot spend more than allowed budget amount.

## BOTTOM UP AT THE END

#ONE ITEM ONE TIME
#O(NB), where N is the number of items (length of the calories or prices list) and B is the budget.
def max_calories1(calories, prices, budget):
    cache = {}
    
    def dfs(i, remaining):
        if i >= len(calories):
            return 0
        
        if (i, remaining) in cache:
            return cache[(i, remaining)]
        
        skip = dfs(i+1, remaining)
        if remaining - prices[i] < 0:
            cache[(i, remaining)] = skip
            return skip
        
        take = calories[i] + dfs(i+1, remaining - prices[i])
        
        cache[(i, remaining)] = max(skip, take)
        return cache[(i, remaining)]
    
    return dfs(0, budget)


#ONE ITEM MULTIPLE TIMES
#O(NB), where N is the number of items (length of the calories or prices list) and B is the budget.
def max_calories2(calories, prices, budget):
    cache = {}
    
    def dfs(i, remaining):
        if i >= len(calories):
            return 0
        
        if (i, remaining) in cache:
            return cache[(i, remaining)]
        
        skip = dfs(i+1, remaining)
        take = 0
        
        if remaining - prices[i] < 0:
            cache[(i, remaining)] = skip
            return skip
        
        take = calories[i] + dfs(i, remaining - prices[i])
        
        cache[(i, remaining)] = max(skip, take)
        return cache[(i, remaining)]
    
    return dfs(0, budget)


# BOTTOM UP ONE ITEM ONCE
def max_calories3(calories, prices, budget):
    # Convert the budget to an integer if it's not, assuming prices are in whole numbers
    # budget = int(budget * 100)  
    # prices = [int(price * 100) for price in prices]
    budget = int(budget)
    
    # Initialize a DP table where dp[i] represents the max calories that can be bought with i dollars
    dp = [0] * (budget + 1)
    
    for i in range(len(calories)):
        # Update the dp table for each price up to the budget
        # Start from the end to avoid recomputing subproblems we just solved
        for j in range(budget, prices[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - prices[i]] + calories[i])
    
    return dp[budget]

# BOTTOM UP ONE ITEM MANY TIMES
def max_calories4(calories, prices, budget):
    # Convert the budget to an integer if it's not, assuming prices are in whole numbers
    # budget = int(budget * 100)  
    # prices = [int(price * 100) for price in prices]
    budget = int(budget)
    # Create the dp table
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(calories) + 1)]

    # Fill the table iteratively
    for i in range(1, len(calories) + 1):  # Item index
        for j in range(1, budget + 1):  # Budget
            if prices[i - 1] <= j:
                # Max of not taking or taking the item
                dp[i][j] = max(dp[i - 1][j], calories[i - 1] + dp[i][j - prices[i - 1]])
            else:
                # If the item cannot be taken, inherit the value from above (not taking the item)
                dp[i][j] = dp[i - 1][j]

    return dp[len(calories)][budget]



calories = [200, 50]
prices = [10, 20]
budget = 31.0

print(max_calories1(calories, prices, budget))
print(max_calories2(calories, prices, budget))
print(max_calories3(calories, prices, budget))
print(max_calories4(calories, prices, budget))
print()


calories = [500, 300, 200, 400]
prices = [15, 10, 5, 20]
budget = 40.0

print(max_calories1(calories, prices, budget))
print(max_calories2(calories, prices, budget))
print(max_calories3(calories, prices, budget))
print(max_calories4(calories, prices, budget))
print()


calories = [600, 250, 120, 300]
prices = [25, 5, 2, 10]
budget = 15.0

print(max_calories1(calories, prices, budget))
print(max_calories2(calories, prices, budget))
print(max_calories3(calories, prices, budget))
print(max_calories4(calories, prices, budget))
print()


calories = [800, 200, 150, 500, 250]
prices = [30, 8, 5, 20, 7]
budget = 50.0

print(max_calories1(calories, prices, budget))
print(max_calories2(calories, prices, budget))
print(max_calories3(calories, prices, budget))
print(max_calories4(calories, prices, budget))
print()