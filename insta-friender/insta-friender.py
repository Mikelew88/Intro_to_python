import pandas as pd

from bs4 import BeautifulSoup
import urllib2

with open('data/followers', 'r') as page:
    soup = BeautifulSoup(page, "html5lib")

follower_html = soup.findAll('li', {'class':'_cx1ua'})

to_follow = []
for follower in follower_html:
    if follower.find('button', {'class':'_aj7mu'}).text == 'Follow':
        to_follow.append(follower.find('a', {'class':'_4zhc5'}).text)
