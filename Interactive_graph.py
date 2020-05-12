
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.express as px
import plotly.graph_objs as go

import dash as dash
import dash_core_components as dcc 
import dash_html_components as html 

from order_data import import_data
from order_data import sort_FaultName_FaultCount
from order_data import sort_VOBCID_FaultCount

from Graphs import generate_scatter

def data_gen(df, xfield, yfield, bubble_size):
    datax = df[xfield].tolist()
    datay = df[yfield].tolist()
    FaultCount = df["FaultCount"].tolist()
    FaultCount = np.array(FaultCount)
    data = generate_scatter(df, datax, datay, "FaultCount", FaultCount, bubble_size)   
    return data


df = import_data("fc1.csv")

df1 = sort_FaultName_FaultCount(df)
df2 = sort_VOBCID_FaultCount(df, 300)

data1 = data_gen(df1,"LocationName", "FaultName", 10000)
data2 = data_gen(df2,"LocationName", "VOBCID", 5000)

app = dash.Dash()

app.layout = html.Div(children = [
        dcc.Graph(id = 'Scatterplot', 
        figure = {'data':[data1], 
        'layout':go.Layout(title = "Faults and Location")
        }
        ),
       
        dcc.Graph(id = 'Scatterplot2', 
        figure = {'data':[data2], 
        'layout':go.Layout(title = "VOBCID Faults at Location")
        }
        ),
])


if __name__ == "__main__":
    app.run_server()