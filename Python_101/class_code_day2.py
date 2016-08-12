import pandas as pd

#looping through str

#loop through letters
for letter in str:
    print letter

#loop through words
for word in str.split():
    print word

df = pd.read_csv('/Users/MikeLewis/Intro_to_python/us-united-states/8--co-colorado--rocky-mountains/beers.csv')
