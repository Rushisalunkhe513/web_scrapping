# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

page = requests.get(url)
print(page.text)

# after this we will get response 200.
# which says we can get html from webpage.

soup = BeautifulSoup(page.text, 'lxml')
# this will show us in more html format.
print(soup)


# tags 
# to get data from between html tags we will use the html tags to get specific data

print(soup.header)

# this soup.div will only give first occurence of div in html page.
print(soup.div)

# soup.prettify() is printed, it gives the visual representation of the parse tree created from the raw HTML content.
# also,soup.header.prettify() will give data within header tag as it is written in html.
print(soup.header.prettify())

# will give output as it is written in html.
print(soup.div.prettify())

# A NavigableString object holds the text within an HTML or an XML tag.

# first lets take variable and give it navigation string values inside of header

tag = soup.header.p


# as you can see in output there is ionly one p tag in header and its Web Scrapper
print(tag)

# now we dont need html syntax in the tag, only want string from it.
# so use..

# it will only show string inside html tag <p>
print(tag.string)


# getting data from attributes.
# attributes are actually in oarange/yellow color and comes after htmltag like class,id etc.

# this will give all attributes in a tag
tag_a  = soup.header.a

print(tag_a.attrs)

# this will give 
print(tag_a["data-bs-toggle"])

# we can also add new attribute to html page content

tag_a["new_attribut"]="this is external added attribute"

# Gives us all attributes from <a> tag
print(tag_a.attrs)

print(tag.comments)
