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
* if you have a class object attribute called pi and a class of Circle..instead of using self.pi you could use Circle.pi
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

# Inheritance and Polymorphism
## Inheritance
* inheritance - a way to form new classes using classes that have already been defined
* benifit: its a way to re-use code and reduce the complexity in a program 
* base class example:
```
class Animal():
      def __init__(self):
          print("Animal Created")
        
      def who_am_i(self):
           print("I am an animal")
      
      def eat(self):
          print("I am eating")

myanimal = Animal()
myanimal.who_am_i()
```
* another function that uses the methods of our base class:
```
class Dog(Animal):
      def __init__(self):
          # runs the init in the Animal class
          Animal.__init__(self) 
          print("Dog Created")

mydog = Dog()
mydog.who_am_i # uses the method from the Animal class
```
* we passed in "Animal" so its now a derived class- we then create an instance of the animal object within the init for Dog
* after passing in the Animal init the methods created in Animal can now be used with Dog
* if you want to overwrite a method in the parent class from within the current class you can just define it again with the same name - so you could redefine this in Dog:
```
# from within the Dog class
def who_am_i(self):
           print("I am a dog not an animal like shown in the animal class")
```
## Polymorphism
* not really used until later in your Python career 
* refers to the different ways different object classes can share the same method name - those methods can then be called from the same place even throgh a variatey of different objects might be passed in
```
class Cat():
      def __init__(self,name):
          self.name = name

      def speak(self): 
          return self.name + " says woof!"

class Dog():
      def __init__(self,name):
          self.name = name

      def speak(self): 
          return self.name + " says meow!"

niko = Dog("niko")
felix = Cat("felix")    

print(niko.speak())
print(felix.speak())

for pet_class in [felix,niko]:
    print(type(pet))
    print(type(pet.speak()))

def pet_speak(pet):
    print(pet.speak())
pet_speak(niko)
pet_speak(felix)
```
* both classes share the same method name however they do something different in thier methods

### Abstract classes
* usually only designed to act as a base class and is never really used
* see below - Animal is a base class - there is no intent to ever make an instance of it - it just acts as a base class
```
class Animal():
      def __init__(self,name):
          self.name = name

       def speak(self):
          raise NotImplementedError("Subclass must implement this abstract method")
       
class Dog(Animal):
      def speak(self):
          return self.name+ " Says woof!"
class Cat(Animal):
      def speak(self):
          return self.name+ " Says meow!"

fido = Dog("fido")
tom = Cat("tom")
print(fido.speak())
```
* notice how we have the init in the base class however it doesnt exist in the other classes - we can still create instances of cat and dog tho
* **ex use cases for this:**
* for example you may want to make a class for opening files. you could make a base class and then make sub classes with an "open" method for each file type ...like pdf or .xlsx 

# Special (Magic/Dunder) Methods
* they allow us to use some built in operations with python such as the lenght function or the print function with our own user created objects
* example of not being able to use some normal python functions with a class
```
mylist = [1,2,3]
len(mylist)

Class Sample():
    pass

mysample = Sample()
len(mysample)  # throws an error
print(mysample) # throws an error
```
* example of a special method
```
class Book():
     def __init__(self,title,author,pages):
         self.title = title
         self.author = author 
         self.pages = pages
     def __str__(self):
         return f"{self.title} by {self.author}"

b = book("Book name", "author name",200 )
print(b) #prints what is in the __str__ method
```
* ```__str__``` is a **special method**. It essentially says when you ask for a string representation of this class, do the code in the method
* another example:
```
def __len__(self):
    return self.pages
```
* another example:
```
del b
```
* this will delete the b instance from the memory
```
def __del__(self):
    print("a book object has been deleted")
```
* that special function for ```del``` now specifies what to do when ```del``` is run on an object
* there are other methods however these are the main ones

# More Examples:
## Tuple unpacking within a class:
```
class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
```