def maxPay(d_starts, d_ends, d_pays):
    jobs = []
    
    for start, end, pay in zip(d_starts, d_ends, d_pays):
        jobs.append((start, end, pay))
    
    jobs.sort()
    heap = []
    maxProf = 0
    
    for i in range(len(jobs)):
        start, end, pay = jobs[i]
        
        while heap and start >= heap[0][0]:
            maxProf = max(maxProf, heap[0][1])
            heappop(heap)
        
        curr = pay + maxProf
        heappush(heap, (end, curr))
    
    while heap:
        maxProf = max(maxProf, heap[0][1])
        heappop(heap)
    return maxProf

d_starts = [2, 3, 5, 7]
d_ends = [6, 5, 10, 11]
d_pays = [5, 2, 4, 1]

print(maxPay(d_starts, d_ends, d_pays))


def maxPayWithOverlaps(d_starts, d_ends, d_pays, n):
    jobs = sorted(zip(d_starts, d_ends, d_pays), key=lambda x: x[0])  # Sort by start time
    memo = {}  # For memoization

    def dp(index, ongoing):
        # Base case: No more jobs to consider
        if index == len(jobs):
            return 0

        # Memoization check
        if (index, ongoing) in memo:
            return memo[(index, ongoing)]

        # Skip current job
        max_profit = dp(index + 1, ongoing)

        # Try to take current job if it doesn't exceed allowed overlaps
        start, end, pay = jobs[index]
        if ongoing < n:  # Check if we can take this job
            next_index = index + 1
            # Increment ongoing jobs for overlapping
            while next_index < len(jobs) and jobs[next_index][0] < end:
                next_index += 1
            max_profit = max(max_profit, pay + dp(next_index, ongoing + 1))

        memo[(index, ongoing)] = max_profit
        return max_profit

    return dp(0, 0)

# Example usage
d_starts = [1, 2, 3, 3]
d_ends = [3, 5, 10, 6]
d_pays = [20, 20, 100, 70]
n = 2  # Up to 2 overlapping jobs are allowed

print(maxPayWithOverlaps(d_starts, d_ends, d_pays, n))

d_starts = [2, 3, 5, 7]
d_ends = [6, 5, 10, 11]
d_pays = [5, 2, 4, 1]
n = 2  # Up to 2 overlapping jobs are allowed

print(maxPayWithOverlaps(d_starts, d_ends, d_pays, n))
