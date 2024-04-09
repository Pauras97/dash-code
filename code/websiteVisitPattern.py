from collections import defaultdict, Counter
from itertools import combinations

# U.n^3 where u in num of disct users and n is avg no of sites per user

def mostVisitedPattern(username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    users = defaultdict(list)
    for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0], x[1])):
        users[user].append(site)
    
    patterns = Counter()
    
    for user, sites in users.items():
        three_site_combo = combinations(sites, 3)
        three_site_combo = set(three_site_combo)
        
        three_site_combo = Counter(three_site_combo)
        patterns.update(three_site_combo)

    maxCount, res = float('-inf'), None
    
    for pattern, count in patterns.items():
        if count > maxCount:
            maxCount = count
            res = pattern
        elif count == maxCount:
            res = min(res, pattern)
    
    return res

    
    
    
    
    
username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
# Output: ["home","about","career"]

print(mostVisitedPattern(username, timestamp, website))


username = ["ua","ua","ua","ub","ub","ub"]
timestamp = [1,2,3,4,5,6]
website = ["a","b","a","a","b","c"]
# Output: ["a","b","a"]
print(mostVisitedPattern(username, timestamp, website))
