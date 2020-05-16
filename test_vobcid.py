
import Graphs
import order_data
import Interactive_graph
import pandas as pd
import numpy
import plotly

df = pd.read_csv('fc1.csv', index_col= "LoggedAt")

 

# def test_import_data():
#     x = order_data.import_data("fc1.csv")
#     try: 
#         order_data.import_data("fc.csv")
#     except FileNotFoundError:
#         return
#     assert len(df.index) == len(x.index)
#     assert df.size == x.size

# def test_sort_VOBCID_FaultCount():
#      x = order_data.sort_VOBCID_FaultCount(df, 300)
#      assert len(x.index) == 300 

# def test_sort_by_VOBCID_Location():
#     x = order_data.sort_by_VOBCID_Location(df, 240, 'GRE-DEB')
#     assert x is not None

# def test_sort_VOBCID_FaultCount_1():
#      x = order_data.sort_VOBCID_FaultCount(df, 3000)
#      assert len(x.index) == 3000 

# def test_sort_FaultName_FaultCount():
#     x = order_data.sort_FaultName_FaultCount(df)
#     assert len(x.index) == 1264

# def test_data_gen_fc_as_size():
#     df2 = order_data.sort_VOBCID_FaultCount(df, 300)
#     fig = Interactive_graph.data_gen_fc_as_size(df2,"LocationName", "VOBCID", 5000)
#     assert fig is not None
#     assert isinstance(fig,plotly.graph_objs.Scatter)