## Data types
int()                                       # integer
float()                                     # decimal/float
chr()                                       # character
str()                                       # string


## Conversion
ord()                                       # ASCII value
bin()                                       # binary value
hex()                                       # hexadecimal value


## Data structures
list()                                      # returns a list (can also use [])
set()                                       # returns a set (can also use {})
dict()                                      # returns a dictionary (can also use {key: value})
tuple()                                     # returns a tuple (can also use ())


## Important functions
print("", end="")                           # output
input("")                                   # input
len()                                       # returns size of data structure
range()                                     # returns range from 0 to n-1
enumerate([])                               # returns index, element
sorted([], key=[], reverse=True)            # sorts a data structure
reversed()                                  # reverses a data structure
max([])                                     # return max value
min([])                                     # return min value
all()                                       # checks if all arguments are true
any()                                       # checks if any arguments are true
map(int, [])                                # returns the collection as the passed function
zip([], [])                                 # returns a collection of tuples per index (x1, y1)
eval("1*2*3")                               # evaluates a string as an expression


## Math-related functions
abs()                                       # returns absolute value
pow(0, 2)                                   # raise 0 to the power of 2
divmod(2, 5)                                # returns quotient, remainder
round(1.4542, 2)                            # returns a number rounded up to 2nd decimal point


## General Methods
"".index('S')                               # returns lowest index of S if S is found
"".count('S')                               # returns number of S in string


## List-specific methods
list().append()                             # append element to end of list (push())
list().insert(1, 'z')                       # insert at index 1, 'z'
list().extend([])                           # appends list to end of list
list().remove()                             # removes first occurence of a value from the list
list().pop(2)                               # remove element at index 2 (default is -1)
list().clear()                              # remove all elements from the list
list().copy()                               # returns a copy of the list


## Set-specific methods
set().add()                                 # adds an element to a set
set().remove()                              # removes an element from the set


# Dictionary-specific methods
dict().items()                              # return key, value tuples
dict().keys()                               # return keys
dict().values()                             # return values
dict().get(1, 0)                            # returns value for key 1 if present, if not returns default 0
dict().pop()                                # removes a key
dict().clear()                              # removes all key-value pairs


# String-specific methods
str().format()                              # formats a string based on {}
str().upper()                               # returns uppercase of string
str().lower()                               # returns lowercase of string
str().isupper()                             # returns True if uppercase
str().islower()                             # returns True if lowercase
str().split('')                             # splits a string based on passed function (default: " ")
str().strip()                               # strips both sides of unnecessary characters
str().isdigit()                             # check if string is digit
str().isalnum()                             # check if string is alphanumeric
str().isalpha()                             # check if string is a letter in the alphabet
str().replace('A', 'B')                     # replaces all occurences of 'A' with 'B' 
str().join([])                              # join passed elements with ""    


## List comprehension
l = [x for x in [] if x not in []]          # returns a list of x in a list, if x is not in another list
single = [0] * 10                           # initializes a list of size 10
multi = [[0] * 10 for _ in range(10)]       # initializes a multi-dimensional list of size 10 x 10


## Ternary
x = 10 if len(l) > 5 else 5                 # equivalent of (len(l) > 5) ? 10 : 5


# Index Accessing
x[0]                                        # accessing index 0
dict()['key']                               # accessing the value of 'key'
str()[3:6]                                  # gets substring from index 3 to 5 (6 not included)


## Format specifier
"{:.2f}".format(float())                    # sets string to a 2 digit float