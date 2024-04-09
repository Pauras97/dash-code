def minEatingSpeed(piles: List[int], h: int):
    left = 1
    right = max(piles)
    
    while left < right:
        mid = (left + right) // 2
        hours = 0
        
        for pile in piles:
            hours += math.ceil(pile/mid)
        
        if hours <= h:
            right = mid
        else:
            left = mid + 1
    
    return right

piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h))

piles = [30,11,23,4,20]
h = 5
print(minEatingSpeed(piles, h))

piles = [30,11,23,4,20]
h = 6
print(minEatingSpeed(piles, h))

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. 
#Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
#If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.