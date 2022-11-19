import os
import csv

count = 0

with open('listapps.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
    	#Execute SimiDroid to compare both file (original and repackage)
    	#and create a Json File with the comparation
        command = None
        command="java -jar SimiDroid.jar "+"/benign-"+row[0]+".apk"+" /malicious-"+row[0]+".apk"
        print(command)
        os.system(command)
        count=count+1
