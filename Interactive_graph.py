
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
from datetime import datetime as dt

import order_data
import dict_gen


from Graphs import generate_scatter

def data_gen_fc_as_size(df, xfield, yfield, size_scale):
    datax = df[xfield].tolist()
    datay = df[yfield].tolist()
    FaultCount = df["FaultCount"].tolist()
    FaultCount = np.array(FaultCount)
    data = generate_scatter(df, datax, datay, "FaultCount", FaultCount, size_scale)   
    return data


df = order_data.import_data("fc1.csv")

df1 = order_data.sort_FaultName_FaultCount(df)
df2 = order_data.sort_VOBCID_FaultCount(df, 300)

data1 = data_gen_fc_as_size(df1,"LocationName", "FaultName", 10000)
data2 = data_gen_fc_as_size(df2,"LocationName", "VOBCID", 5000)

app = dash.Dash()

checkboxdict = dict_gen.dict_gen("FaultName", "Fault Code")

app.layout = html.Div(children = [
        
        html.Div([
            dcc.Graph(id = 'Scatterplot', 
            figure = {'data':[data1], 
            'layout':go.Layout(title = "Faults and Location")}
            ),    

            dcc.Checklist(
            options= checkboxdict,
            value=[])  
        
        ]),
       
        dcc.Graph(id = 'Scatterplot2', 
        figure = {'data':[data2], 
        'layout':go.Layout(title = "VOBCID Faults at Location")
        }
        ),
])


if __name__ == "__main__":
    app.run_server()