# Python Statements
***
# If, Elif and Else Statements
* control flow syntax makes use of colons and indentation (whitespace)
* elif has a confition and you can use as many as you want
* else doesnt use a condition
## Example:
```
if some_condition:
    #execute some code
elif some_other_condition:
    # do domething else
else:
    # do other code
```
## Real Example's:
```
hungry = True

if hungry:
   print("Feed me!")
else:
   print("Not hungry!")
```

# For Loops
* many items are iterable like strings or lists or dictionary

## Syntax of a For Loop
```
my_iterable = [1,2,3]

for item_name in my_iterable:
  print(item_name)
```
this would return: 1 then 2 then 3
## More For Loop Examples
### Lists
* the list var for the examples:
```
mylist = [1,2,3,4,5,6,7,8,9,10]
```
```
for num in mylist:
    # Check for even - remember % is the remainder
    if num % 2 == 0:
       print(num)
    else:
        print(f'Odd Number: {num}')
```
* Get a sum of all the numbers in a list
``` 
list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print(list_sum)
```
### String
```
for letter in "Hello World":
    print(letter)
```
### Tuple
```
tup = (1,2,3)
```
```
for item in tup:
    print(item)
```
* items can be used with Tuple unpacking
* list of tuples:
```
mylist = [(1,2),(3,4),(5,6)]
```
```
# you technically dont need the parentheses in the line below - you just need to duplicate the tuple structure

for (a,b) in mylist:
    print(a)
    print(b)
```
### Dictionary 
* remember dictionaries are not sorted
* the dictionary:
```
d = {"k1":1,"k2":2,"k3":3}
```
```
for item in d:
    print(item)

# dictionaries only iterate through the itmes by default - to iterate the items and key you use d.items()
# if you want to explicitly get the values do d.values()
```
```
for key,value in d.items():
    print(value)
    print(key)
```

# While Loops
* While loops continue to exexute code while a condition remains ```True```
* Syntax:
```
while some_boolean_condition:
    #do something
else: 
    # do something different 

# else is when the condition becomes false
```
* Real Example:
```
x = 0

while x < 5 :
    print(f'current value of X is {x}')
    x = x + 1
else:
    print('x is not less than 5')
```
* ```x = x + 1 ``` can also be written as ```x += 1```

### Break
* Breaks out of the current closest loop and stops everything
```
for letter in mystring:
     if letter == "a":
       break
     else: 
       print(letter)
```
### Continue
* Goes to the top of the closest loop
```
mystring = "Sammy"

for letter in mystring:
     if letter == "a":
       contine
     else: 
       print(letter)
```
### Pass
* Does nothing
```
for item in X:
    pass

# if you did a comment instead of a pass you would get a syntax error
```

# Useful Operators in Python
