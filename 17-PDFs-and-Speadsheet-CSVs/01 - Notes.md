# Working with PDFs and Spreadsheet CSV Files
***
***
# Working with CSV Files in Python
* csv != to excel
* libraries for excel: ```http://www.python-excel.org/``` and ```https://www.xlwings.org/```
* Files in the CSV format are generally used to exchange data, usually when there's a large amount, between different applications. Database programs, analytical software, and other applications that store massive amounts of information (like contacts and customer data), will usually support the CSV format.

## Reading CSV Files
```
import csv
data = open('example.csv') # or entire file path
```
* ```data``` =  ```<_io.TextIOWrapper name='example.csv' mode='r' encoding='cp1252'>```
#### encoding
* csv files sometimes contain characters that python cant interpret (like an @ sign)
* this might throw an error because it cant encode it:
```
csv_data = csv.reader(data)
data_lines = list(csv_data)
```
* you could try adding utf-8 encoding:
```
data = open('example.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)
data_lines[:3]
```
* the first item in the list is the header line, this contains the information about what each column represents
```
for line in data_lines[:5]:
    print(line)
```
* example of grabbing all the emails:
```
all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])
```
* when things are read it puts them in a list like this: ```['1', 'Joseph', 'Zaniolini', 'jzaniolini0@simplemachines.org', 'Male', '163.168.68.132', 'Pedro Leopoldo']```
* in this code snipit its saying get index 3 of the list where the email is 
* pulling names for example:
```
full_names = []

for line in data_lines[1:15]:
    full_names.append(line[1]+' '+line[2])
```
## Writing CSV Files for Example
#### new file
* this also will overwrite a existing files with the same name
```
# newline controls how universal newlines works (it only applies to text
# mode). It can be None, '', '\n', '\r', and '\r\n'. 
file_to_output = open('to_save_file.csv','w',newline='')

csv_writer = csv.writer(file_to_output,delimiter=',')

csv_writer.writerow(['a','b','c'])

csv_writer.writerows([['1','2','3'],['4','5','6']])

file_to_output.close()
```

#### existing file
```
f = open('to_save_file.csv','a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['new','new','new'])
f.close()
```

## Another library
* the pandas library is also good for CVS files: ```https://pandas.pydata.org/```