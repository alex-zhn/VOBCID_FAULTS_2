import VobcFault 
import Graphs
import pandas as pd
import numpy

df = pd.read_csv('fc1.csv', index_col= "LoggedAt")

 

def test_get_fault_count():
    x  = VobcFault.get_row_count(df) 
    assert x is not None
    assert x == 389348 

def test_get_fault_count_by_fault1():
    x = VobcFault.get_row_count_by_fault(df,1)
    assert x == 867

def test_get_fault_count_by_fault3():
    x = VobcFault.get_row_count_by_fault(df,3)
    assert x == 292484

def test_import_data():
    x = Graphs.import_data("fc1.csv", all)
    assert len(df.index) == len(x.index)
    assert df.size == x.size

def test_sort_and_short():
    x = Graphs.sort_and_short(df, 300)
    assert len(x.index) == 300 

   
   