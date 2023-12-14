# web_scrapping

Web Scrapping is use of program which helps us to extract large amount of data from the website.

Whether you are a data scientist, engineer, or anybody who analyzes large amounts of datasets, the ability to scrape data from the web is a useful skill to have.

    # Major use of webScrpping is--->

    1) Mainly Machine learining/Data Science to get data from websites.

    2) looking for Reservation at hotel,lodge

    3) Looking up shopping sites for cheaper price on same product.

    4) Reading or extracting Stock data from website.


# There are two types of web scrapping.
    --> 1) Fetching =  Downloading of page (happens when user views a page in browser)
    --> 2) Extracting = page data is parsed,extracted to obtaing piece of data from it.


---> we will use of html og page and use beautifulsoap to extract data from it.

also there is two types of pages.
1) which contain Html language--> will be using BeautifulSoup.
2) other javascript driven pages.--> will be using selenium.



Note:--->
    We can actually access 99% of data from websites.
    some webites have checkbox like #i am not robot which is for keep webscrappers away from there data.
    we cant access this websites data.


# BeautifulSoup-->
BeautifulSoup is python library to extract data from the HTML pages.
Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.

# lxml-->
lxml is one of the fastest and feature-rich libraries for processing XML and HTML in Python.

# requests-->
Requests allow you to send HTTP/1.1 requests.


### Searching and Extracting From the HTML
Most powerful functions in BeautifulSoup which are the find and find_all functions. These functions will be predominantly used throughout the course to find specific lines of HTML code that have the data that we want to scrape.