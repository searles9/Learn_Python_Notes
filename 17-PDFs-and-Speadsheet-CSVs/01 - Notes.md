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
* the first item in the list is the **header line**, this contains the information about what each column represents
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
* pandas can work with sql files, excel files, etc - essentially most tabular data types
* you could also use the googlesheets Python API for interacting directly with google spreadsheets

## Some key points:
#### Clear example opening a csv file and reading it:
```
# open the file with encoding
data = open('example.csv',encoding="utf-8")
# read as csv
csv_data = csv.reader(data)
# format data into a python object (list of lists)
data_lines = list(csv_data)
# ------------------------------------------------------
# read the first item which is a list 
# ex: data_lines[10][3]  - row 10 item 3 (index starts at 0)
# of the headers - data_lines[0]:
for line in data_lines[:5]:
    print(line)
# ------------------------------------------------------
# grab one of the item in each row:
all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])

# more grabbing data:
full_names = []

for line in data_lines[1:15]:
    full_names.append(line[1]+' '+line[2])
# ------------------------------------------------------
```

#### Clear example of writing to an existing CSV file
```
# open the existing file - comma delmitied 
f = open('to_save_file.csv','a',newline=',')
# indicate what we are writing
csv_writer = csv.writer(f)
# write a single row - has to match the rows that are there
csv_writer.writerow(['new','new','new'])
# write 2 rows - notice 2 lists
csv_writer.writerow(['new','new','new'],['a','b','c'])
# close the file
f.close()
```

***
***

# Working with PDF Files in Python
* a common lbrary for working with PDFs is PyPDF2
```
pip install PyPDF2
```
*  not every PDF file can be read with this library. PDFs that are too blurry, have a special encoding, encrypted, or maybe just created with a particular program that doesn't work well with PyPDF2 won't be able to be read
* more libraries: https://www.binpress.com/manipulate-pdf-python/
*  PyPDF2 can only read text  - not images or other media
* this library probably wont be able to read a scanned pdf
```
# note the capitalization
import PyPDF2
```
#### read a pdf
* open the pdf then create a reader object for it
```
# Notice we read it as a binary with 'rb'
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
pdf_reader.numPages
page_one = pdf_reader.getPage(0)
# then extract the text
page_one_text = page_one.extractText()
page_one_text
f.close()
```
#### adding to PDFs
* you cant write to a pdf - what you can do is copy pages and append pages to the end:
```
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)
pdf_output = open("Some_New_Doc.pdf","wb")
pdf_writer.write(pdf_output)
f.close()
```

#### example of grabbing text from a PDF
```
f = open('Working_Business_Proposal.pdf','rb')

# List of every page's text.
# The index will correspond to the page number.
pdf_text = []

pdf_reader = PyPDF2.PdfFileReader(f)

for p in range(pdf_reader.numPages):
    
    page = pdf_reader.getPage(p)
    
    pdf_text.append(page.extractText())

print(pdf_text)
print(pdf_text[3])
```











