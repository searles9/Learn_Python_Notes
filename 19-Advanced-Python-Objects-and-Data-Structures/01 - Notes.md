# Advanced Python Objects and Data Structures
***
***
# Advanced Numbers
### Hexadecimal
* you can convert numbers into hexidecimal (ipv6)
```
hex(246)
# returns '0xf6'
```

### Binary
* you can convert numbers into binary (ipv4)
```
bin(1234)
# returns '0b10011010010'
```
### Exponentials 
* the pow() function takes two arguments - equivalent to x^y
*  With three arguments it is equivalent to (x^y)%z, but may be more efficient for long integers.
```
pow(3,4)
pow(3,4,5)
```

### absolute value
* adbosulte value is the distance from 0
* this makes negative numbers positive
```
abs(2) # returns 2
abs(-9) # returns 9
```
### Round
* the round() function will round a number given precision in decimal digits (default 0) - it cant convert iniegers to floats
```
round(3,2) # returns 3

round(395,-2) # returns 400 

round(3.1415926535,2) # returns 3.14
```

***
# Advanced strings
* there are multible string related methods that you can use to save time
```
# example string: 
s = 'hello world'
```
### Changing case
* these only return modified copies, it doesnt actually change the string in place
```
s.upper()
s.lower()
s.capitalize() # might return "Hello world"

# to actually change the string:
s = s.upper()


```
### Location and Counting
```
s.count('o') # returns the number of occurrences, without overlap
# returns 2

s.find('o') # returns the starting index position of the first occurence
# returns 4
```
### Formatting
#### center()
* lets you place a string between another string with a certian length
```
s.center(20,'z')
# returns 'zzzzhello worldzzzzz'
```
#### expandtabs()
* The expandtabs() method will expand tab notations \t into spaces:
```
'hello\thi'.expandtabs()
# returns 'hello   hi'
```
### is check methods
#### isalpha()
* isalnum() will return True if all characters in s are alphanumeric
```
s.isalnum()
```
#### islower()
* islower() will return True if all cased characters in s are lowercase and there is at least one cased character in s, False otherwise.
```
s.islower()
```
#### isspace()
* isspace() will return True if all characters in s are whitespace.
```
s.isspace()
```
#### istitle()
* istitle() will return True if s is a title cased string and there is at least one character in s, i.e. uppercase characters may only follow uncased characters and lowercase characters only cased ones. It returns False otherwise.
````
s.istitle()
````
#### isupper()
* isupper() will return True if all cased characters in s are uppercase and there is at least one cased character in s, False otherwise.
```
s.isupper()
```
#### endswith()
* Another method is endswith() which is essentially the same as a boolean check on s[-1]
```
s.endswith('o')
```
### Built-in Reg Expressions
* Strings have some built-in methods that can resemble regular expression operations. We can use split() to split the string at a certain element and return a list of the results. We can use partition() to return a tuple that includes the first occurrence of the separator sandwiched between the first half and the end half.
```
s.split('e') # returns ['h', 'llo']

s.partition('l') # returns ('he', 'l', 'lo')
```
***
# Advanced Sets
* some methods for sets
```
s = set()
```
#### add
s.add(1)
#### clear
* removed all elements from the set
```
s.clear()
```
#### copy
* returns a copy of the set
```
s = {1,2,3}
sc = s.copy()
```
#### difference
* shows the difference between 2 sets
* syntax: ```set1.difference(set2)```
```
s.difference(sc)
```
#### difference_update
* this returns set1 after removing elements found in set2
```
s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2)
print(s1)
```
#### discard
* Removes an element from a set if it is a member. If the element is not a member, do nothing.
```
s.discard(2)
```
#### intersection and intersection_update
* finds the items in common between 2 sets and makes a new set with those elements 
```
s1 = {1,2,3}
s2 = {1,2,4}
s1.intersection(s2)
# returns {1, 2}

# intersection_update will update a set 
# with the intersection of itself and another.
s1.intersection_update(s2)
# s1 will print {1, 2}
```
#### isdisjoint
* This method will return True if two sets have a null intersection.
```
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
s1.isdisjoint(s2)
# False
s1.isdisjoint(s3)
# True
```
#### issubset
* This method reports whether another set contains this set.
```
s1.issubset(s2)
```
#### issuperset
* This method will report whether this set contains another set.
```
s2.issuperset(s1)
```
#### symmetric_difference and symmetric_update
* Return the symmetric difference of two sets as a new set.(i.e. all elements that are in exactly one of the sets.)
```
s1
#{1, 2}
s2
# {1, 2, 4}
s1.symmetric_difference(s2)
# {4}
```
#### union
* Returns the union of two sets (i.e. all elements that are in either set.)
```
s1.union(s2)
```
#### update
* update a set with the union of itself and others
```
s1.update(s2)
```
***
# Advanced Dictonaries 
#### Dictionary Comprehensions
* Dictionary Data Types also support their own version of comprehension for quick creation. It is not as commonly used as List Comprehensions, but the syntax is:
```
{x:x**2 for x in range(10)}
# returns {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```
* One of the reasons it is not as common is the difficulty in structuring key names that are not based off the values.
#### Iteration over keys, values, and items