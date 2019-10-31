# Write a python script to print the current date in the following format “Sun May 29
# 02:26:23 IST 2017”



import datetime
x=datetime.datetime.now()
print(x.strftime('%a %b %d %X %Y'))