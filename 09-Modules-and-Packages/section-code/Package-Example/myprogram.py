# myprogram from within the package
# to run: python myprogram.py

#Import the mainscript module
from MyMainPackage import mainscript
# Import the subscript module from 
# the sub package "SubPackage" which is in 
# the main package "MyMainPackage" 
from MyMainPackage.SubPackage import subscript

# From the main script
# executing "report_main" function 
# which is in the mainscript module 
# which is in the MyMainPackage package
mainscript.report_main()

# From the sub script
# executing the "sub_report" function which
# is in the subscript module
# which is in the MyMainPackage package
subscript.sub_report()
