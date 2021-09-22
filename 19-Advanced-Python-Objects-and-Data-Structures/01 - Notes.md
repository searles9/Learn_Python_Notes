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