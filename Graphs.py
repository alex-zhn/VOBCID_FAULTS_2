# from IPython import get_ipython
# get_ipython().run_line_magic('matplotlib', 'widget')
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.express as px
import plotly.graph_objs as go

import order_data

def generate_scatter_graph(df, datax, datay, text_field, bubble_size, size_scale):
    order_data.is_df_null(df)

    # if (datax | datay |  bubble_size| size_scale) == None:
    #     raise Exception("invalid field selection")
    

    data = go.Scatter(x = datax, 
                    y = datay,
                    text = df[text_field],
                    mode = "markers", 
                    marker=dict(
                        size=bubble_size/max(bubble_size) *size_scale,
                        color=bubble_size, 
                        colorscale='Viridis',
                        sizemode = 'area', 
                        showscale=True)
                        )
    return data

def generate_scatter(df, xfield, yfield, size_scale):
    order_data.is_df_null(df)
    # if (xfield | yfield | size_scale) == None:
    #     raise Exception("invalid field selection")
    
    datax = df[xfield].tolist()
    datay = df[yfield].tolist()
    FaultCount = df["FaultCount"].tolist()
    FaultCount = np.array(FaultCount)
    data = generate_scatter_graph(df, datax, datay, "FaultCount", FaultCount, size_scale)   
    return data

def gen_bar(df, vobcid, loc_name):
    order_data.is_df_null(df)
    df = order_data.sort_by_VOBCID_Location(df, vobcid, loc_name)
    datax = df.index.tolist()
    datay = df['FaultCount'].tolist()
    fig = go.Bar(x=datax, y=datay)
    return fig



