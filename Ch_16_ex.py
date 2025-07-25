"""
Exercises to finish:
    End of chapter 2 exercises
"""
# code given in text
class Time:
    """
    Represents the time of day. 

    attributes: hour, minute, second
    """

# PAGE 155 EXERCISES - FINISHED
def print_time(t):
    """
    prints time object in form hours:minutes:seconds

    params
        t (Time object)
    returns
        None
    raises
        None
    """
    # correction based on hint
    print("%.2d:%.2d:%.2d" % (t.hour, t.minute, t.second)) 

    """original
    print(t.hour, t.minute, t.second, sep=':')"""

def is_after(t1, t2):
    """
    Checks if t1 follows t2. Challenge: don't use an if statement. 

    params
        t1 (Time object): First time
        t2 (Time object): Second time
    returns
        result (bool): True if t1 follows t2; False if otherwise
    raises
        None
    """
    result1 = t1.hour > t2.hour
    result2 = (t1.hour == t2.hour) and (t1.minute > t2.minute)
    result3 = (t1.hour == t2.hour) and (t1.minute == t2.minute) and (t1.second > t2.second)
    result = result1 or result2 or result3
    return result

# PAGE 156 DEMO CODE

# code given in text
def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum


# PAGE 157 EXERCISES - UNFINISHED
def increment(time, seconds):
    time.second += seconds

    if time.second >= 60: 
        temp = time.second
        time.second = time.second % 60
        time.minute += (temp - time.second)/60
    
    if time.minute >= 60:
        temp = time.minute
        time.minute = time.minute % 60
        time.hour += (temp - time.minute)/60
    
    return time
    """
    code given in text:
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
    
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    """

def pure_increment(t, s):
    """
    Returns incremented time by seconds

    params
        t (Time object): Original time object
        s (int): Number of seconds to increment by
    returns
        newt (Time object): New time object
    raises
        None
    """
    newt = Time()
    newt.hour = t.hour
    newt.minute = t.minute
    newt.second = t.second + s

    if newt.second >= 60:
        temp = newt.second
        newt.second = newt.second % 60
        newt.minute += (temp - newt.second)/60
    
    if newt.minute >- 60:
        temp = newt.minute
        newt.minute = newt.minute % 60
        newt.hour += (temp - newt.minute)/60

    return newt


# PAGE 158 DEMO CODE
def time_to_int(time):
    """
    Converts a time object to an integer representing seconds
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    """
    Converts an integer representing seconds to a time object
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60) # divmod returns a tuple of the quotient and remainder of first arg / second arg
    time.hour, time.minute = divmod(minutes, 60)
    return time

def rewritten_add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

# PAGE 158 EXERCISE - FINISHED

def planned_increment(t, s):
    """
    Returns time incremented by seconds

    params
        t (Time object): original time object
        s (seconds): seconds to increment by
    """
    conv_t = time_to_int(t)
    sum = conv_t + s
    return int_to_time(sum)


# PAGE 159 DEMO CODE
def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

"""
Written in comments to prevent redundancy

With valid_time function

def add_time(t1, t2):
    if not valid_time(t1) or valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

With assert clause

def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
"""

# DRIVER

time = Time() # create time (Time object) for page 155 ex 1
time.hour = 9
time.minute = 9
time.second = 9

t1 = Time() # create t1 (Time object) for page 155 ex 2
t1.hour = 7
t1.minute = 4
t1.second = 9

t2 = Time() # create t2 (Time object) for page 155 ex 2
t2.hour = 7
t2.minute = 4
t2.second = 9

start = Time() # code given in text
start.hour = 9
start.minute = 45
start.second = 0

duration = Time() # code given in text
duration.hour = 1
duration.minute = 35
duration.second = 0

print_time(time) # Page 155 ex 1

print(is_after(t1, t2)) # Page 155 ex 2

done = add_time(start, duration) # Page 156 demo 
print_time(done) 

print_time(increment(time, 500)) # Page 157 ex 1

print_time(pure_increment(time, 500)) # Page 157 (technically 158) ex 2

done = rewritten_add_time(start, duration) # Page 158 demo
print_time(done)

print_time(planned_increment(time, 500)) # Page 158 ex 1