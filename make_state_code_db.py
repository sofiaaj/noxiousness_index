
import os 
import csv

f = open("state_codes_pulse.txt","r")
row_list = []
for x in f:
	x = x.replace("'","")
	x = x.replace(" ","")
	row = x.split("=")[0] + "," + x.split("=")[1]
	print(row)
	row_list.append(row)

file = open("state_codes.csv","w")
for row in row_list:
	file.write(row + "\n")
file.close()
