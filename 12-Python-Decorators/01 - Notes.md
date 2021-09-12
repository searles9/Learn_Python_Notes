# Python Decorators
***
***
# Decorators with Python
*Python has **decoratros** that allow you to tack on extra functionality to an already existing function
* The use the ```@``` operator and are then placed on top of the original function
* example syntax:
```
@some_decorator
def simple_func():
     # do stuff
```

* Nesting a function:
```
def hello(name='Jose'):
    print('the hello() function has been executed!')
    def greet():
        return '\t This is the greet() function within hello'
    def welcome():
        return 'this is welcome() inside hello'
    
    if name == 'Jose':
       return greet
    else:
       return welcome

my_new_func = hello('Jose')
my_new_func() #now runs the nested greet function
```

* passing in a function as a argument:
```
def hello():
    return 'Hi Jose'

def other(some_def_func):
    print('Other code runs here)
    print(some_def_function())

other(hello) # passing in the hello function 
```
* example of a decorator
```
def new_decorator(original_func):
    def wrap_func():
         print('some extra code before the original function')

         original_func()

         print('Some extra code after the original function')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print('I want to be decorated')
```
* this basically takes a function then adds some additional functionality to it by returning the original function + the extra code (specified using the @)
* decorators are commonly used in web frameworks - basically adds extra code
