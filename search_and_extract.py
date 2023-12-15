# Searching and extracting data from html pages by find_all() function.
# find_all() function will allow us to find specific data we want to scrap from website.


#lets import libraries

from bs4 import BeautifulSoup
import requests

# new website to exercise the web scrapping.
url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

# will load page data in variable
page = requests.get(url)

# now we will load it in soup variable with Beautifulsoap

soup = BeautifulSoup(page.text, "lxml")

print(soup)
print(soup.prettify())


tag = soup.header

print(tag.prettify())

print(soup.header.p.prettify())

print(soup.header.p.string)

print(soup.header.attrs)

print(soup.header.a.attrs)

tag_attrs = soup.header.a.attrs

print(tag_attrs["data-bs-toggle"])


# Now we will be using find function to get specific data from webpage

# This will return everythin in header tag as well
# also it is similar to soup.header

print(soup.find('header'))

# now to get specific div tag with class name 
print(soup.find("div",{"class":"container-fluid blog-hero"}))

# This is how we can get specific div tag by its class

# also this is how we can get any tag info we  wanty by giving there class name
print(soup.find('h4',{"class":"float-end price card-title pull-right"}))

# img tag with its own class

print(soup.find("img",{"class":"img-fluid card-img-top image img-responsive"}))



# now lets do about a tag

print(soup.find("a",{"class":"title"}))

# lets do about p tag

print(soup.find("h4",{"class":"float-end price card-title pull-right"}))

# now we will see find_all() function.
# if there are multiple tags with same class then we can jse find all to find all tags with same class name
print(soup.find_all("h4",{"class":"float-end price card-title pull-right"}))

# returns all a tag with class title
print(soup.find_all("a",{'class':{"title"}}))

# returns all p tag with class float-end review-count.
print(soup.find_all("p",{"class":"float-end review-count"}))

# now if we want specific price then we can do it like list.
print(soup.find_all("h4",{"class":"float-end price card-title pull-right"})[1:])


# we can also use find_all() to find multiple tags from html page

# This line will return all h4 and p tags from the html page content.

print(soup.find_all(["h4","p"]))

# lets get 3 or 4 tags from html page

print(soup.find_all(["h4","a","p","div"]))



# lets find all html tags who have id as there attribute.
# This will return all attributes which have id.
print(soup.find_all(id = True))


# we can also find all by string 
# this will give us all string by 'Iphone'
print(soup.find_all(string = 'Iphone'))
print(soup.find_all(string = 'Samsung Galaxy'))

print(soup.find_all(string = "Iph"))

# now if we want to find all Data which have certain letter in it.

import re
# This will return all the data which have Iph in it.
print(soup.find_all(string = re.compile('Iph')))

# this will return all the data which have Cap S in it.
print(soup.find_all(string = re.compile('S')))

# this will return all data which have no in it.
print(soup.find_all(string = re.compile(('No'))))

# if we want to find all classes from the html page content
# This will return all tags which have class as pull to it.
 
print(soup.find_all(class_= re.compile("pull")))


# if we want to find specific tag with class in it.
# This will return all p tags.
print(soup.find_all('p'))
# This will return all p tags with class as description card-text.
print(soup.find_all('p',class_=re.compile("description card-text")))

# if we want only 2 of this p tag with same class.

print(soup.find_all('p',class_=re.compile("description card-text"),limit=2))

# we can alson find by multiple string.
# this will return all strings with Nokia 123 and Iphone.

print(soup.find_all(string = ("Nokia 123","Iphone")))
