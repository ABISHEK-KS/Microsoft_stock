import pandas as pd 
import sys
import os
import pandas_profiling as pp
import numpy as np 
np.set_printoptions(threshold=sys.maxsize)

df=pd.read_csv("microsoft_stocks.csv","r")
prof=pp.ProfileReport(df,title='MICROSOFT STOCK DATA PROFILING')
pd.set_option('display.max_colwidth', None)
prof.to_file("Microsoft_Stock_Data_Profiling.json")
prof.to_file("Microsoft_Stock_Data_Profiling.html")
