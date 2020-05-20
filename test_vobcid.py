
import pytest
import Graphs
import order_data
import Interactive_graph as ig
import pandas as pd
import numpy
import plotly
import dict_gen


df = pd.read_csv('fc1.csv', index_col= "LoggedAt")
df.index = pd.to_datetime(df.index)
df2 = None
df3 = df[df["FaultName"] == 0]

 
def test_is_df_null():
    order_data.is_df_null(df)
    order_data.is_df_null(df3)
    with pytest.raises(Exception):
        assert order_data.is_df_null(df2)

def test_import_data_exceptions():
    with pytest.raises(Exception):
        assert order_data.import_data("fc.csv")

def test_import_data():
    x = order_data.import_data("fc1.csv")
    assert len(df.index) == len(x.index)
    assert df.size == x.size

def test_sort_VOBCID_FaultCount_smallamt():
    x = order_data.sort_VOBCID_FaultCount(df, 300)
    assert len(x.index) == 300 

def test_sort_VOBCID_FaultCount_largeamt():
     x = order_data.sort_VOBCID_FaultCount(df, 3000)
     assert len(x.index) == 3000 

def test_sort_by_VOBCID_Location():
    x = order_data.sort_by_VOBCID_Location(df, 240, 'GRE-DEB')
    assert x is not None
    assert len(x) == 52

def test_sort_Dates_exceptions():
    with pytest.raises(Exception):
        assert order_data.sort_Dates(df, df.index.max(), df.index.min())
    with pytest.raises(Exception):
        assert order_data.sort_Dates(df2, None, None)

def test_sort_Dates():
    assert len(df) == len(order_data.sort_Dates(df, None, None))
    assert len(df) == len(order_data.sort_Dates(df, None, df.index.max()))
    assert len(df) == len(order_data.sort_Dates(df, df.index.min(), None))
    assert len(df) == len(order_data.sort_Dates(df, df.index.min(), df.index.max()))

def test_generate_scatter_graph():
    with pytest.raises(Exception):
        Graphs.generate_scatter_graph(df, None, None, None, None, None)

def test_generate_scatter():
    x = order_data.sort_VOBCID_FaultCount(df, 3000)
    data = Graphs.generate_scatter(x, "LocationName", "VOBCID", 5000)
    assert isinstance(data, plotly.graph_objs._scatter.Scatter)
    assert data is not None

def test_generate_scatter_exceptions():
    x = order_data.sort_VOBCID_FaultCount(df, 3000)
    with pytest.raises(Exception):
        assert Graphs.generate_scatter(x,None, "s", 5000)
    with pytest.raises(Exception):
        assert Graphs.generate_scatter(x,23, "sda", 5000)

def test_gen_bar():
    data =  Graphs.gen_bar(df, 240, 'GRE-DEB')
    assert data is not None
    assert isinstance(data, plotly.graph_objs._bar.Bar)
def test_gen_bar_exceptions():
    with pytest.raises(Exception):
        assert Graphs.gen_bar(df, 24777, None)
    


dictionary = [{'label': '01. Passenger Alarm', 'value': 1},
 {'label': '02. FAR Level 2 Fault', 'value': 2},
 {'label': '03. FAR Level 3 Fault', 'value': 3},
 {'label': '04. Failed to Dock', 'value': 4},
 {'label': '05. Dynamic Brake Failure', 'value': 5},
 {'label': '06. Converter Failure', 'value': 6},
 {'label': '07. FAR Level 1 Fault', 'value': 7},
 {'label': '08. Train Overspeed', 'value': 8},
 {'label': '09. Target Point Overshoot', 'value': 9},
 {'label': '10. Rollback', 'value': 10},
 {'label': '11. V = 0 Failure', 'value': 11},
 {'label': '12. Obstruction in AUTO Mode', 'value': 12},
 {'label': '13. EB Test Failure', 'value': 13},
 {'label': '14. Power Deselect Failure', 'value': 14},
 {'label': '15.Loss of Door Closed Status', 'value': 15}]
def test_dict_gen_scatterplot1():
    x = dict_gen.dict_gen_scatterplot1("FaultName", "Fault Code")
    assert x == dictionary
    with pytest.raises(Exception):
        assert dict_gen.dict_gen_scatterplot1("FaultName", None)

def test_display_click_data(dash_br):
    x = ig.display_click_data(None, 5, df.index.min(), df.index.max(), df)
    x