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






