import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def import_data(datasource):
    df = pd.read_csv(datasource, index_col= "LoggedAt")
    df.index = pd.to_datetime(df.index)
    return df

def sort_VOBCID_FaultCount(df, rtn_amt):
    df = df.groupby(["VOBCID", "LocationName"]).size()
    df = df.to_frame(name = 'FaultCount').reset_index()
    df = df.nlargest(rtn_amt,"FaultCount") 
    return df

def sort_by_VOBCID_Location(df, vobcid, loc_name):
    df = df[df['LocationName'].str.contains(loc_name)]
    df = df[df['VOBCID'] == (vobcid)]
    df = df.groupby(df.index.date).count()
    df = df["Fault Code"]
    df = df.to_frame(name = 'FaultCount')
    return df   

def sort_Dates(df, start_date, end_date):
    if start_date is not None and end_date is not None:
        mask = (df.index > start_date) & (df.index <= end_date)
        df = df.loc[mask]
    return df