# excercise

from bs4 import BeautifulSoup
import requests


url = "https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol"

page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')

print(soup)


# lets get Stock price of apple.

stock_price=soup.find_all('bg-quote',class_='value')[0]

print(stock_price.text)
# Done.

# 2) find closing price of day

closing_price = soup.find('td',class_='table__cell u-semi')
print(closing_price.text)


# lets find 52 weeks range header.

# weeks low
year_range = soup.find_all('div',class_="range__header")[2]
print(year_range)

# year low

year_low=year_range.find('span',class_="primary")
print(year_low.text)

#weeks high

year_high = year_range.find_all('span',class_="primary")[1]
print(year_high.text)

# Analysis Rating

analysis = soup.find_all("div",class_="analyst__chart")
print(analysis)

# done.
rating = soup.find('li',class_="analyst__option active").text
print(rating)


# lets work with microsoft stocks.

from bs4 import BeautifulSoup
import requests

url = "https://www.marketwatch.com/investing/stock/msft?mod=search_symbol"

page = requests.get(url)

soup = BeautifulSoup(page.text,"lxml")

print(soup.prettify())

# got the stock price.
stock_price = soup.find('bg-quote',class_="value")

print(stock_price.text)

year_range = soup.find_all('div',class_="range__header")[2]
print(year_range)

# year low
year_low = year_range.find('span',class_="primary")
print(year_low.text)

# year high

year_high = year_range.find_all('span',class_="primary")[1]
print(year_high.text)


a=soup.find('li',class_="analyst__option active")

print(a.text)