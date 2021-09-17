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

#### Libraries
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

# Setting up Web Scraping Libraries