#NLogN + QLogQ
def maxProfitAssignment(diff, prof, worker):
    
    jobs = list(zip(diff, prof))
    jobs.sort()
    
    ans = 0
    best, i = 0, 0
    
    for skill in sorted(worker):
        while i < len(jobs) and skill >= jobs[i][0]:
            best = max(best, jobs[i][1])
            i += 1
        ans += best
    
    return ans
        
        
difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]

print(maxProfitAssignment(difficulty, profit, worker))
