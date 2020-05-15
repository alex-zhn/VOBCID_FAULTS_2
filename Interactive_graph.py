
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
import Graphs


df = order_data.import_data("fc1.csv")
df.index = pd.to_datetime(df.index)



app = dash.Dash()

checkboxdict = dict_gen.dict_gen("FaultName", "Fault Code")


app.layout = html.Div([
    html.Div([    
        html.Div([
            dcc.Graph(id = 'Scatterplot', 
                style={ 'float': 'left', "display":"block", "height" : "60vh",'width': "75vw"},
            
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
        )], className = "six columns"),
        
        html.Div([
            dcc.Graph(id = 'BarGraph', 
                #style={ 'float': 'left', "display":"block", "height" : "35vh",'width': "75vw"},
                
            ),
        ], className = "six columns")


    ],className="row"),

])


@app.callback(
    Output('BarGraph', 'figure'),[
    Input('Scatterplot', 'clickData'),
    Input('Checklist', 'value'),
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date')])
def display_click_data(clickData, faultcode_, start_date, end_date):
    df1 = order_data.sort_Dates(df, start_date, end_date)
    df1 = df1[df1['Fault Code'].isin(faultcode_)]

    if clickData is None:
        vobcid_ = 240
        location = 'GRE-DEB'
    else:
        vobcid_= clickData['points'][0]['y']
        location = clickData['points'][0]['x']

    if df1 is None:
        pass

    data_1 = [Graphs.gen_bar(df1, vobcid_, location)]
    
    return{'data': data_1,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
            'layout' : go.Layout(title = "Faults by Date VOBCID: {} Location: {}".format(vobcid_, location), 
                xaxis = {'title': 'Date'},
                yaxis = {'title': 'Faultcount'}, 
                hovermode="closest")
            }


@app.callback(Output('Scatterplot', 'figure'),
                [Input('Checklist', 'value'),
                Input('date-range', 'start_date'),
                Input('date-range', 'end_date')])
def update_Scatter(faultcode_,start_date ,end_date):
    
    df1 = order_data.sort_Dates(df, start_date, end_date)
    df1 = df1[df1['Fault Code'].isin(faultcode_)]
    
    if df1 is None:
        pass

    df1 = order_data.sort_VOBCID_FaultCount(df1, 300)
    data_1 = [Graphs.generate_scatter(df1,"LocationName", "VOBCID", 5000)]          
    
    return{'data': data_1,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
            'layout' : go.Layout(title = "Faults by VOBCID and LOCATION", 
                xaxis = {'title': 'Location'},
                yaxis = {'title': 'VOBCID'}, 
                hovermode="closest",
                clickmode =  'event+select')
            }
    


if __name__ == "__main__":
    app.run_server()
  




