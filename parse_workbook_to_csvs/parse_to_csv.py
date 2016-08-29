import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('data/Tagging_MJJ_Targeted_Customers_MECE.csv')

    for tag in df.tag.unique():
        df.query('tag == @tag').to_csv('data/tag_'+tag+'.csv', index=False)
