import order_data
import numpy
import pandas as pd


def dict_gen_scatterplot1(labels, values):
    df = pd.read_csv("fc1.csv", usecols= [ labels, values] )
    columns_titles = [labels , values]
    df  = df.reindex(columns=columns_titles)
    df.columns = ['label', 'value'] 
    df= df.drop_duplicates("label")
    df = df.sort_values(by=['value'])
    return df.to_dict('records')
