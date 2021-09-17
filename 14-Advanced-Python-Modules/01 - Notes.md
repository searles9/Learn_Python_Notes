# Advanced Python Modules
***
***
# Into 
* This section covers some of the useful built in Python modules
## Modules:
* Collections 
* Os module and Datetime
* Math and Random
* Python Debugger
* Timeit
* Regular Expressions
* Unzipping and Zipping Modules
***
***
# Python Collections Module
* built in to python 
* implements specialized container data types - an alternitive to Pythons built in general purpose container types
### Counter()
```
from collections import Counter
mylist = [1,1,1,1,1,1,1,2,2,2,2,2,2,43,4,4,4,4]
Counter(mylist) # this shows how many of each item you have -ex 6 2's
```
* Counter stores the output as a dictionary item
```
Counter ('How many times does each word show up in this sentance with a word')
Counter(sentence.lower().split())

Counter("tsdfsdfsdfsdfsdfsdf")
```
```
letters = 'aaaaabbbbbccccc'
c = Counter(letters)

c.most_common(2)  # shows the 2 most common keys
```
### Common patterns when using the Counter() object
* sum(c.values())     --------            # total of all counts
* (c.clear()      ----------                 # reset all counts
* list(c)       --------                  # list unique elements
* set(c)       ------                   # convert to a set
* dict(c)     ------                    # convert to a regular dictionary
* c.items()    -----                   # convert to a list of (elem, cnt) pairs
* Counter(dict(list_of_pairs)) -------   # convert from a list of (elem, cnt) pairs
* c.most_common()[:-n-1:-1]  -----     # n least common elements
* c += Counter()    -------              # remove zero and negative counts
### Defaultdict
```
from collection import defaultdict
d = {'a':10}
d['WRONG KEY'] # returns key error with a normal dictionary

# ---------------------------------

d = defaultdict(lambda:0) # < --- this is the default value
d['correct' = 100]
d['wrong key'] # uses the default value of 0 since this key doesnt exist

# with a default dictionary it will assign a default value if there is an instance where a key error would have occured
```
### Named Tuples
* A named tuple allows you to label your tuple values
```
mytuple = (10,20,30)
mytuple[0]

from collections import namedtuple
Dog = Namedtuple('Dog',['age','breed','name'S])
sammy = Dog(age=5,breed='Husky',name='Sam')
type(sammy) # type Dog
sammy.age # gets the age
sammy.breed
sammy.name
```

***
***
# Opening and Reading Files and Folders (Python OS Module)
* Shutil and OS Modules
* useful for opening every file in a dir so you can reaad and write to it
* useful for action moving files around on your actual PC
#### Writing to a file
```
f = open('practice.txt','w+')
f.write('test')
f.close()
```
#### Getting the current directory
* os module: https://docs.python.org/3/library/os.html
* the commands work across all OS's that support Python
```
import OS
os.getcwd() # gets the CWD (with \\ since you need an escapre character)
```
#### Listing a dir
```
os.listdir() # from the CWD
os.listdir("C:\\Users")
```
#### Moving files
* there are permission restrictions for this
* Move files: https://stackoverflow.com/questions/23253439/shutil-movescr-dst-gets-me-ioerror-errno-13-permission-denied-and-3-more-e
* shutil.move(source,destination)
```
import shutil
shutil.move('practice.txt','C:\\Users\\Marcial')
os.listdir()
shutil.move('C:\\Users\\Marcial\practice.txt',os.getcwd()) # move to cwd
```
#### Deleting files
* ```os.unlink(path)``` deletes a file at the path
* ```os.rmdir(path)```  deletes an **empty** folder at the path you provide
* ```shutil.rmtree(path)```  this removes **all files and folders in the path``` ...spooky and risky
* send2trash is safer as it send items to the trash bin and does not permanatly delete them
* ```pip install send2trash```
```
import send2trash
send2trash.send2trash('practice.txt')
```
#### Walking through a directory
```
os.getcwd()
os.listdir()

for folder , sub_folders , files in os.walk("Example_Top_Level"):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')
    
    # Now look at subfolders

```
***
***
# Python Datetime Module
* Datetime allows you to deal with time stamps in your code. The time values are represented with the time class.
* instance ttributes: hour, minute, second, and microsecond - can include time zone info
### Time
```
import datetime
t = datetime.time(4, 20, 1)


print(t)   # returns 04:20:01
print('hour  :', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo) # time zone
```
* check the min and max values:
```
print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)
```
### Dates
* this module is often used when working with databases
* date timestamps
* date values are represented with the date class
* instance attributes: year, month, and day
* to get todays date: ```today()```
```
today = datetime.date.today()

print(today)
# returns: 2020-06-10

print('ctime:', today.ctime())
# returns: Wed Jun 10 00:00:00 2020

print('tuple:', today.timetuple())
# returns: time.struct_time(tm_year=2020, tm_mon=6, tm_mday=10, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=162, tm_isdst=-1)

print('ordinal:', today.toordinal())
# returns:  737586

print('Year :', today.year)
# returns:  2020

print('Month:', today.month)
# returns:  6

print('Day  :', today.day)
# returns:  10
```
* to get the date range you can use the min, max and resolution
```
print('Earliest  :', datetime.date.min)
# returns: Earliest  : 0001-01-01

print('Latest    :', datetime.date.max)
# returns:  Latest    : 9999-12-31

print('Resolution:', datetime.date.resolution)
# returns:  Resolution: 1 day, 0:00:00
```
* example of using replace() to change the year in a date:
```
d1 = datetime.date(2015, 3, 11)
print('d1:', d1)
# returns: 2015-03-11

d2 = d1.replace(year=1990)
print('d2:', d2)
# returns:  1990-03-11
```
* you get get the difference between dates like this:
```
d1
d2
d1-d2
# returns: datetime.timedelta(9131)
# this returns the difference in days between the 2 dates
```
***
***
# Python Math and Random Module
## Math
```
import math
help(math)
```

### Rounding numbers
```
value = 4.35
math.floor(value) # 4
math.ceiling(value) # 5
round(value) # noth math module - its built into python
```
### Mathamatical constants
```
math.pi
from math ipmort pi
pi # 3.14
math.e # big math
math.tau # big math
math.inf # big math
math.nan # big math
```
### Logarithmic values
```
math.e 
math.log(math.e)
math.log(10)
```
### Custom base
```
math.log(100,10)
10**2
```
### Trigonometrics Functions
```
math.sin(10)
math.degrees(pi/2)
math.radians(180)
```

## Randon Module

```
import random
random.randint(0,100) # start , stop
random.randint(0,100)

# you can set a seed which basically makes it return the same set of numbers
# the value is arbitrary and can be whatever you want
random.seed(101)
random.rantint(0,100)
```
### Random inegers
```
random.randint(0,100)
```
### Random with sequences
* grab a random item from a list
```
mylist = [1,2,3,4,5,65,6]
random.choice(mylist)
```
### Sample with Replacement
* gets a sample and allows replacement
```
random.choices(population=mylist,k=10) # picks 10 numbers
```
### Sample without replacement
```
random.sample(population=mylist,k=10)
```
### Shuffle a list
* this effects the object in place - dont assign it to anything
```
random.shuffle(mylist)
```
### Random disturbutions
#### uniform disturbution
* Continuous - randomly picks a value between a and b - floating point numbers are allowed
```
random.uniform(a=0,b=100)
```
#### normal/gaussian disturbution
```
random.gauss(mu=0,sigma=1)
```

# Python Debugger
* python has a built in debugger tool (pdb)
* example of an error:
```
x =  [1,2,3]
y =2 
z = 3

result = y+z 
result2 = x+y # you cant add a list and an integer 
```
* the  set_trace() module allows you to essentially pause the code at the point of the trace and check if anything is wrong
```
import pdb

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

# Set a trace using Python Debugger
pdb.set_trace()

result2 = y+x
print(result2)
```
* set trace will stop and ask for input. you then then call variables and test things out to see how things work together
* q  to quit the trace debugger

# Regular Exression 
* in python you can search for substrings within a larger string with the in operator
```
"dog" in "my dog is great"
```
* there are some limitations to that however
* regular expressions allow you to search patters - like an email for example , or a phone number structure
## Searching for basic patterns
* syntax: re.search(pattern,text)

#### example expression
* phone number: ``` (555)-555-5555```
* regex pattern: ``` r"(\d\d\d)-\d\d\d-\d\d\d\d" ```
* same thing - different way: ``` r"(\d{3}-\d{3}-\d{4})" ```
* search() will scan the text and then return a match object, or none if no patter is found
```
text = "The person's phone number is 408-555-1234. Call soon!"
'phone' in text
import re
pattern = 'phone'
re.search(pattern,text)

# this returns the span location of the text, and the match
```
* interacting with the match (only 1 match -the first):
```
re.search(pattern,text)
match.span() # gets the span location (12,17)
match.start() # returns the first value of the span
match.end() # returns the last value of the span
```
* interacting with multible matches
```
matches = re.findall(pattern,text)
# you get the matches in a list
len(matches) # number of matches

# this iterates over each match
for match in re.finditer(pattern,text): 
        print(match.span())
        print(match.group()) # the matched text
```

## Patterns

#### Character identifiers 
* Character 	Description 	Example Pattern Code 	Exammple Match
* \d 	A digit 	file_\d\d 	file_25
* \w 	Alphanumeric 	\w-\w\w\w 	A-b_1 (letter or number)
* \s 	White space 	a\sb\sc 	a b c
* \D 	A non digit 	\D\D\D 	ABC
* \W 	Non-alphanumeric 	\W\W\W\W\W 	*-+=)
* \S 	Non-whitespace 	\S\S\S\S 	Yoyo

* example: 
```
text = "My telephone number is 408-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
phone.group() # returns the number
```
* you can call for a portion of 
```
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
results.group() # the entire group
results.group(1) # returns the first 3 digits
```
* group indexes start at 1
* re.compile() compiles a set of expressions - the parantheses are what show what each group is
#### Quantifiers
* Character 	Description 	Example Pattern Code 	Exammple Match
* "+ 	Occurs one or more times 	Version \w-\w+ 	Version A-b1_1"
* {3} 	Occurs exactly 3 times 	\D{3} 	abc
* {2,4} 	Occurs 2 to 4 times 	\d {2,4} 	123
* {3,} 	Occurs 3 or more 	\w{3,} 	anycharacters
* \* 	Occurs zero or more times 	A\*B\*C* 	AAACC
* ? 	Once or none 	plurals? 	plural

#### additional regex syntax
* use the pipe orerator as an or statement
```
re.search(r"man|woman","This man was here.")
```
* the wildcard character can be used to match any character
```
re.findall(r".at","The cat in the hat sat here.")
# returns ['cat', 'hat', 'sat']
re.findall(r".at","The bat went splat")
# returns ['bat', 'lat']
# notice how it only catches the last part of it
re.findall(r"...at","The bat went splat")
# this catches more ... see the dots ['e bat', 'splat']
```
#### starts and ends with 
* you can use the ^ to signal starts with, and the $ to signal ends with
```
# Ends with a number
re.findall(r'\d$','This ends with a number 2')
# Starts with a number
re.findall(r'^\d','1 is the loneliest number.')
```
* To exclude characters, we can use the ^ symbol in conjunction with a set of brackets []. Anything inside the brackets is excluded
```
phrase = "there are 3 numbers 34 inside 5 this sentence."
re.findall(r'[^\d]',phrase) # splits letters into a list
re.findall(r'[^\d]+',phrase) # puts the stuff back together
```
* to remove puncuation:
```
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
re.findall('[^!.? ]+',test_phrase)
# join them back together:
clean = ' '.join(re.findall('[^!.? ]+',test_phrase))
print(clean)
```
#### Brackets for grouping
* you can use brackets to group together options
```
text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
re.findall(r'[\w]+-[\w]+',text)
# returns 
['hypen-words', 'long-ish']
```
#### Parenthesis for multible options
```
# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

re.search(r'cat(fish|nap|claw)',text)
re.search(r'cat(fish|nap|claw)',texttwo)
re.search(r'cat(fish|nap|claw)',textthree) # no match
```

***
***
# Timing your code
* This can help you tell how long it takes your code to run
* code needs to take at least 0.1 seconds to complete
```
import time
# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_one(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time

# returns  0.18550348281860352
```

### Timeit Module
* this can help tell the time difference between two functions
```
import timeit
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
stmt = 'func_one(100)'
timeit.timeit(stmt,setup,number=100000)
# returns 1.3161248000000114

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
stmt2 = 'func_two(100)'
timeit.timeit(stmt2,setup2,number=100000)

# returns 10.894090699999992

# 1 is faster

```

### Jupyter magic method
*  This method is ONLY available in Jupyter and the magic command needs to be at the top of the cell with nothing above it (not even commented code)
```
%%timeit
func_one(100)

# returns 100000 loops, best of 3: 13.4 µs per loop
```

***
***

# Unziping and zipping files
* create files to compress:
