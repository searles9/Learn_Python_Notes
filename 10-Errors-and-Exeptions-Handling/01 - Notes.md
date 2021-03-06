# Errors and Exeptions Handling
***
***
# Errors and Exeption Handling
* you can use error handling to attempt to plan for possible errors 
### Try:
* this is the code that you want to attempt to run
### Except: 
* this is the code that will execute when there is an error in the ```try block```
* **Python built in exception types:** ```https://docs.python.org/3/library/exceptions.html```
### Finally: 
* this block of code is executed regardless of an error 
<br><br>
* this could fail, and is not setup to expect errors:
```
def add(n1,n2):
    print(n1+n2)

add(10,two) # this will error
```
* this is an example of something that is designed to expect errors:
```
try:
    # code to attempt
    result = 10+10
except:
    # code to run if try errors
    print("there is an error")
else:
    print("Add went well!")
    print(result)
```
* check for a specific error type example:
```
try:
   f = open('testfile','w')
   f.write('write a test line to the file')
except TypeError: 
    # ex they gave a string instead of a integer
    print('there was a type error')
except OSError:
    # this can occur if you try to 
    # write to a file that you dont have 
    # permissions to 
    print('You have an OS Error -check if you have permissions to the file!')
except:
    # all other exeptions
    print('All other exeptions')
finally:
    # this executes no matter what
    print('I always run even if we hit an error')
```
* this is an example of using try except in a function:
```
def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("whoops that is not a number")
            continue
        else:
            print("Thank you for the number")
            break
        finally:
            print("This always runs even if you have an error")
```

# Pylint and Unit Testing
* ```pylint myexample.py -r y```
* as you begin to expand to larger multi-file projects it becomes important to have tests in place - this way if you make changes to the code you can run your test files to make sure previous code still runs as expected
### Testing tools
* **Pylint:** this library looks at your code and reports back possible issues
* **Unittest:** (built in to python) this built in library will allow you to test your own programs and check if you are getting the desired output

## Pylint
* to install:
```
pip install pylint
```
* example file:
```
# testingpylint.py
a = 1
b = 2

if __name__ == "__main__":
    print(a)
    print(B) # notice this error
```

* to check for errors:
```
pylint testingpylint.py -r y

# you will get this error: testingpylint.py:7:10: E0602: 
# Undefined variable 'B' (undefined-variable)
#
# Your code has been rated at -8.00/10
```

## Unittest - Unit Testing
* **see the section code folder for an example**
* Basic steps:
* import unit testing
* import your functions to test
* create a class for testing. Inherit from ```unittest.TestCase```
* create methods to test your functions - ```self.assertEqual(result,'expected result')```
* unittest.main()
