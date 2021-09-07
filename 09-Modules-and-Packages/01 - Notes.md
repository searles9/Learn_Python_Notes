# Modules and Packages
***
***
# Pip Install and PyPi
* PyPi is a repository for open-source third-party Python packages (its imilar to RubyGems in the Ruby world, PHP Packagist, CPAN for Perl and NPM for Node.js)
* These libraries are different from the built in libraries like the Math library in Python
* we can install these 3rd party packages with ```pip install```
* when you install Python from ```python.org``` or through Anaconda pip is installed
* example use from CMD:
```
# this package allows you to request info from websites online
pip install requests 
```
```
# this allows you to print out colorized text 
# at the command prompt
pip install colorama

# to use it:
python
from colorama import init
from colorama import Fore
print(Fore.RED + "SOME RED TEXT")
print(Fore.GREEN + "SWITCH TO GREEN")
quit()
```
## Searching Google for Python Packages
* just google something like: ```python package for excel```
* you will find something like this: ```https://www.python-excel.org/```
* you can go to the download which will take you to pypi
* the documentation is usually linked and is often hosted on ```readthedocs.io```
* the documentation will show how to install and use the package
```
pip install openpyxl
import openpyxl
```
# Creating Your Own Modules and Packages 
## Modules
* modules are just .py scripts that you call in another .py script
* **syntax for importing from a module:**
```
from mymodulescriptname import the_func_name_from_the_module
```
* **example of a module and package:**
```
# mymodule.py <-------------------
def my_func():
    print("This is a module - fun times")
```
```
# myprogram.py <-------------------
from mymodule import my_func

my_func()
```
## Packages
* packages are a collection of modules
* to make python realize its a package you need to add an ```__init__.py``` file to the package folders (nothing needs to be in the file - the file just needs to be there so Python knows its a package)
* see the section code for a package example - you can see how the ```myprogram.py``` file interacts with the modules in the packages