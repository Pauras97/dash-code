class Time:
    def __init__(self, day, hour, minute, am):
        self.day = day
        self.hour = hour
        self.min = minute
        self.am = am
        if not self.am:
            self.hour += 12 % 24

    def add(self, mins):
        currHour = self.hour + math.floor((self.min + mins) / 60)
        currHour = currHour % 24    
        self.hour = currHour
        if (self.min + mins) / 60 >= 1:
            if currHour == 0:
                self.day = self.day % 7 + 1
                self.hour = 0
        self.min = (self.min + mins) % 60
            
    def lessThanEquals(self, t1):
        
        if self.day == t1.day:
            return self.getNumeric24() <= t1.getNumeric24()
        return True
        

    def getNumeric24(self):
        return ((self.day*100) + self.hour) * 100 + self.min
    
    def getNumeric12(self):
        hour = self.hour
        hour %= 12
        return ((self.day*100) + hour) * 100 + self.min

class TimeIntervals:
    def __init__(self, mins):
        self.mapDays = {
        'mon': 1,
        'tue': 2,
        'wed': 3,
        'thu': 4,
        'fri': 5,
        'sat': 6,
        'sun': 7,
    }
        self.intervals = []
        self.mins = mins
        
    def getTimeIntervals(self, start, end):
        startTime = self.getTime(start)
        endTime = self.getTime(end)
        while startTime.lessThanEquals(endTime):
            startTime.add(self.mins)
            self.intervals.append(startTime.getNumeric12())
        
        return self.intervals
        
    def getTime(self, t1):
        split = t1.split(" ")
        hour, minute = split[1].split(":")
        return Time(self.mapDays.get(split[0]), int(hour), int(minute), "am" == split[2])


    
ti = TimeIntervals(30);
print(ti.getTimeIntervals("sun 11:37 am", "mon 3:00 pm"))