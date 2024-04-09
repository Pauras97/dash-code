# Given a sequence of timestamps & actions of a dasher's activity within a day, we would like to know the active time of the dasher.
#Idle time is defined as the dasher has NO delivery at hand. 
#(That means all items have been dropped off at this moment and the dasher is just waiting for another pickup)
#Active time equals total time minus idle time. Below is an example. Dropoff can only happen after pickup.
#12:00am means midnight and 12:00pm means noon. All the time is within a day.

# Timestamp(12h) | Action
# 8:30am | pickup
# 9:10am | dropoff
# 10:20am| pickup
# 12:15pm| pickup
# 12:45pm| dropoff
# 2:25pm | dropoff

# total time = 2:25pm-8:30am = 355 mins;
# idle time = 10:20am-9:10am = 70 mins;
# active time = total time-idle time = 355-70 = 285 mins;

# Have 2 lists, one for pickups={8:30am, 10:20am, 12:15pm}, one for dropoff={9:10am, 12:45pm, 2:25pm}
# Then pair them together and put into another list: {8:30am, 9:10am}, {10:20am, 12:45pm}, {12:15pm, 2:25pm}
# merge intervals, then you will know the active time and idle time.

def getIdleTime(times):
    pickups = []
    dropoffs = []
    
    for time in times:
        time, typ = time.split(" | ")
        mins = getMins(time)
        if typ == "pickup":
            pickups.append(mins)
        else:
            dropoffs.append(mins)
    
    pickups.sort()
    dropoffs.sort()
    
    intervals = [[pickups[0], dropoffs[0]]]
    for i in range(1, len(pickups)):
        start, end = pickups[i], dropoffs[i]
        
        if start > intervals[-1][1]:
            intervals.append([start, end])
        else:
            intervals[-1][1] = max(intervals[-1][1], end)
    
    idle = 0
    for i in range(1, len(intervals)):
        idle += intervals[i][0] - intervals[i-1][1]
    
    return idle
            
def getMins(time):
    hr, rest = time.split(":")
    minute, isAm = rest[:-2], rest[-2:] == "am"
    hr = int(hr)
    
    if not isAm:
        hr = hr + 12 if hr != 12 else 12
    if isAm and hr == 12:
        hr = 0
    
    minute = int(minute)
    
    return hr*60 + minute

times = ["8:30am | pickup",
"9:10am | dropoff",
"10:20am | pickup",
"12:15pm | pickup",
"12:45pm | dropoff",
"2:25pm | dropoff"]
print(getIdleTime(times))