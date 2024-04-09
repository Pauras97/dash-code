# Given a streaming data of the form (timestamp, value), find the maximum value in the stream in the last X seconds.

# Assume time is monotonically increasing.
# Assume time is in the order of seconds.
# max_value() function finds the max in the last X seconds.

# StreamProcessor(5) // last 5 seconds
# set_value(0, 5)
# set_value(1, 6)
# set_value(2, 4)
# max_value(3) = 6 -> always the current time

class StreamProcessor:
    def __init__(self, x):
        self.x = x
        self.q = deque()

    def set_value(self, t, v):
        while self.q and t - self.q[0][0] > self.x:
            self.q.popleft()
        
        while self.q and v >= self.q[-1][1]:
            self.q.pop()
        
        self.q.append((t, v))
        print(self.q)

    def max_value(self, cur_t):
        while self.q and cur_t - self.q[0][0] > self.x:
            self.q.popleft()
        
        if self.q:
            return self.q[0][1]
        
        return -1
    

if __name__ == '__main__':
    sp = StreamProcessor(5)
    sp.set_value(0, 5)
    sp.set_value(1, 6)
    sp.set_value(2, 4)
    sp.set_value(5, 5)
    sp.set_value(9, 19)
    sp.set_value(15, 4)
    sp.set_value(15, 25)
    sp.set_value(19, 6)
    sp.set_value(20, 4)

    print(sp.max_value(21))