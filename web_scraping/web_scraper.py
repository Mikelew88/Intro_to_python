import pandas as pd
import datetime

from bs4 import BeautifulSoup
import urllib2

def scrape_page(area, url):

        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'lxml')

        seven_day_forecast = soup.find("div", {"id": "seven-day-forecast-container"})

        forecast_gen = seven_day_forecast.findAll("li", {"class":"forecast-tombstone"})

        print '=================================================='
        print '{} Forcast'.format(area)
        for day in forecast_gen:
            print day.find("p", {"class":"period-name"}).getText()
            print day.find("p", {"class":"short-desc"}).getText()
            try:
                print day.find("p", {"class":"temp-high"}).getText()
                print ''
            except:
                print ''
        print '=================================================='


if __name__ == '__main__':
    areas = [{'Lincoln Lake':'http://forecast.weather.gov/MapClick.php?lat=39.75511089465317&lon=-104.98275154414773#.V_VwSJMrKL4'}, {'Emerald Lake': 'http://forecast.weather.gov/MapClick.php?lat=40.309780&lon=-105.664947#.V_V3vJMrKL7'}]

    for area in areas:
        for area, coordinates in area.iteritems():
            scrape_page(area, coordinates)
