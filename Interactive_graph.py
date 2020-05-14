
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
from dash.dependencies import Input, Output
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
df1 = order_data.sort_VOBCID_FaultCount(df, 300, [1,2,3])
data1 = data_gen_fc_as_size(df1,"LocationName", "VOBCID", 5000)



app = dash.Dash()

checkboxdict = dict_gen.dict_gen("FaultName", "Fault Code")
val = []
#for x in checkboxdict:
#    val.append()

app.layout = html.Div([
    html.Div([    
        html.Div([
            dcc.Graph(id = 'Scatterplot', 
                style={ 'float': 'left', "display":"block", "height" : "80vh",'width': "75vw"},
                
            ),
        ], className = "six columns"),

        html.Div([
            dcc.Checklist(
                id = 'Checklist',
                options= checkboxdict,
                value=  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
                style={'float': 'right', "height" : "80vh",'width': "20vw"}, 
                labelStyle={'display': 'block'}
            )
        ], className = "six columns"), 
    ],className="row")    
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

# app.layout = html.Div([S
#     html.Div([
#         html.Div([
#             html.H3('Column 1'),
#             dcc.Graph(id='g1', figure={'data': [{'y': [1, 2, 3]}]})
#         ], className="six columns"),

#         html.Div([
#             html.H3('Column 2'),
#             dcc.Graph(id='g2', figure={'data': [{'y': [1, 2, 3]}]})
#         ], className="six columns"),
#     ], className="row")
# ])


@app.callback(Output('Scatterplot', 'figure'),
                [Input('Checklist', 'value')])
def update_Scatter(faultcode_):

    df1 = order_data.sort_VOBCID_FaultCount(df, 300, faultcode_)
    data_1 = [data_gen_fc_as_size(df1,"LocationName", "VOBCID", 5000)]
    
    return{'data': data_1, 
            'layout':go.Layout(title = "Faults and Location")} 




if __name__ == "__main__":
    app.run_server()