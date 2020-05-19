import order_data
import numpy
import pandas as pd


def dict_gen_scatterplot1(labels, values):
    if values == None or labels is None:
        raise Exception
    df = pd.read_csv("fc1.csv", usecols= [ labels, values] )
    order_data.is_df_null(df)
    columns_titles = [labels , values]
    df  = df.reindex(columns=columns_titles)
    df.columns = ['label', 'value'] 
    df= df.drop_duplicates("label")
    df = df.sort_values(by=['value'])
    return df.to_dict('records')
