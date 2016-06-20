import pandas as pd
import yahoo_finance as yahoo
from yahoo_finance import Share
from pandas import ExcelWriter
import time
import finsymbols as f
from pandas import ExcelWriter
import numpy as np
writer = ExcelWriter('c:\\temp\\heyo.xlsx')
print ('Script Start Time =' +time.ctime())

sp=[]
sp.append(f.get_sp500_symbols())


df =pd.DataFrame(sp[0])



stocks = df['symbol']
list1=[]
list2=[]
list3=[]
#list4=[]
list5=[]
list6=[]
for stock in stocks:
	yahoo = Share(stock)
	list1.append((yahoo.get_price()))
	list2.append((yahoo.get_open()))
	list3.append((str(stock)))
	#list4.append((yahoo.get_market_cap()))
	list5.append((yahoo.get_price_earnings_ratio()))
	list6.append((yahoo.get_price_earnings_growth_ratio()))
Last = zip(list3,list1,list2,list5,list6)


df2=pd.DataFrame(Last)


dff=pd.concat([df,df2],axis=1)
dff.rename(columns = {0:'Symbol',1:'Current_Price',2:'Open_Price',3:'P/E Ratio',4:'P/E/G Ratio'},inplace=True)

dff.sort_values(['symbol'], ascending =True)

dff.to_excel(writer,'Data',index=None) 




writer.save() 

print ('Script End Time =' +time.ctime())




	
	


