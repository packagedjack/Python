import pandas as pd
import pymssql as p
from pandas import ExcelWriter
from pandas import ExcelFile
import urllib2
import string
from random import randint
from time import sleep
import time
import re

##########################################################################################
print time.ctime()

#Build Excel Writer for Pandas to create an excel sheet
writer = ExcelWriter('c:\\temp\\Zillowresults.xlsx')


##########################################################################################
import pymssql as p
#connect to DW
server =""
user =''
password =''
db =''
conn = p.connect(server, user, password)
cursor = conn.cursor()
##############################
htmlbase = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id='
key =''#API KEY

##########################################################################################


#script to execute. Put a query here that has address, city, street, state, zip, some values
script = ("""

"""
)

##########################################################################################


#execute script
cursor.execute (script)
data = cursor.fetchall()
##########################################################################################

print time.ctime()
#get all columns from query, put into memory
columns = [desc[0] for desc in cursor.description]




##########################################################################################

#Pandas to write Query Results to dataframe, append new column with URL to get XML
df = pd.DataFrame(data, index=None)
df[9]=(htmlbase+key+'&address='+df[df.columns[0]]+'+'+df[df.columns[1]]+'&' +'citystatezip='+df[df.columns[2]]+df[df.columns[5]]+'%2C+'+df[df.columns[3]])
[x.strip().replace(' ', '') for x in df[4]]



##########################################################################################
#define datapoints
zindexstring = re.compile(r'<amount currency="USD">([\d]*)</amount>')
##########################################################################################


#Empty Lists to Append Zestimate Data in ForLoop
Zestimate=[]
Latitude =[]
for rows in df[9]:
    newrows = rows
    finalURL = newrows.replace(' ', '')
    link = urllib2.urlopen(finalURL)
    sleep(randint(1,10))#this is just an attempt to try a method of sleeping an loop that is hitting a website, for API usage it really isn't necessary
    Zestimate.append(re.findall(zindexstring, link.read()))



df2 = pd.DataFrame.from_records(Zestimate,index=None)

print "Loops complete"
dff=pd.concat([df,df2],axis=1)
dff.to_excel(writer,'Zestimates',index=None)  
writer.save()  
print time.ctime()
