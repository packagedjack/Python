
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import pymssql as p
import time
from bs4 import BeautifulSoup
import re


base = ""
usr = ""
pwd = ""
writepath = "c:\\temp\\"
writer = pd.ExcelWriter()
####################################################################
#connect to DW
server =""
user =''
password =''
db =''
conn = p.connect(server, user, password)
cursor = conn.cursor()
script = """

"""
df = pd.read_sql(script,conn)

####################################################################
driver = webdriver.Ie("C:\Temp\IEDriverServer32.exe")#downgrade this driver to 32 bit, 64 bit interface is slow--Fixed 07/05--Running in about 3 seconds now
driver.get(base)

driver.implicitly_wait(2)

elem = driver.find_element_by_name("")
elem.send_keys(usr)
####################################################################

####################################################################
elem = driver.find_element_by_name("")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
####################################################################

####################################################################
driver.implicitly_wait(2)

####################################################################
##start for loops to iterate through a list of loans and parse HTML
####################################################################
counter = 0
list=[]
for lead in df.iterrows():
	driver.implicitly_wait(5)
	elem = driver.find_element_by_name("")
	elem.send_keys(df.iloc[counter])
	elem.send_keys(Keys.RETURN)

	driver.implicitly_wait(2)

	html = driver.page_source

	soup = BeautifulSoup(html)
	soup = str(soup)
	soup = soup.splitlines()
	
	for poop in soup:
		list.append( re.findall(r'<td><font color="blue">(.*)</font></td>',poop.strip()))
		
	list.append(df.iloc[counter])
	counter = counter + 1
	time.sleep(2)

list = filter(len,list)
df2=pd.DataFrame.from_records(list)
df2.to_excel(writer,sheet_name='Text')

writer.save()