"""
Exercises to finish:
    End of chapter 2 exercises
"""

def int_to_time(seconds):
    """
    converts an integer representing seconds into a Time object
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

# PAGE 162 EXERCISES - UNFINISHED
class Time:
    """Represents the time of day."""

    # PAGE 162 DEMO CODE
    def print_time(self):
        print("%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second))

    # PAGE 162 EXERCISE 1
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
    # PAGE 163 DEMO CODE
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    # PAGE 164 DEMO CODE
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
    
    # PAGE 165 DEMO CODE
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    # PAGE 165 DEMO CODE
    def __str__(self):
        return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)
    
    # PAGE 166-167 DEMO CODE
    """
    Written in comments to prevent redundancy
    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    """
    
    def __add__(self, other): 
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    """
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    """

# PAGE 165-167 EXERCISES - UNFINISHED
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            self.add_point(other)
        else:
            self.increment(other)

    def add_point(self, other):
        p = Point()
        p.x = self.x + other.x
        p.y = self.y + other.y
        return p
    
    def increment(self, t):
        p = Point()
        p.x = self.x + t[0]
        p.y = self.y + t[1]
        return p



# DRIVER CODE
start = Time()
start.hour = 9
start.minute = 45
start.second = 0

Time.print_time(start) # Page 162 demo code, less common function syntax to invoke method
start.print_time() # Page 162 demo code, more common method invokation syntax
start.time_to_int() # Page 162 ex 1

end = start.increment(1337) # Page 163 demo code
end.print_time()

print(end.is_after(start)) # Page 164 demo code

time = Time() # Page 165 demo code
time.print_time()
time = Time(9)
time.print_time()
time = Time(9, 45)
time.print_time()

p1 = Point(3, 4) # Page 165-167 ex 1

print(time) # Page 165 demo code

print(p1) # Page 165-167 ex 2

start = Time(9, 45) # Page 166-167 demo code
duration = Time(1, 35)
print(start + duration)
print(start + 1337)
print(1337 + start)

p2 = Point(4, 3) # Page 165-167 ex 3-4
print(p1 + p2)
print(p1 + (4, 3))

t1 = Time(7, 43) # Page 168 demo code
t2 = Time(7, 41)
t3 = Time(7, 37)
total = sum([t1, t2, t3])
print(total)
