import os
import pandas as pd
import psycopg2

<<<<<<< HEAD
=======

>>>>>>> a80a29742329874479a2b9dde2d7c769ee625777
def pull_data():
    ''' Pull name, gender counts from redshift

    input:  (none)
    output: dataframe
    '''
    con=psycopg2.connect(dbname='ibotta', host=os.environ['REDSHIFT_ENDPOINT'],
    port='5439', user=os.environ['REDSHIFT_USER'], password=os.environ['REDSHIFT_PASS'])

    query = '''
    select first_name, gender, sum(1) as n, case when gender = 'M' then .788 else .212 end as weight
    from customers
    where gender in ('M', 'F')
    group by 1, 2
    ;
    '''

    # weight n by number of users in that gender
    df = pd.read_sql_query(query, con)
    df['weighted_n'] = df.eval('n * weight')
    return df

def identify_name(df, name):
    ''' Given a name, predict the gender based on most common gender of name

    input:  df - Pandas dataframe returned by pull_data (df)
            name - Name that we are predicting the gender of ('string')

    output: gender - Gender of name ('string')
    '''
    try:
        df_query = df.query("first_name == @name")
        if df_query.ix[df_query['weighted_n'].idxmax()].gender == 'M':
            print "I think you're male"
        else:
            print "I think you're female"
        return
    except ValueError:
        print "You have a very unique name, I'm not sure what you are!"
        return

if __name__ == '__main__':
    print 'Querying Database...'
    df = pull_data()

    while True:
        identify_name(df, raw_input("What is your name: "))
        print
