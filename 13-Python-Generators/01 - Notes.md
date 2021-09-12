# Python Generators
***
***
# Generators with Python
* Generator runctions allow you to write a function that can send back a value and then later resume to pick up where it left off
* Generators  all you to generate a sequence of values over time rather than holding it all in memory
* Generator functions will automatically suspend and resume thier execution and state around the last point of value generation 
* ex: getting the numbers 1-1 million and storing that in memory would not be super efficent

* example of creating a list - in a non efficient way
```
def create_cubes(n):
     result = []
     for x in range(n):
         result.append(x**3)
     return result
create_cubes(10)
# the list is then stored in memory
```
* you can also do:
```
for x in create_cubes(10):
    print(x)
```
* **the better way to do it with generator functions:**
```
def create_cubes(n):
     for x in range(n):
         yield x**3

for x in create_cubes(10):
    print(x)
```
* In the first example it makes a list and stores it in memory - then if you want to use the list you have to use it while its in memory.
* In this new example with the generator function it generated the values one at a time and then you can iterate over it
* In this new example ```create_cubes(10)``` no lnger works. You have to iterate over each item

* example:
```
def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for number in gen_fibon(10):
    print(number)
```
* **next function:**
```
def simple_gen():
    for x in range(3):
       yield x

for number in simple_gen():
    print(number)

g = simple_gen()
print(next(g))
print(next(g))
```
* next basically lets you step through the values - and because its a generator its not holding all the values in memory 
* after the last item you get a StopIteration error

* **iter function:**
```
s = 'Hello'
 
for letter in s:
    print(letter)

# the code above does the same thing as the code below - below is easier
s_iter = iter(s)
next(s_iter)

```
