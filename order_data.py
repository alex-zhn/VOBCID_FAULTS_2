import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def import_data(datasource):
    df = pd.read_csv(datasource, index_col= "LoggedAt")
    return df

def sort_VOBCID_FaultCount(df, rtn_amt):
    df = df.groupby(["VOBCID", "LocationName"]).size()
    df = df.to_frame(name = 'FaultCount').reset_index()
    df = df.nlargest(rtn_amt,"FaultCount") 
    return df

def sort_by_VOBCID_Location(df, vobcid, loc_name):
    df = df[df['LocationName'].str.contains(loc_name)]
    df = df[df['VOBCID'] == (vobcid)]
    return df   

# def sort_FaultName_FaultCount(df):
#     df = df.groupby(["LocationName", "FaultName", "Fault Code"]).size()
#     df = df.to_frame(name = 'FaultCount').reset_index()
#     df = df.sort_values("FaultName")
#     return df