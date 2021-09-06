# Object Oriented Programming 
***
***
# Introduction 
* allows programmers to create their own objects that have methods and attributes
* commonly repeated tasks and objects can be defined with OOP to create code that is more usable
* **ex:**
```
class NameOfClass():
      def _init_(self,param1,param2):
          self.param1 = param1
          self.param2 = param2
      def some_method(self):
          #perform some action
          print(self.param1)
```
* classes use an upper case naming scheme
* **class defines an object** 
* the def _init_ portion looks like a function but is actually a method because it is in a class
* to connect the methods to the class you need to use a self keyword

# Attributes and the Class Keyword
* class defines the blueprint of a future object
* from classes you can then make an instance of the object
* an instance is a speific object created from a particular class
* simple class example:
```
class Sample():
      pass

```
* notes:
* notice how class uses upper case in the names
* create an instance of the class example:
```
my_sample = Sample()
type(my_sample) # returns __main__.Sample
```
* add attributes example:
```
class Dog():
      def __init__(self,breed):
          self.thebreed = breed 
          # self.attribute_name

my_dog = Dog(breed='beagle')
my_dog.thebreed #returns beagle
```
* the init method is called upon whenever you create an instance of the class 
* you always start with the self keyword which connects the method to the instance of the class / represents the instance of the object itself
* you then pass in any attributes that you want the user to define (in this case breed)
* you can then give those attribues assignments
* notice how the paramater "breed" is not the same as the attribute "mybreed" - they can be names the same however they dont have to be
* more examples:
```
class Dog():
      def __init__(self,breed,name,spots):
          self.breed = breed 
          self.name = name
          # spots expects a boolean 
          self.spots = spots 

my_dog = Dog(breed='beagle',name='Donny',spots=False)
my_dog.breed 
my_dog.name
my_dog.spots
```
* Notice how you cant explicitly say you want spots as a boolean in this example. That would typically be covered in documentation. If you put spots as a string Python wouldnt complain.

# Class Object Attributes and Methods
## Class Object Attributes
* you can create attributes that will be the same for each class instance. you can do this by defining an attribute above the __init__ definition. these are known as "class object attributes"
*example:
```
class Dog():
      # class object attribute (same for any instance)
      species = 'mammal'
   
      def __init__(self,breed,name,spots):
          self.breed = breed 
          self.name = name
          # spots expects a boolean 
          self.spots = spots 

my_dog = Dog(breed='beagle',name='Donny',spots=False)
my_dog.breed 
my_dog.name
my_dog.spots
my_dog.species
```
* notice how you dont use the "self" before species
* notice how you also dont need to define species when calling Dog()
## Methods
* methods are **functions defined inside the body of a class** and they are used to perform operations that sometimes utilize the attributes of the object
* methods are more of actions or operations
```
class Dog():
      # class object attribute (same for any instance)
      species = 'mammal'
      
      def __init__(self,breed,name):
          # ATTRIBUTES
          self.breed = breed 
          self.name = name

       # OPERATIONS/ACTIONS ---> METHODS
       def bark(self):
            print("WOOF! My name is {}".format(self.name))

my_dog = Dog(breed='beagle',name='Donny')
my_dog.bark() # runs the bark method
```
* when you call attributes they dont have "()" - this is because they arent something you really execute - its just information or a characteristic 
* when you run a method you include the "()"
* notice how in the method when you call the attributes you use ```self.attribute_name```
* methods can also take outside arguments - so you could do something like this:
```
       # OPERATIONS/ACTIONS ---> METHODS
       def bark(self,number):
            print("WOOF! My name is {} and the number is {}".format(self.name,number))

my_dog = Dog(breed='beagle',name='Donny')
my_dog.bark(50) # runs the bark method
```
* notice the new paramater number, and notice how its not refrenced with ```self.```
* notice how when you call bark you now pass in the number