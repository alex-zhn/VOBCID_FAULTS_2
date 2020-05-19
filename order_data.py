import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def is_df_null(df):
    if df is None:
        raise Exception('data source is null')


def import_data(datasource):
    df = pd.read_csv(datasource, index_col= "LoggedAt")
    is_df_null(df)
    df.index = pd.to_datetime(df.index)
    return df

def sort_VOBCID_FaultCount(df, rtn_amt):
    is_df_null(df)
    df = df.groupby(["VOBCID", "LocationName"]).size()
    df = df.to_frame(name = 'FaultCount').reset_index()
    df = df.nlargest(rtn_amt,"FaultCount") 
    return df

def sort_by_VOBCID_Location(df, vobcid, loc_name):
    is_df_null(df)
    df = df[df['LocationName'].str.contains(loc_name)]
    df = df[df['VOBCID'] == (vobcid)]
    df = df.groupby(df.index.date).count()
    df = df["Fault Code"]
    df = df.to_frame(name = 'FaultCount')
    return df   

def sort_Dates(df, start_date, end_date):
    is_df_null(df)
    if start_date is not None and end_date is not None:
        if start_date > end_date:
            raise Exception("invalid dates")
        mask = (df.index >= start_date) & (df.index <= end_date)
        df = df.loc[mask]
    return df