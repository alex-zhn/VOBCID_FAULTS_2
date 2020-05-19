
import pytest
import Graphs
import order_data
import Interactive_graph
import pandas as pd
import numpy
import plotly


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
        assert order_data.sort_Dates(df2, None, None)
        assert order_data.sort_Dates(df3, None, None)

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
        assert Graphs.generate_scatter(x,23, "sda", 5000)

def test_gen_bar():
    pass

def test_dict_gen_scatterplot1():
    pass