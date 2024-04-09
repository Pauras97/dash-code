# Given n orders, each order consists of a pickup and a delivery service.

# Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 


##MATH PERMUTATION O(N) SOLUTION
# For placing for 4 Ps, we've 4! options
# _ _ _ _ - each place no of options reduce
# Lets randomly put 4 Ps
# P2P4P1P3
# For D3, we've 1 option only i.e after P3 => P2P4P1P3_
# For D1, we've 3 options i.e => P2P4P1_P3_D3_
# For D4, we've 5 options i.e => P2P4_P1_P3_D3_D1_
# For D2, we've 7 options i.e => P2_P4_P1_P3_D3_D1_D4_

#In short we've summation of (2*n - 1) deliveries

#Total permutaions = n! * summ(2*n-1)


def countOrders(n):
    ans = 1
    MOD = (10**9) + 7
    
    for i in range(1, n+1):
        ans *= i
        
        ans = ans * (2*i - 1)
        ans %= MOD
    
    return ans

print(countOrders(2))
print(countOrders(3))
print(countOrders(4))


## DP TOP DOWN O(N^2) SPCE O(N^2)
def countOrders2(n):
    cache = defaultdict()
    MOD = (10**9) + 7
    
    def backtrack(unpicked, undelivered):
        if (unpicked, undelivered) in cache:
            return cache[(unpicked, undelivered)]
        if not unpicked and not undelivered:
            cache[(unpicked, undelivered)] = 1
            return 1
        if unpicked < 0  or undelivered < 0 or unpicked > undelivered:
            # can't pick or deliver more than n items
            # unpicked can't be more than undelivered
            cache[(unpicked, undelivered)] = 0
            return 0
        
        # Count choices of pickups
        ans = unpicked * backtrack(unpicked-1, undelivered)
        ans %= MOD
        
        # Count choices of deliveries
        ans += (undelivered - unpicked) * backtrack(unpicked, undelivered - 1)
        ans %= MOD
        
        cache[(unpicked, undelivered)] = ans
        return ans
        
        
    
    backtrack(n, n)
    return cache[(n, n)]
    
