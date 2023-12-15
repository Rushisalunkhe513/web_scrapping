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
# this will give us all product_name data.
product_name = soup.find_all('a',class_="title")
print(product_name)

# now we only want string data from the tag.
# we can get it like this
# .text only works on single tag.
name = soup.find('a',class_="title").text
print(name)

# lets do similarly with review,description,price.

prices= soup.find_all('h4',class_="float-end price card-title pull-right")
print(prices)

reviews = soup.find_all('p',class_="float-end review-count")
print(reviews)

descriptions = soup.find_all('p',class_="description card-text")
print(descriptions)

# now we will append all the text data from this tag into string.

product_list = []
price_list = []
review_list = []
description_list = []

for product in product_name:
    product_list.append(product.text)
    
for price in prices:
    price_list.append(price.text)
    
for review in reviews:
    review_list.append(review.text)
    
for description in descriptions:
    description_list.append(description.text)

# Now We can see all data in list.     
print(product_list)
print(price_list)
print(description_list)
print(review_list)
    
# lets make table by using pandas library

import pandas as pd

# we will create dataset by pandas library

table = pd.DataFrame({"product_data":product_list,"price_data":price_list
                      ,"review":review_list,"description_data":description_list})  


# Now we will get data from nested html tags.

boxes = soup.find_all('div',class_="col-md-4 col-xl-4 col-lg-4")[2]
print(boxes)   

# Find_all will give us data in list format
# so , now to find how much box data we have in this, lets use len function on boxes.

#print(len(boxes))

# This will give us data of 2 nd div and its nested tags.
#print(boxes[1])

# now from this boxes we will be needing the inside tags like <a> tag.

# This will get us <a> tag from <div> tag.
print(boxes.find('a').text)

# This will get us p tag with its class inside div tag.
print(boxes.find('p',class_="float-end review-count").text)

a_tag = boxes.find_all('a',class_="title")

print(a_tag)


# lets work with sliding tags

box_tag = soup.find_all("div",class_="col-lg-3 sidebar")[0]

print(box_tag)

print(box_tag.find('a',class_="nav-link subcategory-link active").text)

print(box_tag.find_all('li',class_="nav-item")[1])


print(box_tag.find_all('ul',class_="nav ",id='side-menu'))