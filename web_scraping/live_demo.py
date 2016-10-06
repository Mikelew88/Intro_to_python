import urllib2
from bs4 import BeautifulSoup

url = "http://forecast.weather.gov/MapClick.php?lat=39.75511089465317&lon=-104.98275154414773#.V_VwSJMrKL4"

page = urllib2.urlopen(url)

soup = BeautifulSoup(page, 'lxml')

seven_day_forecast = soup.find("div", {"id":"seven-day-forecast-container"})

for i in seven_day_forecast.findAll("li",{"class":"forecast-tombstone"}):
    print i.prettify()
    print "---------------------------"
    print



urls = ["https://www.walmart.com/ip/Welch-s-Mixed-Fruit-Fat-Free-Fruit-Snacks-.9-oz-22ct/17247711", "https://www.walmart.com/ip/Kellogg-s-Rice-Krispies-Treats-Original-Crispy-Marshmallow-Squares-0.78-oz-16-count/10818666"]

data_dict = {}

for url in urls:
    page = urllib2.urlopen(url)

    soup = BeautifulSoup(page, 'lxml')

    key = soup.find("h1", {"itemprop":"name"}).getText()
    val = soup.find("span", {"itemprop":"sku"}).getText()

    data_dict[key] = val
