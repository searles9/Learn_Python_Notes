# Web Scraping with Python
***
***
# Intro
* web scraping is a general term for techniues involving automating the gathering of data from a website
* with webscraping you can download images or info from a website

#### How do websites work?:
* you request data from site
* site sends you the front end code (like html)

#### Rules:
* if you make too many web scraping requests your IP Address could get blocked - always check if you can get permission 
* some sites automatically block scraping software

#### Limitations:
* every website is unique so 1 sript wont work for every website
* a slight change to the website could break your web scraping script 
* the script you make is usually pretty static so you will have to make changes over time

# Setting up Web Scraping Libraries
* **to web scrape you can use the BeautifulSoup and the requests libraries (not built into python)**
```
pip install requests
pip install lxml # BeautifulSoup related
pip install bs4 # installs BeautifulSoup
```
* or for anaconda:
```
conda install requests
conda install lxml
conda install bs4
```

#### use them:
```
import requests
import bs4
```

# grabbing a title
```
import requests
```
* grab the page
* sometimes you need to run this twice if it fails the first time
```
res = requests.get("http://www.example.com")
```
* this response object contains the info from the page as a string - ```requests.models.Response```
* ```res.text```
```
type(res)  # returns requests.models.Response
```
* beautiful soup helps you parse the data from the response object
```
import bs4

# passing in the text string from the response object
# passing in a string code to show what engine to use to parse it
soup = bs4.BeautifulSoup(res.text,"lxml")

# show it in an easier to read format: 
print(soup)

# get the title - 
# returns [<title>Example Domain</title>]
soup.select('title')
```
* if you use select it could grab multible items. It will put them in a list. You need to grab your specific item.
```
soup.select('title')[0].getText()
```
* or
```
paragraphs = soup.select("p")
paragraphs[0].getText()
```
* its actually not a string. its a beautiful soup object so you have to use .getText() to get the actual string

* **full example**
```
import requests
import bs4
res = requests.get("http://www.example.com")
soup = bs4.BeautifulSoup(res.text,"lxml")
print(soup.select('title')[0].getText())

paragraphs = soup.select("p")
paragraphs[0].getText()
```
* you are basically making a request, using beautiful to parse the data and then selecting the items - you can then pull the text from said items

# Grabbing a class (css)