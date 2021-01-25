import pandas as pd

ret_df = pd.read_csv('C:\Python\FtseCluster\data\Filtered_FTSE All-share_PriceData-Sep2018_to_Current.csv')
ret_idx=pd.read_csv('C:\Python\FtseCluster\data\Filtered_Indices_PriceData-Sep2018_to_Current.csv')
compinfo=pd.read_csv('C:\Python\FtseCluster\data\Filtered_FTSE All-share_CompanyInfo_nonInv.csv')
def cleanPriceData_df(ret_df):
    ret_df = ret_df.iloc[:, :-1]
    ret_df = ret_df.transpose()
    ticnames = ret_df.iloc[0, :]
    ret_df = ret_df.iloc[1:, :]
    dates = ret_df.index.str.split().str.get(-1)
    dates = pd.to_datetime(dates)
    ret_df = ret_df.set_index(dates)
    ret_df.columns = ticnames
    ret_df = ret_df.fillna(0)
    return ret_df

compinfo = compinfo.set_index('TIDM')

ret_idx = cleanPriceData_df(ret_idx)
ret_df = cleanPriceData_df(ret_df)

mask = compinfo.Industry=='Consumer Discretionary'
con_disc_epics = compinfo[mask].index
con_disc_epics_df = ret_df[con_disc_epics]
con_disc_epics_df
