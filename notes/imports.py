## Math Module
import math

math.ceil()                                 # returns ceiling of float
math.floor()                                # returns floor of float
math.log(5, 2)                              # returns log2(5)
math.fabs()                                 # returns absolute value of float
math.factorial()                            # returns factorial of a number
math.gcd(*[1, 2, 3])                        # returns gcd of a group of numbers      
math.lcm(*[1, 2, 3])                        # returns lcm of a group of numbers


## Collections Module
import collections

collections.Counter()                       # returns dictionary of value count per key
collections.deque()                         # returns a deque data structure
collections.defaultdict()                   # returns a dictionary that returns a default value when accessing unfound element


## Datetime Module
import datetime
x = datetime.datetime.now()                 # get current time
datetime.datetime.strptime("10", "%d")      # returns a datetime object passed from a formatted string
x.strftime("%d")                            # returns a string based on passed format
datetime.timedelta(days= 10, weeks=1)       # returns a timedelta object that can be used with a datetime object
x - datetime.timedelta(days = 1)            # subtracts a day from x


## Important formats for Datetime
## Uppercase = full version, Lowercase = short version 

datetime.datetime.strptime("11", "%d")      # %d = day of the month
datetime.datetime.strptime("11", "%m")      # %m = month
datetime.datetime.strptime("11", "%y")      # %y = short year (two digits)
datetime.datetime.strptime("2011", "%Y")    # %Y = full year (4 digits)
datetime.datetime.strptime("Dec", "%b")     # %b = short month name 
datetime.datetime.strptime("May", "%B")     # %B = full month name
datetime.datetime.strptime("Wed", "%a")     # %a = short weekday
datetime.datetime.strptime("Friday", "%A")  # %A = full weekday
datetime.datetime.strptime("1", "%w")       # %w = weekday as a number (0-indexed starting from Sunday)