# from IPython import get_ipython
# get_ipython().run_line_magic('matplotlib', 'widget')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.express as px
import plotly.graph_objs as go


def generate_scatter(df, datax, datay, text_field, bubble_size, size_scale):
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




# coltouse = ["Fault Code", 
#         "FaultName",
#         "LoggedAt",
#         "VOBCID",
#         "LocationName"
#         ]
# title_font = {'family': 'source sans pro',
#         'color':  'darkblue',
#         'weight': 'normal',
#         'size': 20,
#         }

# labels_font = {'family': 'consolas',
#         'color':  'darkred',
#         'weight': 'normal',
#         'size': 15,
#         }




# def generate_graph(df, labels_font, title_font):
#     fig, ax = plt.subplots()
#     df.plot.scatter(ax=ax, x='LocationName', y='VOBCID', c='FaultCount',  colormap='plasma',rot = 90)
#     ax.tick_params(axis='x', which='major', labelsize=5)
#     ax.set_xlabel("Location Name", fontdict = labels_font)
#     ax.set_ylabel("VOBCID", fontdict = labels_font)
#     fig.tight_layout()
#     plt.show()


# if __name__ == "__main__":
#     df = import_data("fc1.csv", coltouse)
#     df = sort_and_short(df, 300)
#     generate_graph(df, labels_font, title_font)

# def import_data(datasource, col_used):
#     df = pd.read_csv(datasource, index_col= "LoggedAt",  usecols= col_used)
#     return df


# def sort_and_short(df, rtn_amt):
#     df = df.groupby(["VOBCID", "LocationName"]).size()
#     df = df.to_frame(name = 'FaultCount').reset_index()
#     df = df.nlargest(rtn_amt,"FaultCount") 
#     return df