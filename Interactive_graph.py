
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
import json

from dash.dependencies import Input, Output
from datetime import datetime as dt
from datetime import datetime as dt
import re


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
df.index = pd.to_datetime(df.index)

# df1 = order_data.sort_VOBCID_FaultCount(df, 300, [1,2,3])
# data1 = data_gen_fc_as_size(df1,"LocationName", "VOBCID", 5000)



app = dash.Dash()

checkboxdict = dict_gen.dict_gen("FaultName", "Fault Code")


app.layout = html.Div([
    html.Div([    
        html.Div([
            dcc.Graph(id = 'Scatterplot', 
                style={ 'float': 'left', "display":"block", "height" : "80vh",'width': "75vw"},
                
            ),
        ], className = "six columns"),

        html.Div([
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            dcc.Checklist(
                id = 'Checklist',
                options= checkboxdict,
                value=  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
                style={'float': 'right', "height" : "40vh",'width': "20vw"}, 
                labelStyle={'display': 'block'}
            )
        ], className = "six columns"),

        html.Div([  
        dcc.DatePickerRange(
            id='date-range',
            min_date_allowed=df.index.min(),
            max_date_allowed=df.index.max(),
            initial_visible_month=df.index.min(),
            end_date=df.index.max(),
        )], className = "six columns")

        html.Div([
            html.Pre(id='click-data', style=styles['pre']),
        ], className="six columns")

    ],className="row"),

    

])


@app.callback(
    Output('click-data', 'children'),
    [Input('basic-interactions', 'clickData')])
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)


@app.callback(Output('Scatterplot', 'figure'),
                [Input('Checklist', 'value'),
                Input('date-range', 'start_date'),
                Input('date-range', 'end_date')])
def update_Scatter(faultcode_,start_date ,end_date):
    
    if start_date is not None and end_date is not None:
        mask = (df.index > start_date) & (df.index <= end_date)
        df1 = df.loc[mask]
    else:
        df1 = df

    if df1 is None:
        pass

    df1 = df1[df1['Fault Code'].isin(faultcode_)] 
    
    df1 = order_data.sort_VOBCID_FaultCount(df1, 300)
    data_1 = [data_gen_fc_as_size(df1,"LocationName", "VOBCID", 5000)]          
    
    return{'data': data_1,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
            'layout' : go.Layout(title = "Faults by VOBCID and LOCATION", 
                xaxis = {'title': 'Location'},
                yaxis = {'title': 'VOBCID'}, 
                hovermode="closest")
            }
    



if __name__ == "__main__":
    app.run_server()