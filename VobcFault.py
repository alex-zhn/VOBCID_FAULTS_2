
import pandas as pd
#import matplotlib.pyplot as plt

dfi = pd.read_csv('fc1.csv', index_col= "LoggedAt")



def get_row_count(df):
    return len(df.index)
    

def get_row_count_by_fault(df, faultcode):
    return len(df[df["Fault Code"] == faultcode])
  

if __name__ == "__main__":
    print(get_row_count(dfi))
    print(get_row_count_by_fault(dfi, 3))
