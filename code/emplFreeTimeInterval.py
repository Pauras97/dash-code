# We are given a list schedule of employees, which represents the working time for each employee.

# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

# (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays.
#For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).
#Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

def employeeFreeTime(schedule: '[[Interval]]') -> '[Interval]':
    heap = []
    res = []
    
    for i in range(len(schedule)):
        item = (schedule[i][0].start, schedule[i][0].end, i)
        heappush(heap, item)
        schedule[i].pop(0)
    
    end = heap[0][1]
    while heap:
        new_start, new_end, i = heappop(heap)
        if new_start <= end:
            end = max(new_end, end)
        else:
            print(end, new_start)
            res.append(Interval(end, new_start))
            end = new_end
        
        if schedule[i]:
            item = (schedule[i][0].start, schedule[i][0].end, i)
            heappush(heap, item)
            schedule[i].pop(0)
    
    return res
    
    

s1 = [[Interval(1, 2), Interval(5, 6)], [Interval(1,3)], [Interval(4, 10)]]

s2 = [[Interval(1,3), Interval(6,7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]]

print([(val.start, val.end) for val in employeeFreeTime(s1)])
print([(val.start, val.end) for val in employeeFreeTime(s2)])