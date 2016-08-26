import pandas as pd
import numpy as np

def import_data(url):
    df = pd.read_csv(url)

    return df.ix[:,:7]

def remove_ipl_2993():
    cond1 = df['Dashboard Type'] == "Ibotta Poll Share"
    cond2 = df['Campaign Ids'].str.match('2993+')
    return df[np.invert(cond1 & cond2)]

if __name__ == '__main__':
    df = import_data('https://s3.amazonaws.com/uploads.hipchat.com/27706/209536/njhOv5BemlIeS0E/dashboard.csv')
    df = remove_ipl_2993(df)
