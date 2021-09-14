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